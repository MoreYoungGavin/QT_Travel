                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                tateChanged.connect(self.dispAmount)
        self.ui.checkBoxRockyRoad.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxCoffee.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxSoda.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxTea.stateChanged.connect(self.dispAmount)

        self.show()

    @pyqtSlot()
    def dispAmount(self):
        amount=0
        if self.ui.checkBoxChoclateAlmond.isChecked()==True:
            amount=amount+3
        if self.ui.checkBoxChoclateChips.isChecked()==True:
            amount=amount+4
        if self.ui.checkBoxCookieDough.isChecked()==True:
            amount=amount+2
        if self.ui.checkBoxRockyRoad.isChecked()==True:
            amount=amount+5
        if self.ui.checkBoxCoffee.isChecked()==True:
            amount=amount+2
        if self.ui.checkBoxSoda.isChecked()==True:
            amount=amount+3
        if self.ui.checkBoxTea.isChecked()==True:
            amount=amount+1
        self.ui.labelAmount.setText("Total amount is $"+str(amount))

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
