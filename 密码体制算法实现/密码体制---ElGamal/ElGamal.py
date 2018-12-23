from PyQt5.QtWidgets import QApplication, QWidget
import sys
from ElGamal_ui import Ui_Form
import random

class ElGamal(QWidget, Ui_Form):
    def __init__(self):
        super(ElGamal, self).__init__()
        self.setupUi(self)
        self.setupSignal()
        self.setupData()

    def setupSignal(self):
        self.encry.clicked.connect(self.onEncryptionClicked)
        self.decry.clicked.connect(self.onDecryptionClicked)
        self.clear1.clicked.connect(self.onClear1Clicked)
        self.clear2.clicked.connect(self.onClear2Clicked)
        self.gen_key.clicked.connect(self.genKey)
    
    def onClear1Clicked(self):
        self.textEdit_1.clear()
        self.textBrowser_1.clear()

    def onClear2Clicked(self):
        self.textBrowser_2.clear()
        self.textEdit_2.clear()
    
    def setupData(self):
        self.prime = int(self.lineEdit_1.text())
        self.prime_root = int(self.lineEdit_2.text())
        self.xa = random.randint(1,1000000000)
        self.lineEdit_3.setText(str(self.xa))
        self.public_a = self.gen_pub_key(self.xa)
        self.lineEdit_7.setText(str(self.public_a))
    
    def genKey(self):
        self.xa = random.randint(1,1000000000)
        self.lineEdit_3.setText(str(self.xa))
        self.public_a = self.gen_pub_key(self.xa)
        self.lineEdit_7.setText(str(self.public_a))
    
    def gen_pub_key(self, x):
        return self.fast_exp_mode(self.prime_root, x, self.prime)

    def fast_exp_mode(self, a, b, c):
        res = 1
        a = a % c
        while b != 0:
            if b % 2 == 1:
                res = (res * a) % c
            b >>= 1
            a = (a * a) % c
        return res
    
    def split_plainText(self, text):
        if len(text) % 3 != 0:
            text += '\0'*(3-len(text)%3)
        n = 0
        i = 0
        res = []
        while i < len(text):
            n = (n << 8) | ord(text[i])
            n = (n << 8) | ord(text[i+1])
            n = (n << 8) | ord(text[i+2])
            res.append(n)
            n = 0
            i += 3
        return res
    
    def onEncryptionClicked(self):
        plain_text = self.textEdit_1.toPlainText()
        if plain_text:
            blocks = self.split_plainText(plain_text)
            result = ''
            for block in blocks:
                result += self.encryption(block)
            self.textBrowser_1.setText(result)
    
    def calc(self, a, key):
        return self.fast_exp_mode(a, key, self.prime)
        
    def encryption(self, block):
         k = random.randint(1, self.prime-1)
         K = self.calc(self.public_a, k)
         c1 = self.calc(self.prime_root, k)
         c2 = ((K%self.prime)*(block%self.prime))%self.prime
         return '%08x%08x'%(c1, c2)

    def split_enText(self, text):
        if len(text) % 16 != 0:
            text += '0' * (16 - len(text) % 16)
        result = []
        i = 0
        while i < len(text):
            c1 = text[i: i+8]
            c2 = text[i+8: i+16]
            i += 16
            c1 = int(c1, 16)
            c2 = int(c2, 16)
            result.append([c1, c2])
        return result
        
    
    def onDecryptionClicked(self):
        en_text = self.textEdit_2.toPlainText()
        if en_text:
            result = ''
            blocks = self.split_enText(en_text)
            for block in blocks:
                result += self.decryption(block)
            self.textBrowser_2.setText(result)

    def decryption(self, block):
        c1 = block[0]
        c2 = block[1]
        K = self.calc(c1, self.xa)
        K_inverse = self.get_inverse(K, self.prime)
        M = (c2 * (K_inverse % self.prime)) % self.prime
        m = ''
        for i in range(3):
            m += chr(M&0x0ff)
            M >>= 8
        return m[::-1]
    
    def get_inverse(self, x, mod):
        x1 = 1
        x2 = 0
        x3 = mod
        y1 = 0
        y2 = 1
        y3 = (x%mod+mod)%mod
        while y3 != 1:
            q = x3 // y3
            t1 = x1 - q * y1
            t2 = x2 - q * y2
            t3 = x3 - q * y3
            x1 = y1
            x2 = y2
            x3 = y3
            y1 = t1
            y2 = t2
            y3 = t3
        return y2




if __name__ == "__main__":
    app = QApplication(sys.argv)
    elgamal = ElGamal()
    elgamal.show()
    sys.exit(app.exec_())