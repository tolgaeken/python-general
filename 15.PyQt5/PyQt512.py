# PyQt5 - TableView Kullanımı

from os import system
system('cmd /c "pyuic5 15.PyQt5/PyQt512Design.ui -o 15.PyQt5/PyQt512Design.py"')

import sys
from PyQt5 import QtWidgets
from PyQt512Design import Ui_MainWindow
from PyQt5.QtWidgets import QTableWidgetItem

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.btnSave.clicked.connect(self.saveProduct)
    
    def loadProducts(self):
        # Bİrden fazla değer ekleme yöntemi
        products = [
            {"name":"Samsung S5","price":2000},
            {"name":"Samsung S6","price":3000},
            {"name":"Samsung S7","price":4000},
            {"name":"Samsung S8","price":5000},
            {"name":"Samsung S9","price":6000}
        ]

        # self.ui.tableProducts.setRowCount(3) # Tablodaki satır sayısı belirlenir
        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2) # Tablodaki sütun sayısı belirlenir
        self.ui.tableProducts.setHorizontalHeaderLabels(("Name","Price")) # Tablonun başlıkları belirlenir
        self.ui.tableProducts.setColumnWidth(0,120) # İlk parametre kolonun index numarasını,ikinci parametre konun genişlik değerini belirler
        self.ui.tableProducts.setColumnWidth(1,50)


        # self.ui.tableProducts.setItem(0,0,QTableWidgetItem("Samsung S5")) # Tek tek değer ekleme yöntemi
        # self.ui.tableProducts.setItem(0,1,QTableWidgetItem("2000"))
        # self.ui.tableProducts.setItem(1,0,QTableWidgetItem("Samsung S6"))
        # self.ui.tableProducts.setItem(1,1,QTableWidgetItem("3000"))
        # self.ui.tableProducts.setItem(2,0,QTableWidgetItem("Samsung S7"))
        # self.ui.tableProducts.setItem(2,1,QTableWidgetItem("4000"))


        rowIndex = 0
        for product in products:
            self.ui.tableProducts.setItem(rowIndex,0,QTableWidgetItem(product["name"])) # (Tablo satır numarası,tablo sütun numarası,eklenecek değer)
            self.ui.tableProducts.setItem(rowIndex,1,QTableWidgetItem(str(product["price"])))
            rowIndex+=1

    def saveProduct(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()

        if name and price is not None:
            rowCount = self.ui.tableProducts.rowCount()
            self.ui.tableProducts.insertRow(rowCount)
            self.ui.tableProducts.setItem(rowCount,0,QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount,1,QTableWidgetItem(price))
            self.ui.txtName.clear() # Tabloya ekleme yaptıktan sonra yeni veri eklemek üzere LineEdit temizlenir
            self.ui.txtPrice.clear()


def app():
    app=QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()