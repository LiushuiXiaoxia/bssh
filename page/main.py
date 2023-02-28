# 定义主窗体
import logging
from functools import partial

import PySide2
from PySide2 import QtWidgets, QtCore, QtGui

import g
import logic
import page
from logic import SshManager
from logic.config import isDev
from logic.model import ResultMsg
from page.about import show_about
from page.setting import SettingDialog
from ui.MainWindow import Ui_MainWindow


class MainPage(QtWidgets.QMainWindow):
    output_signal = QtCore.Signal(ResultMsg)
    hosts_signal = QtCore.Signal(str)

    def __init__(self):
        super(MainPage, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnClean.clicked.connect(self._handle_clear)
        self.ui.btnRun.clicked.connect(self._handleRun)
        self.ui.btnRefresh.clicked.connect(self._handle_refresh)
        self.ui.btnSetting.clicked.connect(self._handle_setting)
        self.ui.edtCmd.textChanged.connect(self._edtCmdChange)
        self.ui.cbSelectAll.setChecked(False)
        self.ui.cbSelectAll.stateChanged.connect(self.select_all_change)

        self.ui.btnRun.setEnabled(False)
        if isDev():
            self.ui.edtCmd.setText("\n".join(g.testCmd))

        self.output_signal.connect(lambda p: self.exec_callback_update(p))
        self.hosts_signal.connect(lambda p: self._update_host_by_signal())

        self.ui.tvHosts.horizontalHeader().setSectionsClickable(False)
        self.ui.tvHosts.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter)
        self.ui.tvHosts.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.ui.tvHosts.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.ui.tvHosts.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        # self.ui.tvHosts.horizontalHeader().setStretchLastSection(True)
        self.ui.tvHosts.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.ui.tvHosts.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tvHosts.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tvHosts.selectionModel().selectionChanged.connect(self.selected_change)

        self.ui.actionClose.triggered.connect(lambda p: page.exit_app())
        self.ui.actionSetting.triggered.connect(self._handle_setting)
        self.ui.actionAbout.triggered.connect(lambda p: show_about(self))

        self.allTabEditMap = {}

        self.setWindowTitle(g.APP_NAME)

    def update_hosts_ui(self, first=False):
        cs = SshManager.getAllClients()
        self.ui.tvHosts.setRowCount(len(cs))
        for idx in range(len(cs)):
            it = cs[idx]

            item1 = QtWidgets.QTableWidgetItem(it.sshModel.ip)
            # item1.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.ui.tvHosts.setItem(idx, 0, item1)

            item2 = QtWidgets.QTableWidgetItem(it.status)
            # item2.setTextAlignment(QtCore.Qt.AlignHCenter)
            self.ui.tvHosts.setItem(idx, 1, item2)

            cb = QtWidgets.QCheckBox()
            cb.setChecked(it.checked)
            cb.stateChanged.connect(partial(self._item_checked_changed, cb, idx, ))
            layout = QtWidgets.QHBoxLayout()
            layout.setAlignment(QtCore.Qt.AlignCenter)
            layout.addWidget(cb)
            w = QtWidgets.QWidget()
            w.setLayout(layout)
            self.ui.tvHosts.setCellWidget(idx, 2, w)

        if len(cs) > 0:
            self.ui.tvHosts.selectRow(0)

        if first:
            self._initTab()

    def _initTab(self):
        for i in range(self.ui.tabOutput.count()):
            self.ui.tabOutput.removeTab(0)

        cs = SshManager.getAllClients()
        for idx in range(len(cs)):
            it = cs[idx]
            edt = QtWidgets.QPlainTextEdit(self.ui.centralwidget)
            edt.setEnabled(True)
            edt.setPlainText(f'{it.sshModel.desc()}')

            font = QtGui.QFont()
            font.setFamily(u"Monaco")
            edt.setFont(font)
            edt.setReadOnly(True)

            layout = QtWidgets.QHBoxLayout()
            layout.addWidget(edt)
            tab = QtWidgets.QTabWidget()
            tab.setLayout(layout)

            if len(cs) <= 5:
                self.ui.tabOutput.addTab(tab, f' {idx + 1} {it.sshModel.ip}')
            else:
                self.ui.tabOutput.addTab(tab, f' {idx + 1}')
                # self.ui.tabOutput.addTab(tab, f' {idx + 1} {it.sshModel.ip}')

            self.allTabEditMap[it.sshModel.key] = edt

    def selectAll(self):
        self.ui.cbSelectAll.setChecked(True)

    def setup(self):
        self.selectAll()

        @g.bus.on(g.EVENT_CONNECT)
        def connect_change(client, msg):
            logging.info(f"connect_change client = {client}, msg = {msg}")
            self.hosts_signal.emit('')
            pass

        SshManager.connectAll(self._execCallback)

    def _update_host_by_signal(self):
        self.update_hosts_ui()
        pass

    def _handle_clear(self):
        logging.info(f'do_clean')
        for key in self.allTabEditMap:
            edt = self.allTabEditMap[key]
            edt.clear()
            c = SshManager.getClientByKey(key)
            logging.info(f'{key} -> {c}')
            edt.setPlainText(f'{c.sshModel.desc()}')

    def select_all_change(self):
        cs = SshManager.getAllClients()
        check = self.ui.cbSelectAll.isChecked()
        for it in cs:
            it.checked = check

        self.update_hosts_ui()
        pass

    def _item_checked_changed(self, cb: QtWidgets.QCheckBox, idx, status):
        logging.info(f'_item_checked_changed args = {idx}, status = {status}')
        cs = SshManager.getAllClients()
        cs[idx].checked = cb.isChecked()
        pass

    def selected_change(self, selected, deselected):
        logging.info(f'selected_change selected = {selected}, deselected = {deselected}')
        row = self.ui.tvHosts.currentRow()
        key = SshManager.getAllModels()[row].key
        logging.info(f'selected_change.row = {row}')

        cs = SshManager.getAllClients()
        if 0 <= row < len(cs):
            self.ui.tabOutput.setCurrentIndex(row)
            edt = self.allTabEditMap.get(key)
            if edt is not None:
                edt.moveCursor(QtGui.QTextCursor.End)
        pass

    def _handleRun(self):
        selects = SshManager.getSelectClients()
        logging.info(f'selects = {selects}')

        if len(selects) == 0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("请选择需要执行的host")
            # msg.setWindowTitle("MessageBox demo")
            # msg.setInformativeText("This is additional information")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
            return

        text = self.ui.edtCmd.toPlainText()
        lines = text.split("\n")

        logging.info(f'do_run text = {text}')
        logging.info(f'do_run.lines = {lines}')

        SshManager.execCmd(lines, self._execCallback)

    def _execCallback(self, client, msg: ResultMsg):
        logging.info(f'_execCallback msg = {msg}')
        self.output_signal.emit(msg)

    def exec_callback_update(self, msg: ResultMsg):
        edt = self.allTabEditMap[msg.key]
        if edt is None:
            return

        if msg.status == logic.model.STATUS_EXEC_BEFORE:
            edt.appendPlainText(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        elif msg.status == logic.model.STATUS_RUN_BEGIN:
            edt.appendPlainText(f"> {msg.msg}")
        elif msg.status == logic.model.STATUS_RUNNING:
            edt.appendPlainText(msg.msg)
        elif msg.status == logic.model.STATUS_RUN_END:
            edt.appendPlainText("")
        elif msg.status == logic.model.STATUS_EXEC_AFTER:
            edt.appendPlainText("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n\n")
        else:
            edt.appendPlainText(msg.msg)

        self._update_status_bar()

    def _update_status_bar(self):
        if SshManager.totalCmdSize == 0:
            self.ui.statusBar.showMessage('')
            return

        c = f'{SshManager.completeClientSize} / {SshManager.totalClientSize}'
        c2 = f'{SshManager.completeCmdSize} / {SshManager.totalCmdSize}'
        self.ui.statusBar.showMessage(f"统计信息: 实例进度 {c}, 命令进度 {c2}")

    def _edtCmdChange(self):
        text = self.ui.edtCmd.toPlainText()
        self.ui.btnRun.setEnabled(len(text) != 0)

    def _handle_refresh(self):
        logging.info('_handle_refresh')
        SshManager.disconnectAll()

        SshManager.connectAll(self._execCallback)

    def _handle_setting(self):
        logging.info('_handle_setting')
        sd = SettingDialog(self)
        sd.setup()
        sd.exec_()

        self.select_all_change()
        self._handle_refresh()
        self.update_hosts_ui(first=True)

    def closeEvent(self, event: PySide2.QtGui.QCloseEvent) -> None:
        logging.info('closeEvent')
        page.exit_app()
