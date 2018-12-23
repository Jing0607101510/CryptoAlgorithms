from PyQt5.QtWidgets import QApplication, QWidget
import sys
from SHA512_ui import Ui_Form
import copy

class SHA512(QWidget, Ui_Form):
    def __init__(self):
        super(SHA512, self).__init__()
        self.setupUi(self)
        self.setupSignal()
        self.setupData()

    def setupSignal(self):
        self.confirm.clicked.connect(self.start_hash)
        self.clear.clicked.connect(self.onClearClicked)
    
    def onClearClicked(self):
        self.textEdit.clear()
        self.textBrowser.clear()
    
    def setupData(self):
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

    def start_hash(self):
        text = self.textEdit.toPlainText()
        if text:
            nums = self.padding_and_append_length(text)#没有问题
            H = copy.deepcopy(self.H0)
            for i in range(len(nums)):
                self.W.clear()
                self.W = self.gen_W(nums[i])
                H0 = H
                for j in range(80):#前两部没有问题
                    H = self.round(H, self.W[j], self.K[j])
                H = self.add_H0(H0, H)
            
            res = ''
            for h in H:
                res += "%016x"%(h)
            self.textBrowser.setText(res)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    sha512 = SHA512()
    sha512.show()
    sys.exit(app.exec_())

