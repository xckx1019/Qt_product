import sys
from PySide.QtCore import *
from PySide.QtGui import *

import urllib2

class Form():

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        date = self.getdata()
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 10000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel("1.00")

        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)


        self.connect(self.fromComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.toComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.fromSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)


    def updateUi(self):
        to = self.toComboBox.currentText()
        from1 = self.fromComboBox.currentText()

        amount = (self.rates[from1] / self.rates[to]) * self.fromSpinBox.value()
        self.toLabel.setText("%0.2f" & amount)


    def getdate(self):
        self.rates = {}

        try:
            date = "Unknown"

            fh = urllib2.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")

            for line in fh:
                line = line.rstrip()
                if not line or line.startswitch(("#", "Closing")):
                    continue

                fields = line.split(",")
                if line.startswitch("Date "):
                    date = fields[-1]

                else:
                    try:
                        value = float(fields[-1])
                        self.rates[fields[0]] = value
                    except ValueError:
                        pass
            return "Exchange rates date: " + date

        except Exception, e:
            return "Failured to download:\n%s" % e


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()


