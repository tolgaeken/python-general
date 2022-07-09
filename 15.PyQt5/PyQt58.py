# PyQt5 - ComboBox Kullanımı

from os import system
system('cmd /c "pyuic5 15.PyQt5/PyQt58Design.ui -o 15.PyQt5/PyQt58Design.py"')

import sys
from PyQt5 import QtWidgets
from PyQt58Design import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.cbSehirler.addItem("Ankara")

        # combo = self.ui.cbSehirler
        # combo.addItem("Ankara") # ComboBox içine tek tek değer ekler
        # combo.addItem("İstanbul")
        # combo.addItem("İzmir")
        # combo.addItems(["Adana","Antalya","Muğla"]) # ComboBox içinde birden fazla değer ekler

        self.ui.btnLoadItems.clicked.connect(self.LoadItems)
        self.ui.btnClearItems.clicked.connect(self.ClearItems)

        self.ui.cbSehirler.currentIndexChanged.connect(self.SelectedChangedIndex) # ComboBox içinde mevcut index değiştiğinde tetiklenecek fonksiyonu belirler
        self.ui.cbSehirler.currentIndexChanged[str].connect(self.SelectedChangedText)

    def LoadItems(self):
        sehirler = ["Ankara","İstanbul","İzmir","Adana","Antalya","Muğla"]
        self.ui.cbSehirler.addItems(sehirler)
    
    # def GetItem(self):
    #     print(self.ui.cbSehirler.currentText())
    #     print(self.ui.cbSehirler.currentIndex())
    #     count = self.ui.cbSehirler.count()
    #     for index in range(count):
    #         print(self.ui.cbSehirler.itemText(index))
    
    def SelectedChangedIndex(self,index):
        return index
    
    def SelectedChangedText(self,text):
        if self.SelectedChangedIndex == -1:
            self.ui.lblResult.setText("")
            return None
        
        self.ui.lblResult.setText(text)
    
    def ClearItems(self):
        self.ui.cbSehirler.clear()






def app():
    app=QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()