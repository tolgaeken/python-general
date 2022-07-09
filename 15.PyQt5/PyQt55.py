# PyQt5 - Layout
import sys
from turtle import color
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from PyQt5.QtGui import QPalette,QColor

class Color(QWidget):
    def __init__(self,color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True) # Arka plan rengini değiştirir
        

        palette = self.palette()
        palette.setColor(QPalette.Window,QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(100,100,500,500)

        hlayout1 = QtWidgets.QHBoxLayout() # Layoutlar ile nesneler için grup oluşturulur
        hlayout1.addWidget(Color("red")) # Layout lara obje ekler
        hlayout1.addWidget(Color("blue"))
        hlayout1.addWidget(Color("green"))
        # hlayout1.setContentsMargins(30,20,0,30) # Margin ile boşluk ayarlaması yapılır
        hlayout1.setSpacing(50) # Objeler arasındaki boşluğu belirler

        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addWidget(Color("red"))
        hlayout2.addWidget(Color("green"))
        hlayout2.setSpacing(20)

        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        # layout = QtWidgets.QGridLayout()
        # layout.addWidget(Color("red"),0,0) # İlk paramtre satır, ikinci parametre sütun numarasını belirtir
        # layout.addWidget(Color("blue"),1,1)
        # layout.addWidget(Color("green"),0,2)
        # layout.addWidget(Color("yellow"),3,1)

        widget= QWidget()
        widget.setLayout(vlayout)
        self.setCentralWidget(widget)

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()