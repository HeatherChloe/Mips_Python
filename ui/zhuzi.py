# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'moemoe.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 30, 381, 511))
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(410, 30, 381, 511))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(410, 10, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuOption = QtGui.QMenu(self.menubar)
        self.menuOption.setObjectName(_fromUtf8("menuOption"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen_2 = QtGui.QAction(MainWindow)
        self.actionOpen_2.setObjectName(_fromUtf8("actionOpen_2"))
        self.actionOpen_3 = QtGui.QAction(MainWindow)
        self.actionOpen_3.setObjectName(_fromUtf8("actionOpen_3"))
        self.action_2 = QtGui.QAction(MainWindow)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.actionRun = QtGui.QAction(MainWindow)
        self.actionRun.setObjectName(_fromUtf8("actionRun"))
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionOpen_3)
        self.menuOption.addAction(self.actionRun)
        self.menuAbout.addAction(self.action_2)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "File_In", None))
        self.label_2.setText(_translate("MainWindow", "Result", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuOption.setTitle(_translate("MainWindow", "Option", None))
        self.menuAbout.setTitle(_translate("MainWindow", "About", None))
        self.menu.setTitle(_translate("MainWindow", "Extra", None))
        self.actionOpen.setText(_translate("MainWindow", "new", None))
        self.actionOpen_2.setText(_translate("MainWindow", "open", None))
        self.actionOpen_3.setText(_translate("MainWindow", "open", None))
        self.action_2.setText(_translate("MainWindow", "Read_Me", None))
        self.actionRun.setText(_translate("MainWindow", "run", None))


def main():
    app = QtGui.QApplication(sys.argv)
    main_window = Ui_MainWindow()
    main_window.show()
    app.exec_()

if __name__ == "__main__":
    main()


    
