import sys

from PyQt5.QtCore import QPropertyAnimation, QRect
from PyQt5.QtWidgets import QDialog, QApplication

from untitledA3 import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui =Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startAnimation)
        self.show()
    def startAnimation(self):
        self.anim = QPropertyAnimation(self.ui.label,b"geometry")
        self.anim.setDuration(10000)
        self.anim.setKeyValueAt(0, QRect(0,0,100,80))
        self.anim.setKeyValueAt(0.5,QRect(160,160,200,180))
        self.anim.setKeyValueAt(1,QRect(400,0,100,80))
        self.anim.start()
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())