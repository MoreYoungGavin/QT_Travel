                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 self.textEdit.setObjectName("textEdit")
        self.pushButtonFont = QtWidgets.QPushButton(Dialog)
        self.pushButtonFont.setGeometry(QtCore.QRect(120, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonFont.setFont(font)
        self.pushButtonFont.setObjectName("pushButtonFont")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButtonFont.setText(_translate("Dialog", "Change Font"))

