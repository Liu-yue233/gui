from PyQt5 import QtWidgets, uic
import sys

# from PIL import Image,ImageTk
# import tkinter as tk

class Ui(QtWidgets.QMainWindow):

    # def Open_Img(self):
    #     global img_png
    #     Img = Image.open('diaochan.jpg')
    #     img_png = ImageTk.PhotoImage(Img)
    #
    # def Show_Img(self):
    #     global img_png
    #     label_Img = tk.Label(window,image=img_png)
    #     label_Img.pack()

    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('tt.ui', self)

        self.button1 = self.findChild(QtWidgets.QPushButton,'hellobutton')
        self.button1.clicked.connect(self.printButton1Pressed)

        self.button2 = self.findChild(QtWidgets.QPushButton, 'byebutton')
        self.button2.clicked.connect(self.printButton2Pressed)
        self.show()


    def printButton1Pressed(self):
        print('hello')

    def printButton2Pressed(self):
        print('bye')


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
#
#
# Form, Window = uic.loadUiType("dtk.ui")
#
# app = QApplication([])
# window = Window()
# form = Form()
# form.setupUi(window)
# window.show()
# app.exec_()