from PyQt5.QtWidgets import QApplication,QWidget
import sys
from RSA_ui import Ui_Form
import random
import math

class RSA(QWidget, Ui_Form):
    def __init__(self):
        super(RSA, self).__init__()
        self.setupUi(self)
        self.setupSignal()
        self.key_length = 1024
    
    def setupSignal(self):
        self.encry.clicked.connect(self.onEncryptionClicked)
        self.decry.clicked.connect(self.onDecryptionClicked)
        self.clear_1.clicked.connect(self.onClear1Clicked)
        self.clear_2.clicked.connect(self.onClear2Clicked)
        self.pushButton.clicked.connect(self.genKey)
    
    def onClear1Clicked(self):
        self.textEdit_1.clear()
        self.textBrowser_1.clear()

    def onClear2Clicked(self):
        self.textEdit_2.clear()
        self.textBrowser_2.clear()
    
    def fast_exp_mode(self, a, b, c):
        res = 1
        a = a % c
        while b != 0:
            if b % 2 == 1:
                res = (res * a) % c
            b >>= 1
            a = (a * a) % c
        return res
    
    def extend_gcd(self, a, b):
        if b == 0:
            return (1, 0, a)
        x1 = 1
        y1 = 0

        x2 = 0
        y2 = 1
        while b != 0:
            q = a // b
            r = a % b
            a = b
            b = r
            x = x1 - q * x2
            x1 = x2
            x2 = x

            y = y1 - q*y2
            y1 = y2
            y2 = y
        return (x1, y1, a)


    def find_E_D(self, ln, bit):
        while 1:
            e = random.randint(0, 1 << bit)#e随机产生
            x,y,r =  self.extend_gcd(e, ln)#e与ln需要互质
            if r == 1:#e与ln就是互质了
                d = x if x >= 0 else x+ln
                return (e, d)

    def find_prime(self, bit):
        while True:
            n = random.randint(0, 1 << bit)
            if n % 2 != 0:
                found = 1
                for i in range(0, 10):
                    if self.prime_test(n) == 0:
                        found = 0
                        break
                if found:
                    return n
    
    def prime_test(self, number):
        q = number - 1
        k = 0
        while q % 2 == 0:
            k += 1
            q = q // 2
        a = random.randint(2, number-2)

        if self.fast_exp_mode(a, q, number) == 1:
            return 1
        
        for j in range(0, k):
            if self.fast_exp_mode(a, (2**j)*q, number) == number-1:
                return 1
        
        return 0

                

    def genKey(self):
        p = self.find_prime(int(self.key_length/2))
        q = self.find_prime(int(self.key_length/2))
        self.n = p * q
        ln = (p-1) * (q-1)
        self.e, self.d = self.find_E_D(ln, int(self.key_length/2))
        self.key.setText("公钥：(%x, %x)       私钥：(%x, %x)"%(self.n, self.e, self.n, self.d))

    def string2int(self, m):
        result = []
        res = 0
        l = self.key_length // 8
        i = 0
        for c in m:
            res <<= 8
            res |= ord(c)
            i += 1
            if i % l == 0:
                result.append(res)
                res = 0
        if i%l != 0:
            result.append(res)
        return result
    
    
    def int2string(self, ints):
        result = []
        while ints:
            ch_int = ints & (0xFF)
            result.insert(0, chr(ch_int))
            ints >>= 8
        return ''.join(result)

    def onEncryptionClicked(self):
        m = self.textEdit_1.toPlainText()
        if m:    
            if len(m) > self.key_length:
                m = m[:self.key_length]        
            int_number = self.string2int(m)[0]
            result = []
            encry_text = self.fast_exp_mode(int_number, self.e, self.n)
            hex_text = "%x"%encry_text
            result.append(hex_text) 
            self.textBrowser_1.setText(''.join(result))

    def onDecryptionClicked(self):
        m = self.textEdit_2.toPlainText()
        if m:
            ints = int(m, 16)
            ints = self.fast_exp_mode(ints, self.d, self.n)
            text = self.int2string(ints)
            self.textBrowser_2.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    rsa = RSA()
    rsa.show()
    sys.exit(app.exec_())