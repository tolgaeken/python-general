# PyQt5 - Pencere Sınıfının Genişletilmesi

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.setWindowTitle("First App")
        self.setGeometry(200,200,500,500)
        self.setWindowIcon(QIcon("15. PyQt5/Files/icon.png"))
        self.setToolTip("My Tool Tip")
        self.initUI()
    
    def initUI(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız : ")
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız : ")
        self.lbl_surname.move(50,90)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(300,50)
        self.lbl_result.move(50,210)
        

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(120,30)
        self.txt_name.resize(200,32) # Metin kutusunu yeniden boyutlandırır

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(120,90)
        self.txt_surname.resize(200,32)

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(50,150)
        self.btn_save.clicked.connect(self.clicked)
    
    def clicked(self):
        self.lbl_result.setText(f"Butona Tıklandı - Adı-Soyadı : {self.txt_name.text()} {self.txt_surname.text()}")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()
