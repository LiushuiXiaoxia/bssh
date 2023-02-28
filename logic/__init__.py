from logic.biz import SshManager
from logic.log import init_log


def setup():
    init_log()
    SshManager.load()
