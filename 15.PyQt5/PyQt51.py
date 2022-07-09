# PyQt5 - Giriş

# # PyQt5 Kütüphanesinin yüklenmesi gerekir
# # Aşağıdaki kod ile otomatik Yüklenir
# import os
# os.system('cmd /c "pip install PyQt5"')
# os.system('cmd /c "pip install QyQt5-tools"') # Hata verirse aşağıdaki kod yüklenebilir
# os.system('cmd /c "pip install PyQt5Designer"')

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QToolTip
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow() # Pencere oluşturur
    win.setWindowTitle("First App") # Uygulamanın başlığıını belirtir
    win.setGeometry(200,200,500,500) # İlk 2 parametre açılacağı konumunu (x,y), son 2 parametre pencerenin büyüklüğünü belirtir
    win.setWindowIcon(QIcon("15. PyQt5/Files/icon.png")) # Uygulamanın logosunu belirtir
    win.setToolTip("My Tool Tip") # Uygulama üzerinde mouse ile üzerine gelindiğinde çıkan açıklamayı belirtir

    lbl_name = QtWidgets.QLabel(win) # Yani bir label oluşturur
    lbl_name.setText("Adınız : ") # Labelda yazacak yazıyı belirtir
    lbl_name.move(50,30) # Label'ın pencere üzerindeki konumunu belirtir

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadınız : ")
    lbl_surname.move(50,90)

    txt_name = QtWidgets.QLineEdit(win) # Yeni bir textbox oluşturur
    txt_name.move(120,30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(120,90)

    def clicked(self): # Aşağıda belirtilen butona tıklandığında yapılması gereken işlemi belirtir
        print(f"Butona Tıklandı - Adı-Soyadı : {txt_name.text()} {txt_surname.text()}")

    btn_save = QtWidgets.QPushButton(win) # Yeni bir buton oluşturur
    btn_save.setText("Kaydet")
    btn_save.move(50,150)
    btn_save.clicked.connect(clicked) # Butona tıklandığında hangi fonksiyona gidilmesi gerektiğini belirtir

    win.show() # Hazırlanan pencereyi gösterir
    sys.exit(app.exec_())

window()
