from PySide2 import QtWidgets

import g


def show_about(parent):
    msg = [
        f'{g.APP_NAME}({g.APP_FULL_NAME})',
        f'author: xiaqiulei',
        f'version: v{g.APP_VERSION_NAME}',
    ]
    QtWidgets.QMessageBox.about(parent, '关于', "\n".join(msg))
