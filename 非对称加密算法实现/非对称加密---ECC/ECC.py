from PyQt5.QtWidgets import QApplication, QWidget
import sys
from ECC_ui import Ui_Form
import copy

class ECC(QWidget, Ui_Form):
    def __init__(self):
        super(ECC, self).__init__()
        self.setupUi(self)
        self.setupSignal()
        self.setupData()
    
    def setupData(self):
        self.K = 9
        self.a = 5
        self.b = 37
        self.p = 127
        self.r = 7
        self.A = [4, 11]#基钥
        self.B = self.mul(self.A, self.K) #公钥部分
    
    
    def setupSignal(self):
        self.encry.clicked.connect(self.onEncryptionClicked)
        self.decry.clicked.connect(self.onDecryptionClicked)
        self.clear1.clicked.connect(self.onClear1Clicked)
        self.clear2.clicked.connect(self.onClear2Clicked)
    
    def onClear1Clicked(self):
        self.textBrowser_1.clear()
        self.textEdit_1.clear()

    def onClear2Clicked(self):
        self.textBrowser_2.clear()
        self.textEdit_2.clear()
    

    #求乘法逆元
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
    
    def add(self, p1, p2):
        if p1 == p2:
            #斜率
            k = ((3 * p1[0]**2+self.a) * self.get_inverse(2*p1[1], self.p)) % self.p
        else:
            k = (p2[1] - p1[1]) * self.get_inverse(p2[0] - p1[0], self.p) % self.p
        res = []
        res.append((k*k-p1[0]-p2[0]) % self.p)
        res.append((k*(p1[0]-res[0]) - p1[1]) % self.p)
        res[0] = (res[0] + self.p) % self.p
        res[1] = (res[1] + self.p) % self.p
        return res
    
    def mul(self, p, n):
        q = copy.deepcopy(p)
        n -= 1
        for i in range(n):
            q = self.add(q, p)
        return q

    def encryption_point(self, x, y):
        c1 = self.mul(self.A, self.r)
        z = self.mul(self.B, self.r)
        c2 = [z[0]*x%self.p, z[1]*y%self.p]
        c11 = "%02x"%(c1[0])
        c12 = "%02x"%(c1[1])
        c21 = "%02x"%(c2[0])
        c22 = "%02x"%(c2[1])
        return [c11, c12, c21, c22]

    def encryption(self, plain_text):
        result = []
        for i in range(len(plain_text)):
            en_c = self.encryption_point(i, ord(plain_text[i]))
            result.extend(en_c)
        return ''.join(result)


    def decryption(self, en_text):
        en_hex = int(en_text, 16)
        chars = []
        while en_hex:
             chars.insert(0, en_hex&(0x0ff))
             en_hex = en_hex >> 8
        i = 0
        res = ''
        while i < len(chars):
            c11 = chars[i]
            c12 = chars[i+1]
            c21 = chars[i+2]
            c22 = chars[i+3]
            M = self.decryption_point(c11, c12, c21, c22)
            res += chr(M)
            i += 4
        return res
    

    def decryption_point(self, c11, c12, c21, c22):
        z = self.mul([c11, c12], self.K)
        m1 = c21 * self.get_inverse(z[0], self.p) % self.p
        m2 = c22 * self.get_inverse(z[1], self.p) % self.p 
        return m2
    
    def onEncryptionClicked(self):
        plain_text = self.textEdit_1.toPlainText()
        if plain_text:
            en_text = self.encryption(plain_text)
            self.textBrowser_1.setText(en_text)

    def onDecryptionClicked(self):
        en_text = self.textEdit_2.toPlainText()
        if en_text:
            plain_text = self.decryption(en_text)
            self.textBrowser_2.setText(plain_text)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ecc = ECC()
    ecc.show()
    sys.exit(app.exec_())