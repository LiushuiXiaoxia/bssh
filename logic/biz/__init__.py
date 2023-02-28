import json
import logging
import os
from threading import Lock

from logic.biz.client import MySshClient
from logic.model import dict2SshConnectModel, newSshConnectModel, mode2Dict
from logic.util import filekit

_all_models = []
_all_clients = []
_data_file = filekit.get_app_data_file("data.json")


def _load():
    _all_models.clear()
    _all_clients.clear()
    if os.path.exists(_data_file):
        with open(_data_file) as f:
            t = f.read()

        for it in json.loads(t):
            m = dict2SshConnectModel(it)
            _all_models.append(m)
            _all_clients.append(MySshClient(m))


def _save():
    ret = []
    for m in _all_models:
        ret.append(mode2Dict(m))
    s = json.dumps(ret, indent=4)
    with open(_data_file, 'w') as f:
        f.write(s)


class SshManager:
    completeClientSize = 0
    totalClientSize = 0

    completeCmdSize = 0
    totalCmdSize = 0

    @staticmethod
    def load():
        _load()

        select_client = []
        for it in _all_clients:
            select_client.append(it)
        logging.debug(f'all = {_all_clients}')
        pass

    @staticmethod
    def addConnect(hosts, username, password, port):
        for ip in hosts:
            m = newSshConnectModel(ip, port, username, password, )
            _all_models.append(m)
        pass

    @staticmethod
    def removeConnect(idx):
        _all_models.pop(idx)
        pass

    @staticmethod
    def swap(new, old):
        t = _all_models[new]
        _all_models[new] = _all_models[old]
        _all_models[old] = t
        pass

    @staticmethod
    def refresh():
        _save()
        SshManager.disconnectAll()
        _load()
        pass

    @staticmethod
    def connectAll(callback=None):
        logging.info('connectAll')

        for cs in _all_clients:
            cs.connect(callback)
        pass

    @staticmethod
    def disconnectAll():
        logging.info('disconnectAll')

        for cs in _all_clients:
            cs.destroy()

    @staticmethod
    def getAllClients():
        return _all_clients

    @staticmethod
    def getAllModels():
        return _all_models

    @staticmethod
    def getClientByKey(key):
        for it in _all_clients:
            if it.sshModel.key == key:
                return it
        return None

    @staticmethod
    def getSelectClients():
        ret = []
        for it in _all_clients:
            if it.checked:
                ret.append(it)
        return ret

    @staticmethod
    def execCmd(cmd_list, callback):
        clients = SshManager.getSelectClients()
        cs = len(clients)
        SshManager.completeClientSize = 0
        SshManager.totalClientSize = cs

        SshManager.completeCmdSize = 0
        SshManager.totalCmdSize = len(cmd_list) * cs

        mutex = Lock()

        def client_complete_callback():
            mutex.acquire()
            SshManager.completeClientSize += 1
            mutex.release()
            pass

        def cmd_complete_callback():
            mutex.acquire()
            SshManager.completeCmdSize += 1
            mutex.release()
            pass

        for c in clients:
            c.exec(cmd_list, callback, client_complete_callback, cmd_complete_callback)
        pass
