from PyQt5.QtWidgets import QApplication, QWidget
import sys
from Schnorr_ui import Ui_Form
import random
import copy

class Schnorr(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setupSignal()
        self.setupData()

    def setupSignal(self):
        self.gen.clicked.connect(self.gen_ds)
        self.varify.clicked.connect(self.varify_ds)
        self.clear1.clicked.connect(self.onClear1Clicked)
        self.clear2.clicked.connect(self.onClear2Clicked)
        self.genKey_bt.clicked.connect(self.genKey)
    
    def onClear1Clicked(self):
        self.textEdit_1.clear()
        self.textBrowser_1.clear()
        self.textBrowser_2.clear()

    def onClear2Clicked(self):
        self.textEdit_2.clear()
        self.textEidt_3.clear()
        self.lineEdit.clear()
    
    def setupData(self):
        self.prime = int(self.line_p.text())
        self.prime_1_factor = int(self.line_p_1_factor.text())
        self.a = int(self.line_a.text())
        self.s = random.randint(1, self.prime_1_factor)
        self.line_s.setText(str(self.s))
        self.v = self.gen_pub_key(self.s)
        self.line_v.setText(str(self.v))

        self.K = [
            0x428a2f98d728ae22,0x7137449123ef65cd,0xb5c0fbcfec4d3b2f,0xe9b5dba58189dbbc,0x3956c25bf348b538,
            0x59f111f1b605d019,0x923f82a4af194f9b,0xab1c5ed5da6d8118,0xd807aa98a3030242,0x12835b0145706fbe,
            0x243185be4ee4b28c,0x550c7dc3d5ffb4e2,0x72be5d74f27b896f,0x80deb1fe3b1696b1,0x9bdc06a725c71235,
            0xc19bf174cf692694,0xe49b69c19ef14ad2,0xefbe4786384f25e3,0x0fc19dc68b8cd5b5,0x240ca1cc77ac9c65,
            0x2de92c6f592b0275,0x4a7484aa6ea6e483,0x5cb0a9dcbd41fbd4,0x76f988da831153b5,0x983e5152ee66dfab,
            0xa831c66d2db43210,0xb00327c898fb213f,0xbf597fc7beef0ee4,0xc6e00bf33da88fc2,0xd5a79147930aa725,
            0x06ca6351e003826f,0x142929670a0e6e70,0x27b70a8546d22ffc,0x2e1b21385c26c926,0x4d2c6dfc5ac42aed,
            0x53380d139d95b3df,0x650a73548baf63de,0x766a0abb3c77b2a8,0x81c2c92e47edaee6,0x92722c851482353b,
            0xa2bfe8a14cf10364,0xa81a664bbc423001,0xc24b8b70d0f89791,0xc76c51a30654be30,0xd192e819d6ef5218,
            0xd69906245565a910,0xf40e35855771202a,0x106aa07032bbd1b8,0x19a4c116b8d2d0c8,0x1e376c085141ab53,
            0x2748774cdf8eeb99,0x34b0bcb5e19b48a8,0x391c0cb3c5c95a63,0x4ed8aa4ae3418acb,0x5b9cca4f7763e373,
            0x682e6ff3d6b2b8a3,0x748f82ee5defb2fc,0x78a5636f43172f60,0x84c87814a1f0ab72,0x8cc702081a6439ec,
            0x90befffa23631e28,0xa4506cebde82bde9,0xbef9a3f7b2c67915,0xc67178f2e372532b,0xca273eceea26619c,
            0xd186b8c721c0c207,0xeada7dd6cde0eb1e,0xf57d4f7fee6ed178,0x06f067aa72176fba,0x0a637dc5a2c898a6,
            0x113f9804bef90dae,0x1b710b35131c471b,0x28db77f523047d84,0x32caab7b40c72493,0x3c9ebe0a15c9bebc,
            0x431d67c49c100d4c,0x4cc5d4becb3e42b6,0x597f299cfc657e2a,0x5fcb6fab3ad6faec,0x6c44198c4a475817
        ]
        self.H0 = [
            0x6a09e667f3bcc908, 0xbb67ae8584caa73b, 0x3c6ef372fe94f82b, 0xa54ff53a5f1d36f1,
            0x510e527fade682d1, 0x9b05688c2b3e6c1f, 0x1f83d9abfb41bd6b, 0x5be0cd19137e2179
        ]
        self.W = []#80个子分组

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
                
    
    def genKey(self):
        self.s = random.randint(1, self.prime_1_factor)
        self.line_s.setText(str(self.s))
        self.v = self.gen_pub_key(self.s)
        self.line_v.setText(str(self.v))
    
    def gen_pub_key(self, x):
        return self.fast_exp_mode(self.get_inverse(self.a, self.prime), x, self.prime)

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
    
    def gen_ds(self):
        plain_text = self.textEdit_1.toPlainText()
        if plain_text:
            r = random.randint(0, self.prime_1_factor)
            x = self.fast_exp_mode(self.a, r, self.prime)
            ##需要修改
            x = '%x'%(x)
            if len(x) % 2 == 1:
                x = '0' + x
            i = 0
            xx = ''
            while i < len(x):
                xx += chr(int(x[i:i+2], 16))
                i += 2
            e = self.start_hash(plain_text+xx)#得到整数一个
            y = (r + (self.s * e) % self.prime_1_factor) % self.prime_1_factor
            self.textBrowser_1.setText("%x"%e)
            self.textBrowser_2.setText("(%x, %x)"%(e, y))

    def varify_ds(self):
        plain_text = self.textEdit_2.toPlainText()##
        ds = self.textEdit_3.toPlainText().replace("(", "")
        ds = ds.replace(")", "")
        recept_DS_e, recept_DS_y = ds.split(",")
        if plain_text and recept_DS_e and recept_DS_y and plain_text:#这些都是字符串
            recept_DS_e = int(recept_DS_e, 16)
            recept_DS_y = int(recept_DS_y, 16)
            
            x_star = (self.fast_exp_mode(self.a, recept_DS_y, self.prime) * self.fast_exp_mode(self.v, recept_DS_e, self.prime)) % self.prime
            x_star = "%x"%x_star
            if len(x_star) % 2 != 0:
                x_star = '0'+x_star
            xx_star = ''
            i = 0
            while i < len(x_star):
                xx_star += chr(int(x_star[i:i+2], 16))
                i += 2
            hash = self.start_hash(plain_text+xx_star)#自己生成的hash
            if hash == recept_DS_e:
                self.lineEdit.setText("Yes!!!")
            else:
                self.lineEdit.setText("No!!!")
        
    
    def calc(self, a, key):
        return self.fast_exp_mode(a, key, self.prime)
        


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


    def padding_and_append_length(self, text):
        length = len(text) * 8
        hex = ''
        for c in text:
            hex += '%02x'%(ord(c))
        hex += '80'
        if len(hex) * 4 % 1024 > 896:
            hex += '0' * ((896 + (1024-len(hex)*4%1024)) // 4)
        elif len(hex) * 4 % 1024 < 896:
            hex += '0' * ((896 - (len(hex)*4%1024))//4)
        hex += '%032x'%(length)
        hexs = []
        i = 0
        while i < len(hex):
            hexs.append(hex[i:i+256])
            i += 256
        return hexs#按每组1024位划分文本,hexs是字符串列表

    def ROTR(self, x, time):
        time = time % 64
        return (((x >> time) & 0xffffffffffffffff) | (x & 0xffffffffffffffff) << (64-time)) & 0xffffffffffffffff
    
    def SHR(self, x, time):
        time = time % 64
        return (x >> time) &0xffffffffffffffff
    
    def P0(self, x):
        return self.ROTR(x, 1) ^ self.ROTR(x, 8) ^ self.SHR(x, 7)
    
    def P1(self, x):
        return self.ROTR(x, 19) ^ self.ROTR(x, 61) ^ self.SHR(x, 6)

    def gen_W(self, block):
        W = []
        i = 0
        while i < len(block):
            W.append(int(block[i:i+16], 16))
            i += 16
        for i in range(64):
            index = i + 16
            w_index = (W[index-16] + self.P0(W[index-15]) + W[index-7] + self.P1(W[index-2])) & 0xffffffffffffffff
            W.append(w_index)
        return W
    
    def Ch(self, e, f, g):
        return (e & f) ^ ((~e) & g)
    
    def SUM1(self, e):
        return self.ROTR(e, 14) ^ self.ROTR(e, 18) ^ self.ROTR(e, 41)

    def Maj(self, a, b, c):
        return (a & b) ^ (a & c) ^ (b & c)
    
    def SUM0(self, a):
        return self.ROTR(a, 28) ^ self.ROTR(a, 34) ^ self.ROTR(a, 39)
    
    def round(self, H, w, k):
        T1 = (H[7] + self.Ch(H[4], H[5], H[6]) + self.SUM1(H[4]) + w + k) & 0xffffffffffffffff
        T2 = (self.SUM0(H[0]) + self.Maj(H[0], H[1], H[2])) & 0xffffffffffffffff
        h = H[6]
        g = H[5]
        f = H[4]
        e = (H[3] + T1) & 0xffffffffffffffff
        d = H[2]
        c = H[1]
        b = H[0]
        a = (T1 + T2) & 0xffffffffffffffff
        return [a, b, c, d, e, f, g, h]
    
    def add_H0(self, H0, H):
        res = []
        for i in range(len(H0)):
            res.append((H0[i] + H[i]) & 0xffffffffffffffff)
        return res

    def start_hash(self, text):
        if text:
            nums = self.padding_and_append_length(text)#没有问题
            H = copy.deepcopy(self.H0)
            for i in range(len(nums)):
                self.W.clear()
                self.W = self.gen_W(nums[i])
                H0 = H
                for j in range(80):#前两部没有问题
                    H = self.round(H, self.W[j], self.K[j])
                H = self.add_H0(H0, H)#是一个列表
            
            res = ''
            for h in H:
                res += "%016x"%(h)
            return int(res, 16)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    schnorr = Schnorr()
    schnorr.show()
    sys.exit(app.exec_())