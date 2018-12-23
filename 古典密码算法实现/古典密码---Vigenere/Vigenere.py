from PyQt5.QtWidgets import QApplication, QWidget
import sys
from Vigenere_ui import Ui_Form

class Vigenere(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignal()

    def setupSignal(self):
        self.clear1.clicked.connect(self.onClear1Clicked)
        self.clear2.clicked.connect(self.onClear2Clicked)
        self.encry.clicked.connect(self.onEncryptionClicked)
        self.decry.clicked.connect(self.onDecryptionClicked)

    def onClear1Clicked(self):
        self.textEdit_1.clear()
        self.textBrowser_1.clear()

    def onClear2Clicked(self):
        self.textEdit_2.clear()
        self.textBrowser_2.clear()

    def onEncryptionClicked(self):
        key = self.lineEdit.text()
        plain_text = self.textEdit_1.toPlainText()
        if key and plain_text:
            key_shift = [ord(c)-ord("a") for c in str.lower(key) if str.isalpha(c)]
            en_text = ''
            for i in range(len(plain_text)):
                en_text += chr(ord("a") + (ord(plain_text[i])-ord("a")+key_shift[i%len(key_shift)])%26)
            self.textBrowser_1.setText(en_text)

    def onDecryptionClicked(self):
        key = self.lineEdit.text()
        en_text = self.textEdit_2.toPlainText()
        if key and en_text:
            key_shift = [ord(c)-ord("a") for c in str.lower(key) if str.isalpha(c)]
            plain_text = ''
            for i in range(len(en_text)):
                plain_text += chr(ord("a") + (ord(en_text[i])-ord("a")-key_shift[i%len(key_shift)])%26)
            self.textBrowser_2.setText(plain_text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vigenere = Vigenere()
    vigenere.show()
    sys.exit(app.exec_())