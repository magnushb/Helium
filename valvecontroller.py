# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Valve_control.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import PyDAQmx
from PyDAQmx import Task
import numpy as np

class Ui_MainWindow(object):
    def setupUi(self, MainWindow): 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(316, 249)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 221, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 150, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        #icon = QtGui.QIcon()
        #icon.addPixmap(QtGui.QPixmap(":/icons/grid.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        #self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        #self.radioButton.setGeometry(QtCore.QRect(190, 90, 82, 17))
        #self.radioButton.setText("")
        #self.radioButton.setObjectName("radioButton")
        #self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        #self.radioButton_2.setGeometry(QtCore.QRect(190, 150, 82, 17))
        #self.radioButton_2.setText("")
        #self.radioButton_2.setObjectName("radioButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 316, 21))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionInformation = QtWidgets.QAction(MainWindow)
        self.actionInformation.setObjectName("actionInformation")
        self.menuAbout.addAction(self.actionInformation)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">BALTAZAR </span><span style=\" font-size:12pt; font-weight:600;\">Beamshutter</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Open"))
        self.pushButton_2.setText(_translate("MainWindow", "Close"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionInformation.setText(_translate("MainWindow", "Information"))
        self.pushButton.clicked.connect(self.open_valve)
        self.pushButton_2.clicked.connect(self.close_valve)

    def open_valve(self,MainWindow):
        data_on = np.array([0,1], dtype=np.uint8)

        task = Task()
        task.CreateDOChan("/Dev1/port0/line0:1","",PyDAQmx.DAQmx_Val_ChanForAllLines)
        task.StartTask()
        task.WriteDigitalLines(1,1,10.0,PyDAQmx.DAQmx_Val_GroupByChannel,data_on,None,None)
        task.StopTask()

    def close_valve(self,MainWindow):
        data_off = np.array([0,0], dtype=np.uint8)

        task = Task()
        task.CreateDOChan("/Dev1/port0/line0:1","",PyDAQmx.DAQmx_Val_ChanForAllLines)
        task.StartTask()
        task.WriteDigitalLines(1,1,10.0,PyDAQmx.DAQmx_Val_GroupByChannel,data_off,None,None)
        task.StopTask()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

