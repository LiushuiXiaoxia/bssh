import logging
import os
from logging.handlers import RotatingFileHandler

from logic.config import currentEnv, ENV_DEVELOPMENT


def init_log():
    mf = '%(asctime)s [%(levelname)-.5s] %(filename)12s:%(lineno).3d - %(message)s'
    tf = '%Y-%m-%d %H:%M:%S'

    log_dir = 'logs'
    if currentEnv == ENV_DEVELOPMENT:
        logging.basicConfig(level=logging.DEBUG, format=mf, datefmt=tf)
    else:
        logging.basicConfig(level=logging.INFO, format=mf, datefmt=tf)
        log_dir = '/tmp/logs/bssh'

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    f = os.path.join(log_dir, "access.log")
    file_log_handler = RotatingFileHandler(f, maxBytes=100 * 1024 * 1024, backupCount=10)
    file_log_handler.setFormatter(logging.Formatter(mf, tf))
    logging.getLogger().addHandler(file_log_handler)
