# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'det.ui'
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

class Ui_Detector(object):
    def setupUi(self, Detector):
        Detector.setObjectName(_fromUtf8("Detector"))
        Detector.resize(433, 323)
        self.detector1Button = QtGui.QPushButton(Detector)
        self.detector1Button.setGeometry(QtCore.QRect(50, 30, 101, 51))
        self.detector1Button.setObjectName(_fromUtf8("detector1Button"))
        self.detector1Button_2 = QtGui.QPushButton(Detector)
        self.detector1Button_2.setGeometry(QtCore.QRect(50, 180, 101, 51))
        self.detector1Button_2.setObjectName(_fromUtf8("detector1Button_2"))
        self.lineEdit = QtGui.QLineEdit(Detector)
        self.lineEdit.setGeometry(QtCore.QRect(210, 29, 211, 51))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Detector)
        self.lineEdit_2.setGeometry(QtCore.QRect(210, 180, 211, 51))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.retranslateUi(Detector)
        QtCore.QObject.connect(self.detector1Button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit.clear)
        QtCore.QObject.connect(self.detector1Button_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.lineEdit_2.clear)
        QtCore.QMetaObject.connectSlotsByName(Detector)

    def retranslateUi(self, Detector):
        Detector.setWindowTitle(_translate("Detector", "Detector", None))
        self.detector1Button.setText(_translate("Detector", "Detector 1", None))
        self.detector1Button_2.setText(_translate("Detector", "Detector 2", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Detector = QtGui.QDialog()
    ui = Ui_Detector()
    ui.setupUi(Detector)
    Detector.show()
    sys.exit(app.exec_())

