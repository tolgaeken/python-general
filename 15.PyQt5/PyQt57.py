# PyQt5 - RadioButton Kullanımı

from os import system
system('cmd /c "pyuic5 15.PyQt5/PyQt57Design.ui -o 15.PyQt5/PyQt57Design.py"')

import sys
from PyQt5 import QtWidgets
from PyQt57Design import Ui_MainWindow

class myApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(myApp,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radioTurkiye.setChecked(True)
        self.ui.radioLise.setChecked(True)

        self.ui.radioTurkiye.toggled.connect(self.onClickedUlke)
        self.ui.radioAlmanya.toggled.connect(self.onClickedUlke)
        self.ui.radioDanimarka.toggled.connect(self.onClickedUlke)
        self.ui.radioAzerbaycan.toggled.connect(self.onClickedUlke)

        self.ui.radioLise.toggled.connect(self.onClickedEgitim)
        self.ui.radioUniversite.toggled.connect(self.onClickedEgitim)
        self.ui.radioYuksekLisans.toggled.connect(self.onClickedEgitim)
        self.ui.radioDoktora.toggled.connect(self.onClickedEgitim)

        self.ui.btnUlke.clicked.connect(self.getSelectedUlke)
        self.ui.btnEgitim.clicked.connect(self.getSelectedEgitim)

    def onClickedUlke(self):
        rb = self.sender()
        if rb.isChecked():
            print(f"Seçilen Radyo : {rb.text()}")

    def onClickedEgitim(self):
        rb = self.sender()
        if rb.isChecked():
            print(f"Seçilen Radyo : {rb.text()}")
    
    def getSelectedUlke(self):
        items = self.ui.groupBoxUlke.findChildren(QtWidgets.QRadioButton)
        for i in items:
            if i.isChecked():
                self.ui.lblUlke.setText(f"Seçilen Ülke {i.text()}")
    
    def getSelectedEgitim(self):
        items = self.ui.groupBoxEgitim.findChildren(QtWidgets.QRadioButton)
        for i in items:
            if i.isChecked():
                self.ui.lblEgitim.setText(f"Seçilen Eğitim {i.text()}")




def app():
    app=QtWidgets.QApplication(sys.argv)
    win = myApp()
    win.show()
    sys.exit(app.exec_())

app()