import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PIL import Image
import numpy as np
from scipy.misc import imresize
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from PIL.ImageQt import ImageQt
import re
import cv2


img = cv2.imread('zsnorlax.png')

class detector1(QWidget):
   def __init__(self, parent = None):
      super(detector1, self).__init__(parent)

      self.showMaximized()
      self.setWindowTitle("Image Detector")
      self.setWindowIcon(QIcon('snorlax.png'))

      #VBOX1
      layout_left_displayInfo = QVBoxLayout()
      layout_left_chooseImage = QHBoxLayout()

      self.chooseLabel = QLabel("Please choose an image to be detected:")
      self.chooseLabel.setAlignment(Qt.AlignCenter)
      layout_left_chooseImage.addWidget(self.chooseLabel)

      self.btn = QPushButton("Choose the image")  #Choose the image button
      self.btn.setLayoutDirection(Qt.RightToLeft)
      self.btn.clicked.connect(self.getfile)
      layout_left_chooseImage.addWidget(self.btn)

      self.le = QLabel("Hello!")  #Display the image
      self.le.setAlignment(Qt.AlignCenter)
      layout_left_displayInfo.addWidget(self.le)

      self.btnExtract = QPushButton("Extract the information of chosen image") #Extract the info of image
      self.btnExtract.clicked.connect(self.getnum) #call def getinfo
      layout_left_displayInfo.addWidget(self.btnExtract)

      self.extractNum = QTextEdit()  # Display the number of chosen image
      layout_left_displayInfo.addWidget(self.extractNum)

      self.btn1 = QPushButton("Process") # All process
      self.btn1.clicked.connect(self.detector2_1)
      self.btn1.clicked.connect(self.detector2_2)
      self.btn1.clicked.connect(self.fill_square)
      self.btn1.clicked.connect(self.detector1)
      self.btn1.clicked.connect(self.detector21)#call def detector
      self.btn1.clicked.connect(self.detector3_combined)
      #self.btn1.clicked.connect(self.detector3_v)
      layout_left_displayInfo.addWidget(self.btn1)

      #VBOX2
      layout_right_grid = QGridLayout()

      self.la1 = QLabel("JPEG Grid Detector")
      layout_right_grid.addWidget(self.la1, 0, 0)

      self.contents = QLabel("Detector21")
      self.contents.setMinimumSize(200, 200)
      layout_right_grid.addWidget(self.contents, 1, 0)

      self.contents2 = QLabel("Detector22")
      self.contents2.setMinimumSize(200, 200)
      layout_right_grid.addWidget(self.contents2, 1, 1)

        #canvas
      #self.figure = plt.figure()
      #self.canvas = FigureCanvas(self.figure)
      #layout_right_grid.addWidget(self.canvas, 1, 2)

      self.ground = QLabel("Ground True")
      layout_right_grid.addWidget(self.ground, 1, 2)

      self.la2 = QLabel("JPEG STH")
      layout_right_grid.addWidget(self.la2, 3, 0)

      self.colorMapDeclare = QLabel("Low Compression                                                                                      High Compression")
      layout_right_grid.addWidget(self.colorMapDeclare, 3, 2)

      self.contents3 = QTextEdit()
      #self.contents3.resize(self.contents3.sizeHint())
      self.contents3.setMinimumSize(200, 50)
      layout_right_grid.addWidget(self.contents3, 4, 0)

      self.contents4 = QTextEdit()
      #self.contents4.resize(self.contents4.sizeHint())
      self.contents.setMinimumSize(200, 50)
      layout_right_grid.addWidget(self.contents4, 4, 1)

      self.content4_3 = QLabel("Color Map")  #Display the image
      self.content4_3.setPixmap(QPixmap("Capture.png"))
      layout_right_grid.addWidget(self.content4_3, 4, 2)

      layout_right_displayImage = QVBoxLayout()

      self.la3 = QLabel("JPEG STH")
      self.la3.setAlignment(Qt.AlignCenter)
      layout_right_displayImage.addWidget(self.la3)

      #self.contents5 = QTextEdit()
      #self.contents5.resize(self.contents5.sizeHint())
      #layout2.addWidget(self.contents5, 6, 0)

      #self.contents6 = QTextEdit()
     # self.contents6.resize(self.contents6.sizeHint())
     # layout2.addWidget(self.contents6, 6, 1)
      self.cb = QLabel("Detector 3")  #Display the image
      self.cb.setAlignment(Qt.AlignCenter)
      layout_right_displayImage.addWidget(self.cb)

      #HBOX
      layout_overall = QHBoxLayout() #overall Horizontal
      #layout_overall.addLayout(layout_left_displayInfo)

      #display left combined vertical layout
      layout_left_combined = QVBoxLayout()
      layout_left_combined.addLayout(layout_left_chooseImage)
      layout_left_combined.addLayout(layout_left_displayInfo)
      layout_overall.addLayout(layout_left_combined)

      #display right combined vertical layout
      layout_right_vertical = QVBoxLayout()
      layout_right_vertical.addLayout(layout_right_grid)
      layout_right_vertical.addLayout(layout_right_displayImage)
      layout_overall.addLayout(layout_right_vertical)
      #layout4.addLayout(layout2)

      self.setLayout(layout_overall)


   def getfile(self):
       self.fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.png)")
       self.le.setPixmap(QPixmap(self.fname))
       return self.fname


   def getnum(self):
       self.findNum = []
       self.regex = re.compile(r'\d+')
       self.findNum = self.regex.findall(str(self.fname))
       self.txt = self.extractNum.setText("The following numbers are Quality Factor, Image Name, Quality Factor, " +
                                          "Cropped Height vale and Cropped Width value: " + str(self.findNum))
       #print self.findNum[3], self.findNum[4]

       return self.txt, self.findNum[3], self.findNum[4]

# Right block functions

   def detector2_1(self):
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
       self.contents.setText(str([q_max, p_max]))

       if [7 - q_max, 7 - p_max] == [int(self.findNum[3]), int(self.findNum[4])]:
        self.contents.setPixmap(QPixmap("g" + str(7 - q_max) + str(7 - p_max) + ".png"))
       else:
        self.contents.setPixmap(QPixmap(str(7 - q_max) + str(7 - p_max) + ".png"))


       #print q_max, p_max, self.findNum[3], self.findNum[4]
       return [q_max, p_max]

   def detector2_2(self):
       im = Image.open(str(self.fname)).convert('L')
       pix = im.load()
       M, N = im.size
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

               a = E.sum(axis=0)
               b = E.sum(axis=1)
               c = np.argmax(a)
               d = np.argmax(b)
       self.contents2.setText(str([c, d]))

       if [7 - c, 7 - d] == [int(self.findNum[3]), int(self.findNum[4])]:
        self.contents2.setPixmap(QPixmap("g" + str(7 - c) + str(7 - d) + ".png"))
       else:
        self.contents2.setPixmap(QPixmap(str(7 - c) + str(7 - d) + ".png"))
       return c, d

   def fill_square(self):

       # Parameters
       jpg_offset_row = int(self.findNum[3])
       jpg_offset_col = int(self.findNum[4])

       self.ground.setPixmap(QPixmap("g"+str(self.findNum[3])+str(self.findNum[4])+".png"))
       #self.ground.setPixmap(QBitmap.fromImage(qimage, flags=Qt.ColorOnly))
       self.ground.show()

       #self.fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Image files (*.jpg *.png)")
       #self.ground.setPixmap(QPixmap(self.fname))


   def detector1(self):
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
       self.contents3.setText(str(k))
       # self.contents3.setStyleSheet("QTextEdit {color:red}")
       # self.contents3.setStyleSheet("QTextEdit { background-color: rgb(0, 255, 0); }");
       norm = k / 1.6
       if 0 <= norm < 0.1:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(255,165,0); }")
       elif 0.1 <= norm < 0.2:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(255,140,0); }")
       elif 0.2 <= norm < 0.3:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(255,69,0); }")
       elif 0.3 <= norm < 0.4:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(255,160,122); }")
       elif 0.4 <= norm < 0.5:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(250,128,114); }")
       elif 0.5 <= norm < 0.6:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(233,150,122); }")
       elif 0.6 <= norm < 0.7:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(240,128,128); }")
       elif 0.7 <= norm < 0.8:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(205,92,92); }")
       elif 0.8 <= norm < 0.9:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(255,127,80); }")
       elif 0.9 <= norm < 1.0:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(255,99,71); }")
       elif 1.0 <= norm < 1.1:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(255,0,0); }")
       elif 1.1 <= norm < 1.2:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(220,20,60); }")
       elif 1.2 <= norm < 1.3:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(178,34,34); }")
       elif 1.3 <= norm < 1.4:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(165,42,42); }")
       elif 1.4 <= norm < 1.5:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(139,0,0); }")
       else:
           self.contents3.setStyleSheet("QTextEdit { background-color: rgb(128,0,0); }")

       return k

   def detector21(self):
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

               a = E.sum(axis=0)
               b = E.sum(axis=1)
               c = np.argmax(a)
               d = np.argmax(b)
       p_max = d
       q_max = c
       m = d - 4
       n = c - 4
       print [p_max, q_max], [m, n]
       if p_max >= 4 and q_max >= 4:
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
       #print h3
       k = sum(h3)

       self.contents4.setText(str(k))
       norm = k / 1.6
       if 0 <= norm < 0.1:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(255,165,0); }")
       elif 0.1 <= norm < 0.2:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(255,140,0); }")
       elif 0.2 <= norm < 0.3:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(255,69,0); }")
       elif 0.3 <= norm < 0.4:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(255,160,122); }")
       elif 0.4 <= norm < 0.5:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(250,128,114); }")
       elif 0.5 <= norm < 0.6:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(233,150,122); }")
       elif 0.6 <= norm < 0.7:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(240,128,128); }")
       elif 0.7 <= norm < 0.8:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(205,92,92); }")
       elif 0.8 <= norm < 0.9:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(255,127,80); }")
       elif 0.9 <= norm < 1.0:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(255,99,71); }")
       elif 1.0 <= norm < 1.1:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(255,0,0); }")
       elif 1.1 <= norm < 1.2:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(220,20,60); }")
       elif 1.2 <= norm < 1.3:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(178,34,34); }")
       elif 1.3 <= norm < 1.4:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(165,42,42); }")
       elif 1.4 <= norm < 1.5:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(139,0,0); }")
       else:
           self.contents4.setStyleSheet("QTextEdit { background-color: rgb(128,0,0); }")

       return [k, [n, m], [p_max, q_max]]


   def detector3_combined(self):
       im = Image.open(str(self.fname)).convert('L')
       pix = np.array(im).astype(np.float)
       r, c = pix.shape

       if r < c:
           # rotate the image
           pix = np.rot90(pix)
           r, c = pix.shape

       arr_h = np.zeros((31, 32))
       arr_v = np.zeros((32, 31))
       sum_h = np.zeros((c / 32, r / 32))
       sum_v = np.zeros((c / 32, r / 32))

       if r % 32 == 0 and c & 32 == 0:
           r_index = r / 32
           c_index = c / 32
       else:
           r_index = r / 32 - 1
           c_index = c / 32 - 1

           # horizontal
           for row in xrange(0, r_index):
               for col in xrange(0, c_index):
                   for j in xrange(32):
                       for i in xrange(31):
                           h1 = pix[row * 32 + i + 1, col * 32 + j]
                           h2 = pix[row * 32 + i, col * 32 + j]
                           h = h1 - h2
                           arr_h[i][j] = h
                   arr_h = np.abs(arr_h)
                   # print arr_h
                   fft = np.abs(np.fft.fft2(arr_h, [32, 32]))  # FFT of horizontal gradient
                   # plt.imshow(fft)
                   # plt.show()
                   if sum(fft[1:16, 0]) == 0:
                       sum1 = 0
                   else:
                       sum1 = (fft[4, 0] + fft[8, 0] + fft[12, 0]) / sum(fft[1:16, 0])

                   sum_h[col][row] = sum1
           myarray = np.asarray(sum_h)

           # vertical
           for col in xrange(0, c_index):
               for row in xrange(0, r_index):
                   for i in xrange(32):
                       for j in xrange(31):
                           v1 = pix[row * 32 + i, col * 32 + j + 1]
                           v2 = pix[row * 32 + i, col * 32 + j]
                           v = v1 - v2
                           arr_v[i][j] = v

                   arr_v = np.abs(arr_v)
                   fft2 = np.abs(np.fft.fft2(arr_v, [32, 32]))  # FFT of vertical gradient
                   if sum(fft2[0, 1:16]) == 0:
                       sum2 = 0
                   else:
                       sum2 = (fft2[0, 4] + fft2[0, 8] + fft2[0, 12]) / sum(fft2[0, 1:16])

                   sum_v[col][row] = sum2
           myarray2 = np.asarray(sum_v)
           combined = (myarray + myarray2)/2.0
           combined = combined[0:-1, 0:-1].T
           g = np.asarray(dtype=np.dtype('float'), a=combined)
           g = imresize(g, (int(pix.shape[0]/1.1), int(pix.shape[1]/1.1)), interp='nearest')

           pix2 = np.array(im).astype(np.float)
           m, n = pix2.shape
           print m,n
           if m < n:
                g = np.rot90(g)
           new_image = Image.fromarray(g)
           qimage = ImageQt(new_image)

           self.cb.setPixmap(QPixmap.fromImage(qimage))
           self.cb.show()
           return g

def main():
   app = QApplication(sys.argv)
   ex = detector1()
   ex.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
