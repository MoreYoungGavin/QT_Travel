                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 self.ui.verticalSliderCholestrolLevel.valueChanged.connect(self.slidervertical)
        self.show()

    def scrollhorizontal(self,value):    
        self.ui.lineEditResult.setText("Sugar Level : "+str(value))

    def scrollvertical(self, value):    
        self.ui.lineEditResult.setText("Pulse Rate : "+str(value))

    def sliderhorizontal(self, value):    
        self.ui.lineEditResult.setText("Blood Pressure : "+str(value))
        
    def slidervertical(self, value):    
        self.ui.lineEditResult.setText("Cholestrol Level : "+str(value))
      

if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
