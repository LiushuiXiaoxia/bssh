import logging

import paramiko

import g
import logic.model
from logic.model import SshConnectModel, ResultMsg

STATUS_NONE = 'none'
STATUS_CONNECTED = 'connected'
STATUS_DISCONNECTED = 'disconnected'
STATUS_RUNNING = 'running'
STATUS_SUCCESS = 'success'
STATUS_FAILED = 'fail'


class MySshClient:

    def __init__(self, model: SshConnectModel):
        self.checked = False
        self.sshModel = model
        self.client = paramiko.SSHClient()
        self.connect_success = False
        self.is_run = False
        self.status = STATUS_NONE

    def connect(self, callback=None):
        # Thread(target=self._connect, args=[callback, ]).start()
        g.pool.submit(self._connect, callback, )
        pass

    def _connect(self, callback=None):
        model = self.sshModel
        msg = f'connect {model.ip}:{model.port} success :)'
        try:
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # self.client.connect(model.ip, model.port, model.username, timeout=5)
            self.client.connect(model.ip, model.port, model.username, model.password, timeout=5)
            logging.info(msg)

            self.connect_success = True
            self.status = STATUS_CONNECTED
            g.bus.emit(g.EVENT_CONNECT, self, msg)
        except Exception as e:
            msg = f'connect {model.ip} fail, error = {e}, :('
            logging.info(msg)

            self.connect_success = False
            self.status = STATUS_DISCONNECTED
            g.bus.emit(g.EVENT_CONNECT, self, msg)

        key = self.sshModel.key
        callback(self, ResultMsg(key, msg, err=not self.connect_success, status=logic.model.STATUS_UNKNOWN))

    def exec(self, cmd_list, callback, client_callback, cmd_callback):
        if self.is_run or not self.connect_success:
            logging.info(f"can not exec cmd, is_run = {self.is_run}, connect_success = {self.connect_success}")
            return

        # Thread(target=self._exec, args=[cmd_list, callback, ]).start()
        g.pool.submit(self._exec, cmd_list, callback, client_callback, cmd_callback)
        pass

    def _exec(self, cmd_list, callback, client_callback, cmd_callback):
        model = self.sshModel
        self.is_run = True
        self.status = STATUS_RUNNING

        key = self.sshModel.key
        callback(self, ResultMsg(key, "", status=logic.model.STATUS_EXEC_BEFORE))

        for cmd in cmd_list:
            logging.info(f'{model.ip} > {cmd}')
            callback(self, ResultMsg(key, cmd, status=logic.model.STATUS_RUN_BEGIN))

            if len(cmd) > 0:
                stdin, stdout, stderr = self.client.exec_command(cmd)
                while True:
                    line = stdout.readline()
                    if not line:
                        break
                    callback(self, ResultMsg(key, line.rstrip(), status=logic.model.STATUS_RUNNING))
                    logging.info(f'[{model.ip}/I] {line.rstrip()}')

                while True:
                    line = stderr.readline()
                    if not line:
                        break
                    callback(self, ResultMsg(key, line.rstrip(), err=True, status=logic.model.STATUS_RUNNING))
                    logging.info(f'[{model.ip}/E] {line.rstrip()}')

            cmd_callback()
            callback(self, ResultMsg(key, "", status=logic.model.STATUS_RUN_END))

        client_callback()
        callback(self, ResultMsg(key, "", status=logic.model.STATUS_EXEC_AFTER))

        logging.info(f'[{model.ip}] finish')
        self.is_run = False
        self.status = STATUS_SUCCESS

    def destroy(self):
        self.client.close()
        pass
