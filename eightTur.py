import sys
from PySide.QtCore import *
from PySide.QtGui import *

__appname__ = "Eight Video"

class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        openButton = QPushButton("Open")
        saveButton = QPushButton("Save")
        dirButton = QPushButton("Other")
        closeButton = QPushButton("Close")

        self.connect(openButton, SIGNAL("clicked()"), self.open)
        self.connect(saveButton, SIGNAL("clicked()"), self.save)

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)
        layout.addWidget(closeButton)
        self.setLayout(layout)

    def open(self):

        dir = "."

        fileObj = QFileDialog.getOpenFileName(self, __appname__+"Open File Dialog", dir=dir, filter="Text files (*.txt)")
        print fileObj
        print type(fileObj)

        fileName = fileObj[0]

        file = open(fileName, "r")
        read = file.read()
        file.close()
        print read

    def save(self):
        dir ="."

        fileObj = QFileDialog.getSaveFileName(self, __appname__, dir=dir, filter="Text Files(*.txt)")

        print fileObj
        print type(fileObj)

        content ="Hello World!!"

        fileNmae = fileObj[0]
        open(fileNmae, mode="w").write(content)


app = QApplication(sys.argv)
form = Program()
form.show()
app.exec_()