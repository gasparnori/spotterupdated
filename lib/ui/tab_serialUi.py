# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tab_serialUi.ui'
#
# Created: Wed Aug 22 12:47:03 2018
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_tab_serial(object):
    def setupUi(self, tab_serial):
        tab_serial.setObjectName(_fromUtf8("tab_serial"))
        tab_serial.resize(245, 449)
        self.gridLayout = QtGui.QGridLayout(tab_serial)
        self.gridLayout.setMargin(0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setSpacing(1)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.toolBox = QtGui.QToolBox(tab_serial)
        self.toolBox.setFrameShape(QtGui.QFrame.NoFrame)
        self.toolBox.setFrameShadow(QtGui.QFrame.Plain)
        self.toolBox.setLineWidth(0)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page_serial_connection = QtGui.QWidget()
        self.page_serial_connection.setGeometry(QtCore.QRect(0, 0, 243, 426))
        self.page_serial_connection.setObjectName(_fromUtf8("page_serial_connection"))
        self.gridLayout_6 = QtGui.QGridLayout(self.page_serial_connection)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.board_widget = QtGui.QWidget(self.page_serial_connection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.board_widget.sizePolicy().hasHeightForWidth())
        self.board_widget.setSizePolicy(sizePolicy)
        self.board_widget.setObjectName(_fromUtf8("board_widget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.board_widget)
        self.gridLayout_5.setMargin(0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label = QtGui.QLabel(self.board_widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(124, 250))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/ArduinoDue.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_5.addWidget(self.label, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_4.addWidget(self.board_widget, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_4, 6, 1, 1, 3)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.combo_serialports = QtGui.QComboBox(self.page_serial_connection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_serialports.sizePolicy().hasHeightForWidth())
        self.combo_serialports.setSizePolicy(sizePolicy)
        self.combo_serialports.setEditable(True)
        self.combo_serialports.setInsertPolicy(QtGui.QComboBox.InsertAtTop)
        self.combo_serialports.setDuplicatesEnabled(False)
        self.combo_serialports.setObjectName(_fromUtf8("combo_serialports"))
        self.verticalLayout.addWidget(self.combo_serialports)
        self.btn_serial_connect = QtGui.QPushButton(self.page_serial_connection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_serial_connect.sizePolicy().hasHeightForWidth())
        self.btn_serial_connect.setSizePolicy(sizePolicy)
        self.btn_serial_connect.setCheckable(False)
        self.btn_serial_connect.setObjectName(_fromUtf8("btn_serial_connect"))
        self.verticalLayout.addWidget(self.btn_serial_connect)
        self.gridLayout_3.addLayout(self.verticalLayout, 3, 3, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lbl_serial_port = QtGui.QLabel(self.page_serial_connection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_serial_port.sizePolicy().hasHeightForWidth())
        self.lbl_serial_port.setSizePolicy(sizePolicy)
        self.lbl_serial_port.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_serial_port.setObjectName(_fromUtf8("lbl_serial_port"))
        self.verticalLayout_2.addWidget(self.lbl_serial_port)
        self.btn_serial_refresh = QtGui.QPushButton(self.page_serial_connection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_serial_refresh.sizePolicy().hasHeightForWidth())
        self.btn_serial_refresh.setSizePolicy(sizePolicy)
        self.btn_serial_refresh.setObjectName(_fromUtf8("btn_serial_refresh"))
        self.verticalLayout_2.addWidget(self.btn_serial_refresh)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 3, 1, 1, 1)
        self.lbl_tx = QtGui.QLabel(self.page_serial_connection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_tx.sizePolicy().hasHeightForWidth())
        self.lbl_tx.setSizePolicy(sizePolicy)
        self.lbl_tx.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_tx.setObjectName(_fromUtf8("lbl_tx"))
        self.gridLayout_3.addWidget(self.lbl_tx, 4, 1, 1, 1)
        self.lbl_bytes_received = QtGui.QLabel(self.page_serial_connection)
        self.lbl_bytes_received.setText(_fromUtf8(""))
        self.lbl_bytes_received.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_bytes_received.setObjectName(_fromUtf8("lbl_bytes_received"))
        self.gridLayout_3.addWidget(self.lbl_bytes_received, 5, 3, 1, 1)
        self.lbl_rx = QtGui.QLabel(self.page_serial_connection)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_rx.sizePolicy().hasHeightForWidth())
        self.lbl_rx.setSizePolicy(sizePolicy)
        self.lbl_rx.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_rx.setObjectName(_fromUtf8("lbl_rx"))
        self.gridLayout_3.addWidget(self.lbl_rx, 5, 1, 1, 1)
        self.lbl_bytes_sent = QtGui.QLabel(self.page_serial_connection)
        self.lbl_bytes_sent.setText(_fromUtf8(""))
        self.lbl_bytes_sent.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_bytes_sent.setObjectName(_fromUtf8("lbl_bytes_sent"))
        self.gridLayout_3.addWidget(self.lbl_bytes_sent, 4, 3, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_3, 2, 1, 1, 1)
        self.toolBox.addItem(self.page_serial_connection, _fromUtf8(""))
        self.gridLayout_2.addWidget(self.toolBox, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.retranslateUi(tab_serial)
        self.toolBox.setCurrentIndex(0)
        self.toolBox.layout().setSpacing(0)
        QtCore.QMetaObject.connectSlotsByName(tab_serial)

    def retranslateUi(self, tab_serial):
        tab_serial.setWindowTitle(_translate("tab_serial", "Form", None))
        self.btn_serial_connect.setText(_translate("tab_serial", "Connect", None))
        self.lbl_serial_port.setText(_translate("tab_serial", "Available Serial Ports:", None))
        self.btn_serial_refresh.setText(_translate("tab_serial", "Refresh", None))
        self.lbl_tx.setText(_translate("tab_serial", "sent:", None))
        self.lbl_rx.setText(_translate("tab_serial", "received:", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_serial_connection), _translate("tab_serial", "Connection", None))

import images_rc
