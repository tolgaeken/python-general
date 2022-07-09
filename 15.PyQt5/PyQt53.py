# PyQt5 - Uygulama - Hesap Makinesi
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm,self).__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(300,300,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText("Sayı 1:")
        self.lbl_sayi1.move(50,30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150,30)
        self.txt_sayi1.resize(200,32)
        
        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText("Sayı 2:")
        self.lbl_sayi2.move(50,80)

        self.lbl_sonuc = QtWidgets.QLabel(self)
        self.lbl_sonuc.move(150,290)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150,80)
        self.txt_sayi2.resize(200,32)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText("Topla")
        self.btn_topla.move(150,130)
        self.btn_topla.clicked.connect(self.hesapla)

        self.btn_cikar = QtWidgets.QPushButton(self)
        self.btn_cikar.setText("Çıkar")
        self.btn_cikar.move(150,170)
        self.btn_cikar.clicked.connect(self.hesapla)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText("Çarp")
        self.btn_carp.move(150,210)
        self.btn_carp.clicked.connect(self.hesapla)

        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText("Böl")
        self.btn_bol.move(150,250)
        self.btn_bol.clicked.connect(self.hesapla)

    def hesapla(self):
        sender = self.sender() # Sender ile gelen obje alınır
        try:
            sayi1 = int(self.txt_sayi1.text())
            sayi2 = int(self.txt_sayi2.text())         
        except ValueError:
            self.lbl_sonuc.setText("Geçerisz İşlem")
            return

        match sender.text():
            case "Topla":
                self.lbl_sonuc.setText(f"Sonuç {str(sayi1+sayi2)}")

            case "Çıkar":
                self.lbl_sonuc.setText(f"Sonuç {str(sayi1-sayi2)}")

            case "Çarp":
                self.lbl_sonuc.setText(f"Sonuç {str(sayi1*sayi2)}")

            case "Böl":
                try:
                    self.lbl_sonuc.setText(f"Sonuç {str(round(sayi1/sayi2,2))}")
                except ZeroDivisionError:
                    self.lbl_sonuc.setText("Sayı 0'a Bölünemez")

    # def toplama(self):
    #     try:
    #         result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
    #         self.lbl_sonuc.setText(f"Sonuç {str(result)}")
    #     except ValueError:
    #         self.lbl_sonuc.setText("Geçersiz İşlem")

    # def cikarma(self):
    #     try:
    #         result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
    #         self.lbl_sonuc.setText(f"Sonuç {str(result)}")
    #     except ValueError:
    #         self.lbl_sonuc.setText("Geçersiz İşlem")

    # def carpma(self):
    #     try:
    #         result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
    #         self.lbl_sonuc.setText(f"Sonuç {str(result)}")
    #     except ValueError:
    #         self.lbl_sonuc.setText("Geçersiz İşlem")

    # def bolme(self):
    #     try:
    #         result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
    #         self.lbl_sonuc.setText(f"Sonuç {str(round(result,2))}")
    #     except ValueError:
    #         self.lbl_sonuc.setText("Geçersiz İşlem")
    #     except ZeroDivisionError:
    #         self.lbl_sonuc.setText("Sayı 0'a Bölünemez")


def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()




