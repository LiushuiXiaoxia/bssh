# 定义主窗体
import logging

from PySide2 import QtWidgets, QtCore

import g
from logic import SshManager
from logic.config import isDev
from ui.SettingWidget import Ui_SettingWidget


class SettingDialog(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(SettingDialog, self).__init__(parent)

        self.ui = Ui_SettingWidget()
        self.ui.setupUi(self)

        self.ui.edtHosts.textChanged.connect(self.text_change)
        self.ui.edtAccount.textChanged.connect(self.text_change)
        self.ui.edtPassword.textChanged.connect(self.text_change)
        self.ui.edtPort.textChanged.connect(self.text_change)

        self.ui.btnAdd.clicked.connect(self._handle_add)
        self.ui.btnEdit.clicked.connect(self._handle_edit)
        self.ui.btnRemove.clicked.connect(self._handle_remove)
        self.ui.btnMoveUp.clicked.connect(self._handle_move_up)
        self.ui.btnMoveDown.clicked.connect(self._handle_move_down)

        # no impl
        self.ui.btnEdit.setVisible(False)
        self.setWindowTitle("设置")

        self.ui.tvClients.horizontalHeader().setSectionsClickable(False)
        self.ui.tvClients.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
        self.ui.tvClients.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)
        self.ui.tvClients.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.ui.tvClients.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.ui.tvClients.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)

        if isDev():
            self.test_text()
            pass

    def test_text(self):
        self.ui.edtHosts.setPlainText("\n".join(g.testHosts.split('\n')).strip())
        self.ui.edtAccount.setText(g.testUser)
        self.ui.edtPassword.setText(g.testPasswd)

    def setup(self):
        self.update_table()

    def update_table(self):
        self.ui.tvClients.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tvClients.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tvClients.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # self.ui.tvClients.itemClicked.connect(self.itemClickChanged)
        self.ui.tvClients.selectionModel().selectionChanged.connect(self.selected_change)

        self.models = SshManager.getAllModels()
        self.ui.tvClients.setRowCount(len(self.models))
        for i, it in enumerate(self.models):
            item0 = QtWidgets.QTableWidgetItem(str(i + 1))
            item0.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.ui.tvClients.setItem(i, 0, item0)

            self.ui.tvClients.setItem(i, 1, QtWidgets.QTableWidgetItem(it.ip))
            self.ui.tvClients.setItem(i, 2, QtWidgets.QTableWidgetItem(it.username))

            item3 = QtWidgets.QTableWidgetItem(str(it.port))
            item3.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.ui.tvClients.setItem(i, 3, item3)

    def selected_change(self, selected, deselected):
        logging.info(f'selected_change selected = {selected}, deselected = {deselected}')
        row = self.ui.tvClients.currentRow()
        logging.info(f'itemClickChanged.row = {row}')
        self.ui.btnEdit.setEnabled(row >= 0)
        self.ui.btnRemove.setEnabled(row >= 0)
        self.ui.btnMoveUp.setEnabled(row > 0)
        self.ui.btnMoveDown.setEnabled(row < len(self.models) - 1)

    def text_change(self, obj=None):
        hosts = self.ui.edtHosts.toPlainText().strip()
        account = self.ui.edtAccount.text().strip()
        password = self.ui.edtPassword.text().strip()
        port = self.ui.edtPort.text().strip()
        e = len(hosts) == 0 or len(account) == 0 or len(password) == 0
        self.ui.btnAdd.setEnabled(not e)
        pass

    def _handle_add(self):
        hosts = self.ui.edtHosts.toPlainText().strip()
        account = self.ui.edtAccount.text().strip()
        password = self.ui.edtPassword.text().strip()
        port = self.ui.edtPort.text().strip()
        if len(port) == 0:
            port = "22"

        ips = hosts.split("\n")
        SshManager.addConnect(ips, account, password, port)

        self.update_table()
        self.ui.tvClients.scrollToBottom()
        pass

    def _handle_edit(self):
        pass

    def _handle_remove(self):
        row = self.ui.tvClients.currentRow()
        SshManager.removeConnect(row)

        self.update_table()
        # self.selected_change()
        pass

    def _handle_move_up(self):
        row = self.ui.tvClients.currentRow()
        logging.info(f'_handle_move_down.row = {row}')

        if row - 1 >= 0:
            SshManager.swap(row - 1, row)
            self.update_table()

            self.ui.tvClients.selectRow(row - 1)
            # self.selected_change()
        pass

    def _handle_move_down(self):
        row = self.ui.tvClients.currentRow()
        logging.info(f'_handle_move_down.row = {row}')

        if row + 1 < len(SshManager.getAllModels()):
            SshManager.swap(row + 1, row)
            self.update_table()

            self.ui.tvClients.selectRow(row + 1)
            # self.selected_change()
        pass

    def closeEvent(self, args) -> None:
        SshManager.refresh()
        pass
