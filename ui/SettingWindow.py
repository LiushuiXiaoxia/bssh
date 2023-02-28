# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SettingWindow(object):
    def setupUi(self, SettingWindow):
        if not SettingWindow.objectName():
            SettingWindow.setObjectName(u"SettingWindow")
        SettingWindow.resize(687, 827)
        self.centralwidget = QWidget(SettingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 800))
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(600, 800))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_5.addWidget(self.label_4)

        self.edtHosts = QPlainTextEdit(self.widget)
        self.edtHosts.setObjectName(u"edtHosts")

        self.verticalLayout_5.addWidget(self.edtHosts)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_6.addWidget(self.label)

        self.edtAccount = QLineEdit(self.widget)
        self.edtAccount.setObjectName(u"edtAccount")

        self.verticalLayout_6.addWidget(self.edtAccount)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.edtPassword = QLineEdit(self.widget)
        self.edtPassword.setObjectName(u"edtPassword")
        self.edtPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_6.addWidget(self.edtPassword)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.edtPort = QLineEdit(self.widget)
        self.edtPort.setObjectName(u"edtPort")

        self.verticalLayout_6.addWidget(self.edtPort)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.btnAdd = QPushButton(self.widget)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setEnabled(False)
        self.btnAdd.setCheckable(False)
        self.btnAdd.setAutoDefault(False)
        self.btnAdd.setFlat(False)

        self.verticalLayout_2.addWidget(self.btnAdd)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tvClients = QTableWidget(self.widget)
        if (self.tvClients.columnCount() < 4):
            self.tvClients.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tvClients.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tvClients.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tvClients.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tvClients.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tvClients.setObjectName(u"tvClients")
        self.tvClients.horizontalHeader().setVisible(True)
        self.tvClients.horizontalHeader().setDefaultSectionSize(120)
        self.tvClients.horizontalHeader().setProperty("showSortIndicator", False)
        self.tvClients.verticalHeader().setVisible(False)
        self.tvClients.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout.addWidget(self.tvClients)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btnEdit = QPushButton(self.widget)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setEnabled(False)

        self.verticalLayout.addWidget(self.btnEdit)

        self.btnRemove = QPushButton(self.widget)
        self.btnRemove.setObjectName(u"btnRemove")
        self.btnRemove.setEnabled(False)

        self.verticalLayout.addWidget(self.btnRemove)

        self.btnMoveUp = QPushButton(self.widget)
        self.btnMoveUp.setObjectName(u"btnMoveUp")
        self.btnMoveUp.setEnabled(False)

        self.verticalLayout.addWidget(self.btnMoveUp)

        self.btnMoveDown = QPushButton(self.widget)
        self.btnMoveDown.setObjectName(u"btnMoveDown")
        self.btnMoveDown.setEnabled(False)

        self.verticalLayout.addWidget(self.btnMoveDown)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(2, 2)

        self.verticalLayout_4.addWidget(self.widget)

        SettingWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(SettingWindow)
        self.statusBar.setObjectName(u"statusBar")
        SettingWindow.setStatusBar(self.statusBar)

        self.retranslateUi(SettingWindow)

        self.btnAdd.setDefault(False)


        QMetaObject.connectSlotsByName(SettingWindow)
    # setupUi

    def retranslateUi(self, SettingWindow):
        SettingWindow.setWindowTitle(QCoreApplication.translate("SettingWindow", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("SettingWindow", u"\u4e3b\u673a\u5730\u5740", None))
        self.label.setText(QCoreApplication.translate("SettingWindow", u"\u8d26\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("SettingWindow", u"\u5bc6\u7801", None))
        self.edtPassword.setText("")
        self.label_3.setText(QCoreApplication.translate("SettingWindow", u"\u7aef\u53e3", None))
        self.edtPort.setText("")
        self.edtPort.setPlaceholderText(QCoreApplication.translate("SettingWindow", u"22", None))
        self.btnAdd.setText(QCoreApplication.translate("SettingWindow", u"\u6dfb\u52a0", None))
        ___qtablewidgetitem = self.tvClients.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SettingWindow", u"\u5e8f\u5217", None));
        ___qtablewidgetitem1 = self.tvClients.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SettingWindow", u"\u5730\u5740", None));
        ___qtablewidgetitem2 = self.tvClients.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SettingWindow", u"\u8d26\u53f7", None));
        ___qtablewidgetitem3 = self.tvClients.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SettingWindow", u"\u7aef\u53e3", None));
        self.btnEdit.setText(QCoreApplication.translate("SettingWindow", u"\u7f16\u8f91", None))
        self.btnRemove.setText(QCoreApplication.translate("SettingWindow", u"\u5220\u9664", None))
        self.btnMoveUp.setText(QCoreApplication.translate("SettingWindow", u"\u4e0a\u79fb", None))
        self.btnMoveDown.setText(QCoreApplication.translate("SettingWindow", u"\u4e0b\u79fb", None))
    # retranslateUi

