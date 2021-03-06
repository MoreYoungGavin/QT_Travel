import sys

from PyQt5.QtWidgets import QDialog, QFontDialog, QApplication

from untitledFD import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.changefont)
        self.show()
    def changefont(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.ui.textEdit.setFont(font)
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())