���2��H�N��ۻ[�R���FS�1��t�	0u�E��y�e����4$D�g$5���{s!h�BEܙ$q�s!�L���s&�/���Zz>�pC��<�[Hy5�F��-� ����A�a�:^���bj9p�RZ͈X�a'�J���I�
���@�iR��,�Dmh&�K��@
\׽�a�:��� *����N����"{�^'�J���u����	|$�}E�(�UNY3�X��^6XΉ�p�>a3|T����O���13<��hͮ�Vg�n��z(o� ��H� 5J�l��y�e����.$A�7}/���ai;{�WXư>M�};�V���i�2���`�֎Nc�T����J�%{�p�p.d2�Ӗ�Tsy�ҁ\�<4��6�L�:�鍺�u��9@���gdk��=�E`q��\*�3�4ZC��~����t:U����T�x��C�?N�1��]�T���@>U�7�Nc��uAe��a�[֯u u؄�@�	w2%���k^1w�ZX̽4[�b1�\HX�z�q��;�E� ��J�"b��-[�O�S&d:�ۯ�\4{`���,��N�ޕ���H�r��X�Hj5~�Y�{Zk�	c��M�#h��0�y�u����>ڌdCR�ı4\.�o��H�?]�%��X��!�X8C���gdk��=�E`q��\*�3�4Mc���K߉������$L^M�����g>�n����*e�l���xm�7��J�"=A�L��y�QGi��-�:w(%���kK1C�}x̱4z�B1�\���c �3������g����xi�M""6߭[                                                                                                                                                                                                                      age
class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.dispmessage)
        self.show()
    def dispmessage(self):
        resultObj = Result(self.ui.lesc.text(),self.ui.lesn.text(),self.ui.leem.text(),self.ui.lemm.text())
        self.ui.total.setText(str(resultObj.getTotalMarks()))
        self.ui.percentage.setText(str(resultObj.getPercentage()))
if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())