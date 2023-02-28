import hashlib


class SshConnectModel:

    def __init__(self):
        self.ip = ''
        self.port = 22
        self.username = ''
        self.password = ''
        self.key = ''

    def hashKey(self):
        key = f'{self.username}-{self.ip}-{self.port}'
        md5 = hashlib.md5()
        md5.update(key.encode())
        self.key = md5.hexdigest()

    def desc(self):
        return f'ssh {self.username}@{self.ip} -p {self.port}'


def newSshConnectModel(ip, port, username, password):
    it = SshConnectModel()
    it.ip = ip
    it.port = int(port)
    it.username = username
    it.password = password
    it.hashKey()
    return it


def dict2SshConnectModel(d):
    it = SshConnectModel()
    it.ip = d['ip']
    it.port = d['port']
    it.username = d['username']
    it.password = d['password']
    it.hashKey()
    return it


def mode2Dict(m: SshConnectModel):
    return {
        'ip': m.ip,
        'port': m.port,
        'username': m.username,
        'password': m.password,
    }


# 未知
STATUS_UNKNOWN = 0
# 全局开始
STATUS_EXEC_BEFORE = 1
# 单个开始
STATUS_RUN_BEGIN = 2
# 执行中
STATUS_RUNNING = 3
# 单个结束
STATUS_RUN_END = 4
# 全局结束
STATUS_EXEC_AFTER = 5


class ResultMsg:
    key = ""
    msg = ""
    cmd = ""
    status = 0
    err = False

    def __init__(self, key, msg, cmd="", err=False, status=STATUS_UNKNOWN):
        self.key = key
        self.msg = msg
        self.cmd = cmd
        self.status = status
        self.err = err
