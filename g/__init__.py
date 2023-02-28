import multiprocessing

from concurrent.futures import ThreadPoolExecutor
from event_bus import EventBus

EVENT_CONNECT = 'connect'
bus = EventBus()

APP_NAME = "bssh"
APP_FULL_NAME = "batch ssh client"
APP_VERSION = 2
APP_VERSION_NAME = '0.0.2'

_count = max(20, multiprocessing.cpu_count() * 2)
print(f'count = {_count}')
pool = ThreadPoolExecutor(max_workers=_count)

testCmd = [
    "pwd",
    "hostname",
    "ls -l",
    "bash test.sh",
]

testHosts = '''
10.19.17.10
10.19.17.11
10.19.17.12
10.19.17.13
10.19.17.14
'''

testUser = 'admin'
testPasswd = 'admin'
