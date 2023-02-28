import os


def get_user_home():
    return os.environ['HOME']


def get_app_data_dir():
    d = os.path.join(get_user_home(), ".batch-ssh-client")
    if not os.path.exists(d):
        os.mkdir(d)
    return d


def get_app_data_file(name):
    d = get_app_data_dir()
    f = os.path.join(d, name)
    return f
