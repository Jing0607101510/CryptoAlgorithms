from PyQt5.QtWidgets import QApplication, QWidget 
import sys
from DAA_ui import Ui_Form
import numpy as np

class DAA(QWidget, Ui_Form):
    def __init__(self):
        super(DAA, self).__init__()
        self.setupUi(self)
        self.setupData()
        self.setupSignal()

    def setupData(self):#(1,3) 12->42
        self.IP = [58,50,42,34,26,18,10,2,60,52,44,36,28,20,12,4,
            62,54,46,38,30,22,14,6,64,56,48,40,32,24,16,8,
            57,49,41,33,25,17, 9,1,59,51,43,35,27,19,11,3,
            61,53,45,37,29,21,13,5,63,55,47,39,31,23,15,7]#前28为为左，后28位为右//以行划分
        self.invIP = [40,8,48,16,56,24,64,32,39,7,47,15,55,23,63,31,
            38,6,46,14,54,22,62,30,37,5,45,13,53,21,61,29,
            36,4,44,12,52,20,60,28,35,3,43,11,51,19,59,27,
            34,2,42,10,50,18,58,26,33,1,41, 9,49,17,57,25]
        self.s1 = [14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
            0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
            4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
            15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13]
        self.s2 = [15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
            3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
            0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
            13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9]
        self.s3 = [10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
            13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
            13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
            1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12]
        self.s4 = [7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
            13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
            10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
            3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14]
        self.s5 = [2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
            14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
            4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
            11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]
        self.s6 = [12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
            10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
            9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
            4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13]
        self.s7 = [4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
            13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
            1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
            6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12]
        self.s8 = [13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
            1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
            7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
            2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11]
        self.s = [self.s1, self.s2, self.s3, self.s4, self.s5, self.s6, self.s7, self.s8]
        self.leftShiftNum = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
        self.PC_1 = [57,49,41,33,25,17,9,
                    1,58,50,42,34,26,18,
                    10,2,59,51,43,35,27,
                    19,11,3,60,52,4,36,
                    63,55,47,39,31,23,15,
                    7,62,54,46,38,30,22,
                    14,6,61,53,45,37,29,
                    21,13,5,28,20,12,4]
        self.PC_2 = [14,17,11,24,1,5,
                    3,28,15,6,21,10,
                    23,19,12,4,26,8,
                    16,7,27,20,13,2,
                    41,52,31,37,47,55,
                    30,40,51,45,33,48,
                    44,49,39,56,34,53,
                    46,42,50,36,29,32]
        self.P = [16,7,20, 21,
                29,12, 28, 17,
                1, 15, 23, 26,
                5, 18, 31, 10,
                2, 8, 24, 14,
                32, 27, 3, 9,
                19, 13, 30, 6,
                22, 11, 4, 25]
        self.e = [32,1,2,3,4,5,
                4,5,6,7,8,9,
                8,9,10,11,12,13,
                12,13,14,15,16,17,
                16,17,18,19,20,21,
                20,21,22,23,24,25,
                24,25,26,27,28,29,
                28,29,30,31,32,1]
        self.subKey = []
        self.initValue = []

    def setupSignal(self):
        self.confirm.clicked.connect(self.start_daa)
        self.clear.clicked.connect(self.onClearClicked)
        self.pushButton.clicked.connect(self.saveKey)


    def onClearClicked(self):
        self.textEdit.clear()
        self.textBrowser.clear()


    #ok
    def permutate(self, block, table):
        return list(map(lambda x : block[x], table))
    
    #ok
    def string2hex(self, string):
        hex = '0123456789ABCDEF'
        bits = self.string2bits(string)
        i = 3
        num = 0
        result = ''
        for pos in range(len(bits)):
            num += bits[pos] << i
            i -= 1
            if i == -1:
                result += hex[num]
                num = 0
                i = 3
        return result

    #ok
    def hex2bits(self, hex):
        bits = []
        hexCh = '0123456789ABCDEF'
        for c in hex:
            bits.extend(self.decimal2bits(hexCh.index(c)))
        return bits

    #ok
    def string2bits(self, string):
        result = []
        data = [ord(c) for c in string]
        for ch in data:
            i = 7
            while i >= 0:
                if ch & (1 << i) != 0:
                    result.append(1)
                else:
                    result.append(0)
                i -= 1
        return result

    #ok
    def bits2string(self, bits):
        result = []
        pos = 0
        c = 0
        while pos < len(bits):
            c += bits[pos] << (7 - pos % 8)
            if pos % 8 == 7:
                result.append(chr(c))
                c = 0
            pos += 1
        return ''.join(result)


    #每一个整数要变成4位的 ok
    def decimal2bits(self, integer):
        result = [0, 0, 0, 0]
        i = 3
        while integer > 0:
            result[i] = integer % 2
            i -= 1
            integer >>= 1
        return result
            
        

    #ok
    def saveKey(self):
        key = self.lineEdit.text()
        if key:
            self.initValue = [0] * 64            
            self.subKey.clear()
            bits = self.string2bits(key)
            if len(bits) < 64:
                bits += [0] * (64 - len(bits))
            elif len(bits) > 64:
                bits = bits[:64]
            
            bits_56 = self.permutate(bits, np.array(self.PC_1)-1)

            left_key_28 = bits_56[:28]
            right_key_28 = bits_56[28:]
            for i in range(16):
                for j in range(self.leftShiftNum[i]):
                    left_key_28.append(left_key_28[0])
                    left_key_28.pop(0)

                    right_key_28.append(right_key_28[0])
                    right_key_28.pop(0)
                self.subKey.append(self.permutate(left_key_28 + right_key_28, np.array(self.PC_2)-1))



    
    def start_daa(self):
        plainText = self.textEdit.toPlainText()

        if plainText and len(self.subKey):
            textBits = self.string2bits(plainText)#正确
            result = []     
                
            if len(textBits) % 64 != 0:
                textBits.extend([0] * (64 - (len(textBits) % 64)))
            blocks = [textBits[i:i+64] for i in range(0, len(textBits), 64)]
            res = []
            res.append(self.initValue)
            for i in range(len(blocks)):
                cbc = (np.array(blocks[i]) ^ np.array(res[i])).tolist()
                res.append(self.encryption(cbc))
            res.pop(0)
            
            text = self.bits2string(res[-1])
            hexText = self.string2hex(text)
            self.textBrowser.setText(hexText)

    def addOne(self, counter):
        one = 1
        index = len(counter) - 1
        while one and index >= 0:
            one = (counter[index] + one) // 2
            counter[index] = (counter[index] + one) % 2
            index -= 1
        return counter





    def compressBlock(self, block, index):
        row = block[0] * 2 + block[5]
        col = block[1] * 8 + block[2] * 4 + block[3] * 2 + block[4]
        ind = row * 16 + col
        return self.decimal2bits(self.s[index][ind])


    def encryption(self, block):#block是64位的0-1
        permutate_block = self.permutate(block, np.array(self.IP)-1)
        left_block = permutate_block[:32]
        right_block = permutate_block[32:]
        for i in range(16):
            extand_right_block = self.permutate(right_block, np.array(self.e)-1)
            right_block_48 = (np.array(extand_right_block) ^ np.array(self.subKey[i])).tolist()
            right_block_32 = []
            for j in range(8):
                right_block_6 = right_block_48[j*6:(j+1)*6]
                right_block_4 = self.compressBlock(right_block_6, j)
                right_block_32.extend(right_block_4)
            permutate_right_block_32 = self.permutate(right_block_32, np.array(self.P)-1)
            temp_block = right_block
            right_block = (np.array(left_block) ^ np.array(permutate_right_block_32)).tolist()
            left_block = temp_block
        return self.permutate(right_block + left_block, np.array(self.invIP)-1)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    daa = DAA()
    daa.show()
    sys.exit(app.exec_())