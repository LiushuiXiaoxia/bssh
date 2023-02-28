import os

import g


def get_user_home():
    return os.environ['HOME']


def get_app_data_dir():
    d = os.path.join(get_user_home(), f".{g.APP_NAME}")
    if not os.path.exists(d):
        os.makedirs(d)
    return d


def get_app_data_file(name):
    d = get_app_data_dir()
    f = os.path.join(d, name)
    return f


def get_app_log_dir():
    d = get_app_data_dir()
    f = os.path.join(d, "logs")

    if not os.path.exists(f):
        os.makedirs(f)
    return f
