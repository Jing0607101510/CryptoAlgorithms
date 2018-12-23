from PyQt5.QtWidgets import QApplication, QWidget
from Caesar_ui import Ui_Form
import sys


class Caesar_Widget(QWidget, Ui_Form):
    def __init__(self):
        super(Caesar_Widget, self).__init__()
        self.setupUi(self)
        self.setupSignal()
    
    def setupSignal(self):
        self.clear_1.clicked.connect(self.onClear1Clicked)
        self.clear_2.clicked.connect(self.onClear2Clicked)
        self.encryption_1.clicked.connect(self.onEncryptionClicked)
        self.decryption_2.clicked.connect(self.onDecryptionClicked)
    
    def onClear1Clicked(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
    
    def onClear2Clicked(self):
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

    def onEncryptionClicked(self):
        s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ss = 'defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC'
        transtable = str.maketrans(s, ss)
        plain_text = self.lineEdit_1.text()
        encrypted_text = plain_text.translate(transtable)
        self.lineEdit_2.setText(encrypted_text)

    def onDecryptionClicked(self):
        encrypted_text = self.lineEdit_3.text()
        result = []
        for ch in encrypted_text:
            if ch.islower():
                if ord(ch) >= ord('a') + 3:
                    result.append(chr(ord(ch) - 3))
                else:
                    result.append(chr(ord(ch) + 26 - 3))
            elif ch.isupper():
                if ord(ch) >= ord("A") + 3:
                    result.append(chr(ord(cn) - 3))
                else:
                    result.append(chr(ord(ch) + 26 - 3))
            else:
                result.append(ch)
        plain_text = ''.join(result)
        self.lineEdit_4.setText(plain_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    caesar = Caesar_Widget()
    caesar.show()
    sys.exit(app.exec_())


            


        