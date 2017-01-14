import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PyQt4 import *

__appname__ = "Image Detector"

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setGeometry(50, 50, 500, 300)
        self.setWindowTitle("Image Detector")
        self.setWindowIcon(QIcon('snorlax.png'))

        openButton = QPushButton("Open")

        self.connect(openButton, SIGNAL("clicked()"), self.open)

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        self.setLayout(layout)

    def open(self):
        dir = "."

        fileObj = QFileDialog.getOpenFileName(self, __appname__ + "Open File Dialog", dir=dir,
                                              filter="Text files (*.txt)")
        print fileObj
        print type(fileObj)

        fileName = fileObj[0]

        file = open(fileName, "r")
        read = file.read()
        file.close()
        print read






app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()