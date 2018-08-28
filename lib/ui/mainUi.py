# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created: Tue Aug 28 10:33:15 2018
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 386)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon64.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.frame_video = QtGui.QHBoxLayout()
        self.frame_video.setSpacing(0)
        self.frame_video.setObjectName(_fromUtf8("frame_video"))
        spacerItem = QtGui.QSpacerItem(320, 0, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.frame_video.addItem(spacerItem)
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Sunken)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.frame_video.addWidget(self.frame)
        self.horizontalLayout_2.addLayout(self.frame_video)
        self.frame_parameters = QtGui.QHBoxLayout()
        self.frame_parameters.setSpacing(0)
        self.frame_parameters.setObjectName(_fromUtf8("frame_parameters"))
        self.horizontalLayout_2.addLayout(self.frame_parameters)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.toolBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCamera = QtGui.QAction(MainWindow)
        self.actionCamera.setCheckable(True)
        self.actionCamera.setChecked(True)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/camera_on_red.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/camera_off.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionCamera.setIcon(icon1)
        self.actionCamera.setObjectName(_fromUtf8("actionCamera"))
        self.actionFile = QtGui.QAction(MainWindow)
        self.actionFile.setCheckable(True)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/play_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/stop_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionFile.setIcon(icon2)
        self.actionFile.setObjectName(_fromUtf8("actionFile"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/save-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.action_Parameters = QtGui.QAction(MainWindow)
        self.action_Parameters.setEnabled(False)
        self.action_Parameters.setObjectName(_fromUtf8("action_Parameters"))
        self.action_Transcode_Video = QtGui.QAction(MainWindow)
        self.action_Transcode_Video.setObjectName(_fromUtf8("action_Transcode_Video"))
        self.actionParameters = QtGui.QAction(MainWindow)
        self.actionParameters.setEnabled(False)
        self.actionParameters.setObjectName(_fromUtf8("actionParameters"))
        self.actionAbout = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/about_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbout.setIcon(icon4)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionRecord = QtGui.QAction(MainWindow)
        self.actionRecord.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/record_on.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/stop_file.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionRecord.setIcon(icon5)
        self.actionRecord.setObjectName(_fromUtf8("actionRecord"))
        self.actionArduino = QtGui.QAction(MainWindow)
        self.actionArduino.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/arduino_off.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionArduino.setIcon(icon6)
        self.actionArduino.setObjectName(_fromUtf8("actionArduino"))
        self.actionLoadConfig = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/load_template.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoadConfig.setIcon(icon7)
        self.actionLoadConfig.setObjectName(_fromUtf8("actionLoadConfig"))
        self.actionSaveConfig = QtGui.QAction(MainWindow)
        self.actionSaveConfig.setIcon(icon3)
        self.actionSaveConfig.setObjectName(_fromUtf8("actionSaveConfig"))
        self.actionRemoveTemplate = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/remove_config.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemoveTemplate.setIcon(icon8)
        self.actionRemoveTemplate.setObjectName(_fromUtf8("actionRemoveTemplate"))
        self.actionSourceProperties = QtGui.QAction(MainWindow)
        self.actionSourceProperties.setObjectName(_fromUtf8("actionSourceProperties"))
        self.actionOnTop = QtGui.QAction(MainWindow)
        self.actionOnTop.setCheckable(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/pin_to_top.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOnTop.setIcon(icon9)
        self.actionOnTop.setObjectName(_fromUtf8("actionOnTop"))
        self.actionGUI_on_off = QtGui.QAction(MainWindow)
        self.actionGUI_on_off.setCheckable(True)
        self.actionGUI_on_off.setChecked(True)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/GUI_on.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/GUI_off.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionGUI_on_off.setIcon(icon10)
        self.actionGUI_on_off.setObjectName(_fromUtf8("actionGUI_on_off"))
        self.actionFPS_test = QtGui.QAction(MainWindow)
        self.actionFPS_test.setCheckable(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/fps_test.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFPS_test.setIcon(icon11)
        self.actionFPS_test.setObjectName(_fromUtf8("actionFPS_test"))
        self.actionSpeed_up = QtGui.QAction(MainWindow)
        self.actionSpeed_up.setCheckable(True)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(_fromUtf8(":/Space_rocket-16-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionSpeed_up.setIcon(icon12)
        self.actionSpeed_up.setObjectName(_fromUtf8("actionSpeed_up"))
        self.actionLogger = QtGui.QAction(MainWindow)
        self.actionLogger.setCheckable(True)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(_fromUtf8(":/logger.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLogger.setIcon(icon13)
        self.actionLogger.setObjectName(_fromUtf8("actionLogger"))
        self.actionGraph = QtGui.QAction(MainWindow)
        self.actionGraph.setCheckable(True)
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(_fromUtf8(":/graph.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionGraph.setIcon(icon14)
        self.actionGraph.setObjectName(_fromUtf8("actionGraph"))
        self.spacer = QtGui.QAction(MainWindow)
        self.spacer.setText(_fromUtf8(""))
        self.spacer.setObjectName(_fromUtf8("spacer"))
        self.actionReset = QtGui.QAction(MainWindow)
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap(_fromUtf8(":/reset.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset.setIcon(icon15)
        self.actionReset.setObjectName(_fromUtf8("actionReset"))
        self.spacer_2 = QtGui.QAction(MainWindow)
        self.spacer_2.setText(_fromUtf8(""))
        self.spacer_2.setObjectName(_fromUtf8("spacer_2"))
        self.toolBar.addAction(self.actionCamera)
        self.toolBar.addAction(self.actionFile)
        self.toolBar.addAction(self.actionRecord)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionGUI_on_off)
        self.toolBar.addAction(self.actionFPS_test)
        self.toolBar.addAction(self.actionSpeed_up)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLoadConfig)
        self.toolBar.addAction(self.actionSaveConfig)
        self.toolBar.addAction(self.actionRemoveTemplate)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLogger)
        self.toolBar.addAction(self.actionGraph)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionReset)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionOnTop)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.spacer)
        self.toolBar.addAction(self.spacer_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Spotter", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionCamera.setText(_translate("MainWindow", "&Camera", None))
        self.actionFile.setText(_translate("MainWindow", "&File", None))
        self.actionSave.setText(_translate("MainWindow", "&Transcode", None))
        self.action_Parameters.setText(_translate("MainWindow", "&Parameters", None))
        self.action_Transcode_Video.setText(_translate("MainWindow", "&Transcode Video", None))
        self.actionParameters.setText(_translate("MainWindow", "Parameters", None))
        self.actionAbout.setText(_translate("MainWindow", "&About", None))
        self.actionRecord.setText(_translate("MainWindow", "Record", None))
        self.actionRecord.setToolTip(_translate("MainWindow", "Record Video", None))
        self.actionArduino.setText(_translate("MainWindow", "Arduino", None))
        self.actionArduino.setToolTip(_translate("MainWindow", "Arduino State", None))
        self.actionLoadConfig.setText(_translate("MainWindow", "Load", None))
        self.actionSaveConfig.setText(_translate("MainWindow", "Save", None))
        self.actionSaveConfig.setToolTip(_translate("MainWindow", "Save current configuration", None))
        self.actionRemoveTemplate.setText(_translate("MainWindow", "Remove all", None))
        self.actionRemoveTemplate.setToolTip(_translate("MainWindow", "Remove all configurations", None))
        self.actionSourceProperties.setText(_translate("MainWindow", "Source Props", None))
        self.actionOnTop.setText(_translate("MainWindow", "Always on Top", None))
        self.actionGUI_on_off.setText(_translate("MainWindow", "GUI on/off", None))
        self.actionFPS_test.setText(_translate("MainWindow", "FPS test", None))
        self.actionFPS_test.setToolTip(_translate("MainWindow", "Outputs a square wave of the framerate on D3", None))
        self.actionSpeed_up.setText(_translate("MainWindow", "Speed up!", None))
        self.actionSpeed_up.setToolTip(_translate("MainWindow", "Increase framerate (the framerate is less stable)", None))
        self.actionLogger.setText(_translate("MainWindow", "Logger", None))
        self.actionGraph.setText(_translate("MainWindow", "Graph view", None))
        self.actionGraph.setToolTip(_translate("MainWindow", "<html><head/><body><p>Output analog outputs in graph view</p></body></html>", None))
        self.actionReset.setText(_translate("MainWindow", "Reset", None))
        self.actionReset.setToolTip(_translate("MainWindow", "Delete position history, and reset filters", None))

import icons_rc
