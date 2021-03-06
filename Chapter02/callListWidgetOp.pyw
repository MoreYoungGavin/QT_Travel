                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                dlist)
        self.ui.pushButtonEdit.clicked.connect(self.editlist)
        self.ui.pushButtonDelete.clicked.connect(self.delitem)
        self.ui.pushButtonDeleteAll.clicked.connect(self.delallitems)
        self.show()

    def addlist(self):
        self.ui.listWidget.addItem(self.ui.lineEdit.text())
        self.ui.lineEdit.setText('')
        self.ui.lineEdit.setFocus()
        
    def editlist(self):
        row=self.ui.listWidget.currentRow()
        newtext, ok=QInputDialog.getText(self, "Enter new text", "Enter new text")
        if ok and (len(newtext) !=0):
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            self.ui.listWidget.insertItem(row,QListWidgetItem(newtext))
        
    def delitem(self):
        self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
       
    def delallitems(self):
        self.ui.listWidget.clear()

        
if __name__=="__main__":    
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
