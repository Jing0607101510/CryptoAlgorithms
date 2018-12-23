from PyQt5.QtWidgets import QWidget, QApplication
import sys
from substitution_ui import Ui_Form

class Substitution(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignal()

    def setupSignal(self):
        self.clear1.clicked.connect(self.onClear1Clicked)
        self.clear2.clicked.connect(self.onClear2Clicked)
        self.encry.clicked.connect(self.onEncryClicked)
        self.decry.clicked.connect(self.onDecryClicked)

    def onClear1Clicked(self):
        self.textBrowser_1.clear()
        self.textEdit_1.clear()

    def onClear2Clicked(self):
        self.textBrowser_2.clear()
        self.textEdit_2.clear()

    def onEncryClicked(self):
        plainText = self.textEdit_1.toPlainText()
        key = self.lineEdit.text()
        if plainText and key:
            order = [int(c) for c in key]#转为数字
            key_len = len(key)
            plainText = list(plainText)
            if len(plainText) % key_len != 0:
                plainText.append("A"*(key_len - len(plainText)%key_len))
            res = ''
            for i in range(key_len):
                res += ''.join([plainText[j] for j in range(order.index(i), len(plainText), key_len)])

            self.textBrowser_1.setText(res)
    
    def onDecryClicked(self):
        key = self.lineEdit.text()
        enText = self.textEdit_2.toPlainText()
        if key and enText:
            order = [int(c) for c in key]
            key_len = len(key)
            if len(enText) % key_len != 0:
                enText += '\0' * (key_len-len(enText)%key_len)
            res_matrix = [0]*(key_len*(len(enText)//key_len))
            for i in range(key_len):#这是列的索引, 遍历密文中的每一“列”
                for j in range(len(enText)//key_len):#这是行的索引
                    res_matrix[j*key_len+order.index(i)] = enText[i*(len(enText)//key_len)+j]
            res = ''.join(res_matrix)
            self.textBrowser_2.setText(res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    substitution = Substitution()
    substitution.show()
    sys.exit(app.exec_())