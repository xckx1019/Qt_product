import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
import urllib2

class detector1(QWidget):
   def __init__(self, parent = None):
      super(detector1, self).__init__(parent)
      self.setWindowTitle("Image Detector")
      self.setWindowIcon(QIcon('snorlax.png'))

      layout = QVBoxLayout()

      self.btn = QPushButton("Choose the image")
      self.btn.clicked.connect(self.getfile)
      layout.addWidget(self.btn)

      self.le = QLabel("Hello!")
      layout.addWidget(self.le)

      self.btn1 = QPushButton("Detect the chosen image with Detector 1")
      self.btn1.clicked.connect(self.detector)
      layout.addWidget(self.btn1)

      self.btn2 =QPushButton("Detect the chosen image with Detector 2")
      self.btn2.clicked.connect(self.detector2)
      layout.addWidget(self.btn2)

      self.btn3 =QPushButton("Detect the chosen image with Detector 2+1")
      self.btn3.clicked.connect(self.detector3)
      layout.addWidget(self.btn3)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.setLayout(layout)


   def getfile(self):
       self.fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.png)")
       self.le.setPixmap(QPixmap(self.fname))
       return self.fname


   def detector(self):
       im = Image.open(str(self.fname)).convert('L')
       pix = im.load()
       M, N = im.size
       arr = np.zeros((M / 8 - 1, N / 8 - 1))
       arr2 = np.zeros((M / 8 - 1, N / 8 - 1))

       for i in range(0, M / 8 - 1):
           for j in range(0, N / 8 - 1):
               A = pix[i * 8 + 3, j * 8 + 3]
               B = pix[i * 8 + 4, j * 8 + 3]
               C = pix[i * 8 + 3, j * 8 + 4]
               D = pix[i * 8 + 4, j * 8 + 4]

               E = pix[i * 8 + 7, j * 8 + 7]
               F = pix[i * 8 + 8, j * 8 + 7]
               G = pix[i * 8 + 7, j * 8 + 8]
               H = pix[i * 8 + 8, j * 8 + 8]

               Z = abs(A - B - C + D)
               Z2 = abs(E - F - G + H)
               arr[i][j] = Z
               arr2[i][j] = Z2


       h1, binEdges = np.histogram(arr, bins=np.arange(0, 256), normed=True)
       bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])

       h2, binEdges = np.histogram(arr2, bins=np.arange(0, 256), normed=True)
       bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])

       h3 = abs(h1 - h2)
       k = sum(h3)
       self.contents.setText("The K value is: " + str(k))
       return k


   def detector2(self):
       im = Image.open(str(self.fname)).convert('L')
       pix = im.load()
       M, N = im.size

       p_max = 0
       q_max = 0
       E_max = 0
       E = np.zeros((8, 8))

       for p in range(0, 8):
           for q in range(0, 8):
               for i in range(0, M / 8 - 1):
                   for j in range(0, N / 8 - 1):
                       A = pix[i * 8 + p, j * 8 + q]
                       B = pix[i * 8 + p + 1, j * 8 + q]
                       C = pix[i * 8 + p, j * 8 + q + 1]
                       D = pix[i * 8 + p + 1, j * 8 + q + 1]

                       Z = abs(A - B - C + D)
                       E[p, q] = E[p, q] + Z

               if E[p, q] >= E_max:
                   E_max = E[p, q]
                   q_max = q
                   p_max = p
       self.contents.setText("The Q_max and P_max value are: " + str([7 - q_max, 7 - p_max]))

       return [q_max, p_max]

   def detector3(self):
       im = Image.open(str(self.fname)).convert('L')
       pix = im.load()
       M, N = im.size
       arr = np.zeros((M / 8 - 1, N / 8 - 1))
       arr2 = np.zeros((M / 8 - 1, N / 8 - 1))
       p_max = 0
       q_max = 0
       E_max = 0
       E = np.zeros((8, 8))

       for p in range(0, 8):
           for q in range(0, 8):
               for i in range(0, M / 8 - 1):
                   for j in range(0, N / 8 - 1):
                       A = pix[i * 8 + p, j * 8 + q]
                       B = pix[i * 8 + p + 1, j * 8 + q]
                       C = pix[i * 8 + p, j * 8 + q + 1]
                       D = pix[i * 8 + p + 1, j * 8 + q + 1]

                       Z = abs(A - B - C + D)
                       E[p, q] = E[p, q] + Z

               if E[p, q] >= E_max:
                   E_max = E[p, q]
                   q_max = q
                   p_max = p

       m = p_max - 4
       n = q_max - 4
       if (p_max and q_max) >= 4:
           block = 0
       else:
           block = 1
       for i in range(block, M / 8 - 1):
           for j in range(block, N / 8 - 1):
               A = pix[i * 8 + m, j * 8 + n]
               B = pix[i * 8 + m + 1, j * 8 + n]
               C = pix[i * 8 + m, j * 8 + n + 1]
               D = pix[i * 8 + m + 1, j * 8 + n + 1]

               E = pix[i * 8 + p_max, j * 8 + q_max]
               F = pix[i * 8 + p_max + 1, j * 8 + q_max]
               G = pix[i * 8 + p_max, j * 8 + q_max + 1]
               H = pix[i * 8 + p_max + 1, j * 8 + q_max + 1]

               Z = abs(A - B - C + D)
               Z2 = abs(E - F - G + H)
               arr[i][j] = Z
               arr2[i][j] = Z2

       h1, binEdges = np.histogram(arr, bins=np.arange(0, 256), normed=True)
       bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])

       h2, binEdges = np.histogram(arr2, bins=np.arange(0, 256), normed=True)
       bincenters = 0.5 * (binEdges[1:] + binEdges[:-1])

       h3 = abs(h1 - h2)
       k = sum(h3)
       self.contents.setText("The K value, M and N value and P_max and Q_max value are: " + str([k, [m, n], [7 - q_max, 7 - p_max]]))
       return [k, [m, n], [p_max, q_max]]


def main():
   app = QApplication(sys.argv)
   ex = detector1()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()