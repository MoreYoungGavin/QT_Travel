import sys

from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import pyqtSlot
from demoCheckBox1 import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.checkBoxCheese.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxOlives.stateChanged.connect(self.dispAmount)
        self.ui.checkBoxSausages.stateChanged.connec                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 