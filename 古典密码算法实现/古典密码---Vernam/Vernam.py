from PyQt5.QtWidgets import QApplication, QWidget
import sys
from Vernam_ui import Ui_Form

class Vernam(QWidget, Ui_Form):
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
            key_list = list(map(ord, key))
            plain_text_list = list(map(ord, plain_text))
            plain_text_list = [plain_text_list[i:i+len(key_list)] for i in range(0, len(plain_text_list), len(key_list))]
            res = ''
            print(plain_text_list)
            for i in range(len(plain_text_list)-1):
                res += ''.join(list(map(lambda x:"%02x"%(x[0]^x[1]), zip(key_list, plain_text_list[i]))))
            res += ''.join(list(map(lambda x:"%02x"%(x[0]^x[1]), zip(plain_text_list[len(plain_text_list)-1], key_list[:len(plain_text_list[len(plain_text_list)-1])]))))
            self.textBrowser_1.setText(res)
            

    def onDecryptionClicked(self):
        key = self.lineEdit.text()
        plain_text = self.textEdit_2.toPlainText()
        if key and plain_text:
            key_list = list(map(ord, key))
            plain_text_list = list(map(lambda x:int(x, 16), [plain_text[i:i+2] for i in range(0, len(plain_text), 2)]))
            plain_text_list = [plain_text_list[i:i+len(key_list)] for i in range(0, len(plain_text_list), len(key_list))]
            res = ''
            for i in range(len(plain_text_list)-1):
                res += ''.join(list(map(lambda x:chr(x[0]^x[1]), zip(key_list, plain_text_list[i]))))
            res += ''.join(list(map(lambda x:chr(x[0]^x[1]), zip(plain_text_list[len(plain_text_list)-1], key_list[:len(plain_text_list[len(plain_text_list)-1])]))))
            self.textBrowser_2.setText(res)
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    vernam = Vernam()
    vernam.show()
    sys.exit(app.exec_())
    