from PyQt5.QtWidgets import QApplication, QWidget
import sys
from SHA3_ui import Ui_Form
import numpy as np
import copy

class SHA3(QWidget, Ui_Form):
    def __init__(self):
        super(SHA3, self).__init__()
        self.setupUi(self)
        self.setupSignal()
        self.setupData()
    
    def setupData(self):
        self.r = 576
        self.c = 1024
        self.l = int(self.lineEdit.text())#以1个十六进制数位单位
        self.RC = [
            0x0000000000000001, 0x0000000000008082, 0x800000000000808A, 0x8000000080008000,
            0x000000000000808B, 0x0000000080000001, 0x8000000080008081, 0x8000000000008009, 
            0x000000000000008A, 0x0000000000000088, 0x0000000080008009, 0x000000008000000A,
            0x000000008000808B, 0x800000000000008B, 0x8000000000008089, 0x8000000000008003,
            0x8000000000008002, 0x8000000000000080, 0x000000000000800A, 0x800000008000000A,
            0x8000000080008081, 0x8000000000008080, 0x0000000080000001, 0x8000000080008008
        ]
        self.R_CONS = [
            [0, 36, 3, 41, 18], 
            [1, 44, 10, 45, 2], 
            [62, 6, 43, 15, 61],
            [28, 55, 25, 21, 56],
            [27, 20, 39, 8, 14]
        ]
    
    def setupSignal(self):
        self.clear.clicked.connect(self.onClearClicked)
        self.pushButton.clicked.connect(self.start_hash)


    def onClearClicked(self):
        self.textEdit.clear()
        self.textBrowser.clear()

    def C(self, col):#一行
        res = 0
        for i in range(5):
            res ^= col[i]
        return res
    
    def LOTL(self, col):
        return ((col << 1) | (col >> 63)) & 0xffffffffffffffff
        

    def theta(self, mid_value):
        res = np.zeros([5, 5], dtype=np.uint64)
        res = res.tolist()
        array = np.array(mid_value, dtype=np.uint64)
        for i in range(5):#遍历列
            for j in range(5):
                res[i][j] = mid_value[i][j] ^ self.C((array[:,(j-1)%5]).tolist()) 
                res[i][j] ^= self.LOTL(self.C((array[:,(j+1)%5]).tolist()))
        return res
    
    def right_shift(self, num, time):
        return ((num >> time) | (num << (64 - time))) & 0xffffffffffffffff

    
    def rho(self, mid_value):
        res = np.zeros([5, 5], dtype=np.uint64)
        res = res.tolist()
        for i in range(5):
            for j in range(5):
                res[i][j] = self.right_shift(mid_value[i][j], self.R_CONS[i][j])
        return res

    def pi(self, mid_value):
        res = np.zeros([5, 5], dtype=np.uint64)
        res = res.tolist()
        for i in range(5):
            for j in range(5):
                res[(2*j+3*i)%5][i] = mid_value[i][j]
        return res

    def chi(self, mid_value):
        res = np.zeros([5, 5], dtype=np.uint64)
        res = res.tolist()
        for i in range(5):
            for j in range(5):
                res[i][j] = mid_value[i][j] ^ (~(mid_value[i][(j+1)%5])) & mid_value[i][(j+2)%5]
        return res

    def iota(self,mid_value, i):
        res = mid_value
        res[0][0] = res[0][0] ^ self.RC[i]
        return res
    
    #需要转化为2维矩阵，而且是5*5
    def split(self, text):
        hhex = ''
        for c in text:
            hhex += '%02x'%(ord(c))
        hexs = []
        i = 0
        while i < len(hhex):
            matrix = np.zeros([5, 5], dtype=np.uint64)
            matrix = matrix.tolist()
            num = int(hhex[i:i+144], 16) << self.c
            for j in range(4, -1, -1):
                for k in range(4, -1 , -1):
                    matrix[j][k] = (num & 0xffffffffffffffff)
                    num = num >> 64                                
            i += 144
            hexs.append(matrix)
        #这里的每一个hex是1600位的，而5*5中每个纵是64位的，也就是16个十六进制数
        return hexs
    
    def function(self, mid_value):
        for i in range(24):
            mid_value = self.theta(mid_value)#引用传递
            mid_value = self.rho(mid_value)
            mid_value = self.pi(mid_value)
            mid_value = self.chi(mid_value)
            mid_value = self.iota(mid_value, i)
        return mid_value#二维数组
    
    def to_hex(self, matrix):
        res = ''
        for i in range(5):
            for j in range(5):
                res += '%016x'%(matrix[i][j])
        res = "%0144x"%(int(res, 16) >> self.c)
        return res

    def start_hash(self):
        text = self.textEdit.toPlainText()
        self.l = int(self.lineEdit.text())
        if text:
            #简单填充
            text += chr(0x80)
            text += '\0' * (72 - (len(text) * 8 % self.r) // 8)
            blocks = self.split(text)#每个block是为2维列表
            s = np.zeros([5, 5], dtype=np.uint64)
            s = s.tolist()
            #海绵结构：吸水过程
            for block in blocks:
                for i in range(5):
                    for j in range(5):
                        s[i][j] ^= block[i][j]
                s = self.function(s)#mid_value是二维array
            #挤压过程
            hex_s = self.to_hex(s)
            res = ''
            block_number = (self.l * 4) // self.r
            last_block_len = (self.l * 4 % self.r) // 4
            for i in range(block_number):
                res += hex_s
                s = self.function(s)
                hex_s = self.to_hex(s)
            res += hex_s[:last_block_len]
            self.textBrowser.setText(res)
                


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sha3 = SHA3()
    sha3.show()
    sys.exit(app.exec_())
        