# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demoCheckbox2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(646, 537)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(250, 0, 71, 31))
        font = QtGu                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                .checkBoxSoda.setFont(font)
        self.checkBoxSoda.setObjectName("checkBoxSoda")
        self.verticalLayout.addWidget(self.checkBoxSoda)
        self.checkBoxTea = QtWidgets.QCheckBox(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBoxTea.setFont(font)
        self.checkBoxTea.setObjectName("checkBoxTea")
        self.verticalLayout.addWidget(self.checkBoxTea)
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(60, 450, 541, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelAmount.setFont(font)
        self.labelAmount.setText("")
        self.labelAmount.setObjectName("labelAmount")
        self.groupBoxIceCreams.raise_()
        self.groupBoxDrinks.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.labelDrinks.raise_()
        self.labelAmount.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Menu"))
        self.label_2.setText(_translate("Dialog", "Select your IceCream"))
        self.labelDrinks.setText(_translate("Dialog", "Select your drink"))
        self.groupBoxIceCreams.setTitle(_translate("Dialog", "IceCreams"))
        self.checkBoxChoclateChips.setText(_translate("Dialog", "Mint Choclate Chips $4"))
        self.checkBoxCookieDough.setText(_translate("Dialog", "Cookie Dough $2"))
        self.checkBoxChoclateAlmond.setText(_translate("Dialog", "Chocolate Almond   $3"))
        self.checkBoxRockyRoad.setText(_translate("Dialog", "Rocky Road $5"))
        self.groupBoxDrinks.setTitle(_translate("Dialog", "Drinks"))
        self.checkBoxCoffee.setText(_translate("Dialog", "Coffee $2"))
        self.checkBoxSoda.setText(_translate("Dialog", "Soda $3"))
        self.checkBoxTea.setText(_translate("Dialog", "Tea $1"))

