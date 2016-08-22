# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'miao.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui
import save

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

class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 500)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 395, 400))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setReadOnly(True)
        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(400, 30, 395, 400))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.textEdit_2.setReadOnly(True)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 10, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOption = QtGui.QMenu(self.menubar)
        self.menuOption.setObjectName(_fromUtf8("menuOption"))
        self.menuExtra = QtGui.QMenu(self.menubar)
        self.menuExtra.setObjectName(_fromUtf8("menuExtra"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.actionRead_Me = QtGui.QAction(MainWindow)
        self.actionRead_Me.setObjectName(_fromUtf8("actionRead_Me"))
        self.menuFile.addAction(self.actionOpen)
        self.menuOption.addAction(self.actionRun)
        self.menuExtra.addAction(self.actionRead_Me)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuExtra.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Button

        self.connect(self.actionOpen, QtCore.SIGNAL('triggered()'), self.openfile)
        self.connect(self.actionRun, QtCore.SIGNAL('triggered()'), self.run)

    def openfile(self):
        file = open('file_in.txt', 'r')
        string = ""
        for eachline in file:
            string += eachline
            print(string)
        self.textEdit.setText(string)
    
    def run(self):
        self.textEdit_2.setText("233")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "File_in", None))
        self.label_2.setText(_translate("MainWindow", "Result", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOption.setTitle(_translate("MainWindow", "Option", None))
        self.menuExtra.setTitle(_translate("MainWindow", "Extra", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionRun.setText(_translate("MainWindow", "Run", None))
        self.actionRead_Me.setText(_translate("MainWindow", "Read_Me", None))

app = QtGui.QApplication(sys.argv)
ui = Ui_MainWindow()
ui.show()
app.exec_()


