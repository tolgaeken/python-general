# PyQt5 - ListView Kullanımı

from os import system
system('cmd /c "pyuic5 15.PyQt5/PyQt511Design.ui -o 15.PyQt5/PyQt511Design.py"')

import sys
from PyQt5 import QtWidgets
from PyQt511Design import Ui_MainWindow
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QMessageBox

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadStudents()

        self.ui.btnAdd.clicked.connect(self.addStudent)
        self.ui.btnEdit.clicked.connect(self.editStudent)
        self.ui.btnDelete.clicked.connect(self.deleteStudent)
        self.ui.btnUp.clicked.connect(self.upStudent)
        self.ui.btnDown.clicked.connect(self.downStudent)
        self.ui.btnSort.clicked.connect(self.sortStudents)
        self.ui.btnExit.clicked.connect(self.close)
    
    def loadStudents(self):
        self.ui.listItems.addItems(["Ahmet","Ali","Çınar"])
        self.ui.listItems.setCurrentRow(0)
    
    def addStudent(self):
        # currentIndex = self.ui.listItems.currentRow() # Aktif olarak tıklanan satır numarasını verir
        lastIndex = self.ui.listItems.count() # Toplam satır sayısını verir, aşağıdaki if bloğunda kaydı en sona eklemek için kullanılır
        text,ok=QInputDialog.getText(self,"New Student","Student Name")
        if (ok is not None) and (text is not (None or "")): # Eklenecek veri boş ya da dialog kutusunda ok dışında başka butona basılmadığı durumda ekler
            self.ui.listItems.insertItem(lastIndex,text) # İlk parametre kaydın yerleştirileceği index numarasınıi ikinci parametre değeri belirtir

    def editStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)

        if item is not None:
            text,ok = QInputDialog.getText(self,"EditStudent","New Student Name",QLineEdit.Normal,item.text())
            if (ok is not None) and (text is not (None or "")):
                item.setText(text)
    
    def deleteStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)

        if item is None:
            return
        
        question = QMessageBox.question(self,"Remove Student",f"Are You Sure Delete {item.text()}?",QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            item = self.ui.listItems.takeItem(index)
            del item
    
    def upStudent(self): # Kaydı bir üst sıraya kaydırmak için kullanılır
        index = self.ui.listItems.currentRow()
        if index >=1: # En üst sıradaki kaydın en üstte olup olmadığı kontrol edilir
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1,item)
            self.ui.listItems.setCurrentItem(item)
    
    def downStudent(self): # Kaydı bir alt sıraya kaydırak için kullanılır
        index = self.ui.listItems.currentRow()
        if index <= self.ui.listItems.count(): # En alt sıradaki kaydın en altta olup olmadığı kontrol edilir
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1,item)
            self.ui.listItems.setCurrentItem(item)
    
    def sortStudents(self):
        self.ui.listItems.sortItems() # Kayıtları sıralamak için kullanılır

    def close(self):
        # quit() # Uygulamadan çıkış yapmak için kullanılır fakat "QtWidgets.qApp.quit()" ile daha hızlı çıkış yapılır
        QtWidgets.qApp.quit()
        


        
       

def app():
    app=QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()