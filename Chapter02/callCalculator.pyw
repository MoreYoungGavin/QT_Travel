                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                um)
        self.show()

    def addtwonum(self):
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a=int(self.ui.lineEditFirstNumber.text())
        else:
            a=0
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b=int(self.ui.lineEditSecondNumber.text())
        else:
            b=0
        sum=a+b
        self.ui.labelResult.setText("Addition: " +str(sum))

    def subtracttwonum(self):
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a=int(self.ui.lineEditFirstNumber.text())
        else:
            a=0
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b=int(self.ui.lineEditSecondNumber.text())
        else:
            b=0
        diff=a-b
        self.ui.labelResult.setText("Substraction: " +str(diff))
        
    def multiplytwonum(self):
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a=int(self.ui.lineEditFirstNumber.text())
        else:
            a=0
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b=int(self.ui.lineEditSecondNumber.text())
        else:
            b=0
        mult=a*b
        self.ui.labelResult.setText("Multiplication: " +str(mult))
        
    def dividetwonum(self):
        if len(self.ui.lineEditFirstNumber.text())!=0:
            a=int(self.ui.lineEditFirstNumber.text())
        else:
            a=0
        if len(self.ui.lineEditSecondNumber.text())!=0:
            b=int(self.ui.lineEditSecondNumber.text())
        else:
            b=0
        division=a/b
        self.ui.labelResult.setText("Division: " +str(round(division,2)))

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
