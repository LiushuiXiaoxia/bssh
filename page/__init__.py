import logging
import sys

from PySide2.QtWidgets import QApplication

from logic import SshManager
from page.main import MainPage

app = QApplication(sys.argv)
mp = MainPage()

def start_ui():
    mp.update_hosts_ui(True)
    mp.show()
    mp.setup()

    sys.exit(app.exec_())


def exit_app():
    logging.info('stop_ui')
    SshManager.disconnectAll()
    app.quit()
