# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/app-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.archButton = QtGui.QPushButton(Dialog)
        self.archButton.setGeometry(QtCore.QRect(14, 70, 111, 61))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/arch-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.archButton.setIcon(icon1)
        self.archButton.setIconSize(QtCore.QSize(32, 32))
        self.archButton.setObjectName(_fromUtf8("archButton"))
        self.fedoraButton = QtGui.QPushButton(Dialog)
        self.fedoraButton.setGeometry(QtCore.QRect(134, 70, 111, 61))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/fedora-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fedoraButton.setIcon(icon2)
        self.fedoraButton.setIconSize(QtCore.QSize(32, 32))
        self.fedoraButton.setObjectName(_fromUtf8("fedoraButton"))
        self.windowsButton = QtGui.QPushButton(Dialog)
        self.windowsButton.setGeometry(QtCore.QRect(254, 70, 111, 61))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/windows-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.windowsButton.setIcon(icon3)
        self.windowsButton.setIconSize(QtCore.QSize(32, 32))
        self.windowsButton.setObjectName(_fromUtf8("windowsButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Pick an OS", None))
        self.archButton.setText(_translate("Dialog", "Load Arch", None))
        self.fedoraButton.setText(_translate("Dialog", "Load Fedora", None))
        self.windowsButton.setText(_translate("Dialog", "Load Windows", None))

import icons_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

