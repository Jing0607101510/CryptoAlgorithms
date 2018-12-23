from PyQt5.QtWidgets import QApplication, QWidget
import sys
from substitution_ui import Ui_Form
import math

class Substitution(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignal()

    def setupSignal(self):
        self.clear1.clicked.connect(self.onClear1Clicked)
        self.encry.clicked.connect(self.onEncryptionClicked)
        self.decry.clicked.connect(self.onDecryptionClicked)
        self.clear2.clicked.connect(self.onClear2Clicked)
    
    def onClear1Clicked(self):
        self.textEdit_1.clear()
        self.textBrowser_1.clear()
    
    def onClear2Clicked(self):
        self.textEdit_2.clear()
        self.textBrowser_2.clear()
    
    def onEncryptionClicked(self):
        plain_text = self.textEdit_1.toPlainText()
        if plain_text:
            line = [[], []]
            for i in range(len(plain_text)):
                line[i%2].append(plain_text[i])
            res = ''.join(line[0]) + ''.join(line[1])
            self.textBrowser_1.setText(res)
    
    def onDecryptionClicked(self):
        en_text = self.textEdit_2.toPlainText()
        if en_text:
            length = len(en_text)
            line = [list(en_text[:math.ceil(length/2)]), list(en_text[math.ceil(length/2):])]
            res = ''
            j = 0
            k = 0
            for i in range(length):
                if i % 2 == 0:
                    res += line[0][j]
                    j += 1
                else:
                    res += line[1][k]
                    k += 1
            self.textBrowser_2.setText(res)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    substitution = Substitution()
    substitution.show()
    sys.exit(app.exec_())


            

