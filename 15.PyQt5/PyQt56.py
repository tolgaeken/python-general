# PyQt5 - CheckBox Kullanımı
from os import system
system('cmd /c "pyuic5 15.PyQt5/PyQt56Design.ui -o 15.PyQt5/PyQt56Design.py"')

import sys
from PyQt5 import QtWidgets
from PyQt56Design import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.cbSinema.stateChanged.connect(self.show_state)
        # self.ui.cbKitap.stateChanged.connect(self.show_state)
        # self.ui.cbSpor.stateChanged.connect(self.show_state)
        self.ui.btnSecilenleriAlHobiler.clicked.connect(self.getAllHobiler)
        self.ui.btnSecilenleriAlDersler.clicked.connect(self.getAllDersler)
        

    def getAllHobiler(self,value):
        result = ""
        items = self.ui.groupHobiler.findChildren(QtWidgets.QCheckBox) # GroupBox içindeki objeleri dolanır
        for i in items:
            if i.isChecked(): # CheckBox ın işaretlenip işaretlenmediğini kontrol eder
                result += i.text() + "\n"
        
        self.ui.lblResultHobiler.setText(result)

    def getAllDersler(self,value):
        result = ""
        items = self.ui.groupDersler.findChildren(QtWidgets.QCheckBox)
        for i in items:
            if i.isChecked():
                result += i.text() + "\n"
        
        self.ui.lblResultDersler.setText(result)




def app():
    app=QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()