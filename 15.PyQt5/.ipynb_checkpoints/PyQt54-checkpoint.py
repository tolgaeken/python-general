# PyQt5 - QtDesigner Kullanımı

# Qt Designer üzerinde yapılan ui dosyasını py dosyasına dönüştürmek gerekir
# Aşağıdaki kod ile otomatik yapılır
from os import system
system('cmd /c "pyuic5 15.PyQt5/PyQt54Design.ui -o 15.PyQt5/PyQt54Design.py"')

import sys
from PyQt5 import QtWidgets
from PyQt54Design import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnTopla.clicked.connect(self.hesapla)
        self.ui.btnCikar.clicked.connect(self.hesapla)
        self.ui.btnCarp.clicked.connect(self.hesapla)
        self.ui.btnBol.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender()
        try:
            sayi1 = int(self.ui.txtSayi1.text())
            sayi2 = int(self.ui.txtSayi2.text())         
        except ValueError:
            self.ui.lbl_sonuc.setText("Geçersiz İşlem")
            return

        match sender.text():
            case "Toplama":
                self.ui.lbl_sonuc.setText(f"Sonuç {str(sayi1+sayi2)}")

            case "Çıkarma":
                self.ui.lbl_sonuc.setText(f"Sonuç {str(sayi1-sayi2)}")

            case "Çarpma":
                self.ui.lbl_sonuc.setText(f"Sonuç {str(sayi1*sayi2)}")

            case "Bölme":
                try:
                    self.ui.lbl_sonuc.setText(f"Sonuç {str(round(sayi1/sayi2,2))}")
                except ZeroDivisionError:
                    self.ui.lbl_sonuc.setText("Sayı 0'a Bölünemez")

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()



