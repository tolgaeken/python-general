# PyQt5 - DateTime Kullanımı

from os import system
system('cmd /c "pyuic5 15.PyQt5/PyQt510Design.ui -o 15.PyQt5/PyQt510Design.py"')

import sys
from PyQt5 import QtWidgets
from PyQt510Design import Ui_MainWindow
from PyQt5.QtCore import QDate,QTime,QDateTime

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.TotalCalculate)
    
    def TotalCalculate(self):
        start = self.ui.startDate.date()
        end = self.ui.endDate.date()
        print(start,end)

        print(f"Days in month : {start.daysInMonth()}") # Değişkene atanan tarihin bulunduğu ay içindeki gün sayısını belirtir
        print(f"Days in month : {start.daysInYear()}") # Değişkene atanan tarihin bulunduğu yıl içindeki gün sayısını belirtir
        print(f"Total days : {start.daysTo(end)}") # İki tarih arasındaki gün sayısını belirtir
        
        now = QDate.currentDate()
        print(f"Total days : {start.daysTo(now)}") # Değişken ile mevcut tarih arasındaki gün sayısını belirtir

        
       

def app():
    app=QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()