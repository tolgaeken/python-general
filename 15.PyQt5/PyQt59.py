# PyQt5 - MessageBox Kullanımı

from os import system
system('cmd /c "pyuic5 15.PyQt5/PyQt59Design.ui -o 15.PyQt5/PyQt59Design.py"')

import sys
from PyQt5 import QtWidgets
from PyQt59Design import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.ShowDialog)

    def ShowDialog(self):
        
        # result değişkeninde self den sonra ilk parametre msgbox başlığınıiikinci parametre msgbox açıklamasını,üçüncü parametre msgbox butonlarını belirler
        result = QMessageBox.question(self,"Close Application","Are You Sure?",QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore,QMessageBox.Cancel)
        match result:
            case QMessageBox.Ok:
                print("Yes Clicked")
                QtWidgets.qApp.quit() # Uygulamadan çıkış yapar
            case _:
                print("No Clicked")

        # msg = QMessageBox()
        # msg.setWindowTitle("Close Application")
        # msg.setText("Are You Sure?")
        # msg.setIcon(QMessageBox.Question)
        # # msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        # msg.setDefaultButton(QMessageBox.Cancel)
        # msg.setDetailedText("Details...")
        # msg.buttonClicked.connect(self.PopupButton)

        
        # x = msg.exec_()
        # print(x)
    
    # def PopupButton(self,i):
    #     match i.text():
    #         case "OK":
    #             print("OK")
    #             QtWidgets.qApp.quit()
    #         case "Cancel":
    #             print("CANCEL")

    #         case "Ignore":
    #             print("IGNORE")
    #         case _:
    #             print("ERROR")
        
       

def app():
    app=QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()