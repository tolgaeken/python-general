# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '15.PyQt5/PyQt56Design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnSecilenleriAlHobiler = QtWidgets.QPushButton(self.centralwidget)
        self.btnSecilenleriAlHobiler.setGeometry(QtCore.QRect(60, 290, 131, 71))
        self.btnSecilenleriAlHobiler.setObjectName("btnSecilenleriAlHobiler")
        self.lblResultHobiler = QtWidgets.QLabel(self.centralwidget)
        self.lblResultHobiler.setGeometry(QtCore.QRect(30, 380, 181, 141))
        self.lblResultHobiler.setText("")
        self.lblResultHobiler.setObjectName("lblResultHobiler")
        self.groupHobiler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupHobiler.setGeometry(QtCore.QRect(30, 10, 241, 241))
        self.groupHobiler.setObjectName("groupHobiler")
        self.widget = QtWidgets.QWidget(self.groupHobiler)
        self.widget.setGeometry(QtCore.QRect(30, 70, 151, 65))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cbSinema = QtWidgets.QCheckBox(self.widget)
        self.cbSinema.setObjectName("cbSinema")
        self.verticalLayout.addWidget(self.cbSinema)
        self.cbKitap = QtWidgets.QCheckBox(self.widget)
        self.cbKitap.setObjectName("cbKitap")
        self.verticalLayout.addWidget(self.cbKitap)
        self.cbSpor = QtWidgets.QCheckBox(self.widget)
        self.cbSpor.setObjectName("cbSpor")
        self.verticalLayout.addWidget(self.cbSpor)
        self.groupDersler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupDersler.setGeometry(QtCore.QRect(330, 10, 241, 241))
        self.groupDersler.setObjectName("groupDersler")
        self.layoutWidget = QtWidgets.QWidget(self.groupDersler)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 70, 151, 65))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbWeb = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbWeb.setObjectName("cbWeb")
        self.verticalLayout_2.addWidget(self.cbWeb)
        self.cbProgramlama = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbProgramlama.setObjectName("cbProgramlama")
        self.verticalLayout_2.addWidget(self.cbProgramlama)
        self.cbMatematik = QtWidgets.QCheckBox(self.layoutWidget)
        self.cbMatematik.setObjectName("cbMatematik")
        self.verticalLayout_2.addWidget(self.cbMatematik)
        self.btnSecilenleriAlDersler = QtWidgets.QPushButton(self.centralwidget)
        self.btnSecilenleriAlDersler.setGeometry(QtCore.QRect(370, 280, 131, 71))
        self.btnSecilenleriAlDersler.setObjectName("btnSecilenleriAlDersler")
        self.lblResultDersler = QtWidgets.QLabel(self.centralwidget)
        self.lblResultDersler.setGeometry(QtCore.QRect(350, 380, 181, 141))
        self.lblResultDersler.setText("")
        self.lblResultDersler.setObjectName("lblResultDersler")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnSecilenleriAlHobiler.setText(_translate("MainWindow", "Se??ilenleri Al"))
        self.groupHobiler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbSinema.setText(_translate("MainWindow", "Sinema"))
        self.cbKitap.setText(_translate("MainWindow", "Kitap"))
        self.cbSpor.setText(_translate("MainWindow", "Spor"))
        self.groupDersler.setTitle(_translate("MainWindow", "GroupBox"))
        self.cbWeb.setText(_translate("MainWindow", "Web Tasar??m"))
        self.cbProgramlama.setText(_translate("MainWindow", "Programlama"))
        self.cbMatematik.setText(_translate("MainWindow", "Matematik"))
        self.btnSecilenleriAlDersler.setText(_translate("MainWindow", "Se??ilenleri Al"))
