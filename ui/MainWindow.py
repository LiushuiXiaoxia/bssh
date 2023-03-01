# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1300, 900)
        MainWindow.setMinimumSize(QSize(1300, 900))
        self.actionSetting = QAction(MainWindow)
        self.actionSetting.setObjectName(u"actionSetting")
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tvHosts = QTableWidget(self.centralwidget)
        if (self.tvHosts.columnCount() < 3):
            self.tvHosts.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tvHosts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tvHosts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tvHosts.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tvHosts.setObjectName(u"tvHosts")
        self.tvHosts.setMinimumSize(QSize(300, 0))
        self.tvHosts.horizontalHeader().setCascadingSectionResizes(False)
        self.tvHosts.horizontalHeader().setMinimumSectionSize(50)
        self.tvHosts.horizontalHeader().setDefaultSectionSize(80)
        self.tvHosts.verticalHeader().setVisible(True)

        self.verticalLayout_2.addWidget(self.tvHosts)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btnSetting = QPushButton(self.centralwidget)
        self.btnSetting.setObjectName(u"btnSetting")

        self.horizontalLayout_2.addWidget(self.btnSetting)

        self.btnRefresh = QPushButton(self.centralwidget)
        self.btnRefresh.setObjectName(u"btnRefresh")

        self.horizontalLayout_2.addWidget(self.btnRefresh)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.cbSelectAll = QCheckBox(self.centralwidget)
        self.cbSelectAll.setObjectName(u"cbSelectAll")

        self.horizontalLayout_2.addWidget(self.cbSelectAll)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabOutput = QTabWidget(self.centralwidget)
        self.tabOutput.setObjectName(u"tabOutput")
        self.tabOutput.setTabPosition(QTabWidget.North)
        self.tabOutput.setTabShape(QTabWidget.Rounded)
        self.tabOutput.setUsesScrollButtons(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabOutput.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabOutput.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabOutput)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.edtCmd = QTextEdit(self.centralwidget)
        self.edtCmd.setObjectName(u"edtCmd")

        self.verticalLayout.addWidget(self.edtCmd)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnClean = QPushButton(self.centralwidget)
        self.btnClean.setObjectName(u"btnClean")

        self.horizontalLayout.addWidget(self.btnClean)

        self.btnRun = QPushButton(self.centralwidget)
        self.btnRun.setObjectName(u"btnRun")

        self.horizontalLayout.addWidget(self.btnRun)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 5)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(2, 3)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1300, 24))
        self.menubar.setNativeMenuBar(True)
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionSetting)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        self.tabOutput.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSetting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.actionSetting.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#if QT_CONFIG(tooltip)
        self.actionClose.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
#endif // QT_CONFIG(tooltip)
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#if QT_CONFIG(tooltip)
        self.actionAbout.setToolTip(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
#endif // QT_CONFIG(tooltip)
        ___qtablewidgetitem = self.tvHosts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u5730\u5740", None));
        ___qtablewidgetitem1 = self.tvHosts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u72b6\u6001", None));
        ___qtablewidgetitem2 = self.tvHosts.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9", None));
        self.btnSetting.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.btnRefresh.setText(QCoreApplication.translate("MainWindow", u"\u5237\u65b0", None))
        self.cbSelectAll.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
        self.tabOutput.setTabText(self.tabOutput.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabOutput.setTabText(self.tabOutput.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Page", None))
        self.edtCmd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u547d\u4ee4", None))
        self.btnClean.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u5c4f", None))
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"\u6267\u884c", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
    # retranslateUi

