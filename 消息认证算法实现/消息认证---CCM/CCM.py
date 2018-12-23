from PyQt5.QtWidgets import QApplication, QWidget 
import sys
from CCM_ui import Ui_Form
import numpy as np
import copy

class CCM(QWidget, Ui_Form):
    def __init__(self):
        super(CCM, self).__init__()
        self.setupUi(self)
        self.setupSignal()
        self.setupData()
    
    def setupData(self):
        self.S = [
            0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
            0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
            0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
            0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
            0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
            0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
            0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
            0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
            0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
            0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
            0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
            0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
            0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
            0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
            0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
            0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
        ]
        self.invS = [
            0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
            0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
            0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
            0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
            0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
            0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
            0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
            0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
            0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
            0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
            0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
            0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
            0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
            0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
            0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
            0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
        ]
        #ok
        self.ConfusionMat = np.array([
            [0x02, 0x03, 0x01, 0x01],
            [0x01, 0x02, 0x03, 0x01],
            [0x01, 0x01, 0x02, 0x03],
            [0x03, 0x01, 0x01, 0x02]
        ])
        self.invConfusionMat = np.array([
            [0x0e, 0x0b, 0x0d, 0x09],
            [0x09, 0x0e, 0x0b, 0x0d],
            [0x0d, 0x09, 0x0e, 0x0b],
            [0x0b, 0x0d, 0x09, 0x0e]
        ])
        self.Rcon = [0x01, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00,
            0x04, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00,
            0x10, 0x00, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00,
            0x40, 0x00, 0x00, 0x00, 0x80, 0x00, 0x00, 0x00,
            0x1b, 0x00, 0x00, 0x00, 0x36, 0x00, 0x00, 0x00
            ]
        self.subKey = []


    def setupSignal(self):
        self.encry.clicked.connect(self.onEncryptionClicked)
        self.decry.clicked.connect(self.onDecryptionClicked)
        self.clear1.clicked.connect(self.onClear1Clicked)
        self.clear2.clicked.connect(self.onClear2Clicked)
        self.pushButton.clicked.connect(self.saveKey)


    def onEncryptionClicked(self):
        text = self.textEdit_1.toPlainText()
        relate = self.relate_line.text()
        if text and len(self.subKey) and relate:

            cmac_res = self.start_cmac(self.temp + relate + text) #就选128位作为消息验证码的长度
            cmac = []
            i = 0
            while i < len(cmac_res):
                cmac.append(int(cmac_res[i:i+2], 16))
                i += 2
            encry_counter = self.encryption(self.CTR0)  
            res = (np.array(encry_counter) ^ np.array(cmac)).tolist()

            textBits = self.string2int(text)#正确
            result = []
            flag = 0
            if len(textBits) % 16 != 0:
                flag = 16 - (len(textBits) % 16)
                textBits.extend([0] * flag) 
                     
            #如果flag=1则最后一个分组是不完整的             
            blocks = [textBits[i:i+16] for i in range(0, len(textBits), 16)]
            counter = self.CTR0
            counter = self.addOne(counter)
            for block in blocks:
                encry_counter = self.encryption(counter)
                result.extend((np.array(encry_counter) ^ np.array(block)).tolist())
                counter = self.addOne(counter)
            while flag:
                result.pop()
                flag -= 1
            result.extend(res)
            
            enText = self.int2hex(result)
            ccm_code = self.int2hex(res)
            self.textBrowser_2.setText(enText)
            self.textBrowser_1.setText(ccm_code)


    def onDecryptionClicked(self):
        enText = self.textEdit_2.toPlainText()
        relate = self.relate_line.text()
        if enText and len(self.subKey):
            enText, ccm_code = enText[:-32], enText[-32:]

            self.textBrowser_3.setText(ccm_code)

            textBits = self.hex2int(enText)
            result = []
            
            flag = 0
            if len(textBits) % 16 != 0:
                flag = 16 - len(textBits) % 16
                textBits.extend([0] * (16 - len(textBits) % 16))

            blocks = [textBits[i: i+16] for i in range(0, len(textBits), 16)]
            counter = self.CTR0
            counter = self.addOne(counter)
            for block in blocks:
                encry_counter = self.encryption(counter)
                result.extend((np.array(encry_counter) ^ np.array(block)).tolist())
                counter = self.addOne(counter)
            
            while flag:
                result.pop()
                flag -= 1
            
            plainText = self.int2string(result)

            cmac_res = self.start_cmac(self.temp + relate + plainText) #就选128位作为消息验证码的长度
            cmac = []
            i = 0
            while i < len(cmac_res):
                cmac.append(int(cmac_res[i:i+2], 16))
                i += 2
            encry_counter = self.encryption(self.CTR0)  
            res = (np.array(encry_counter) ^ np.array(cmac)).tolist()
            new_ccm_code = self.int2hex(res)
            self.textBrowser_5.setText(plainText)
            self.textBrowser_4.setText(new_ccm_code)
            if new_ccm_code == ccm_code:
                self.textBrowser_6.setText("Yes!")
            else:
                self.textBrowser_6.setText("No!")
    
    def decryption(self, block):
        block = (np.array(block) ^ np.array(self.subKey[10])).tolist()#初始的轮密钥加
        for i in range(9, -1, -1):
            block_piece = [block[j:j+4] for j in range(0, len(block), 4)]
            for j in range(4):#逆向行移位
                for k in range(j):
                    block_piece[j].insert(0, block_piece[j].pop())
            block = []
            for piece in block_piece:
                block.extend(piece)
            s_block = self.s_premutate(block, type=2)#16字节#逆向字节替代
            s_block = (np.array(s_block) ^ np.array(self.subKey[i])).tolist()#轮密相加
            block = s_block
            if i != 0:                
            #列混淆
                s_block_piece = [s_block[j:j+4] for j in range(0, len(block), 4)]
                s_block_piece = np.array(s_block_piece)#s_block_piece是矩阵形式
                s_block_piece = self.colConfusion(s_block_piece, self.invConfusionMat)
                s_block_piece = (s_block_piece.reshape(1, s_block_piece.size)[0]).tolist()#矩阵形式reshape
                block = s_block_piece
        return block



    def onClear1Clicked(self):
        self.relate_line.clear()
        self.textEdit_1.clear()
        self.textBrowser_1.clear()
        self.textBrowser_2.clear()
    
    def onClear2Clicked(self):
        self.textEdit_2.clear()
        self.textBrowser_3.clear()
        self.textBrowser_4.clear()
        self.textBrowser_5.clear()

    
    #直接是字符转为16/10进制的数
    def string2int(self, string):
        result = []
        for c in string:
            result.append(ord(c))
        return result

    def int2string(self, ints):
        result = []
        for i in ints:
            result.append(chr(i))
        return ''.join(result)
    #ok
    def int2hex(self, ints):#hex是string类型
        hex = "0123456789ABCDEF"
        result = []
        for int in ints:
            high = (int&0xF0) >> 4
            low = int & 0x0F
            highHex = hex[high]
            lowHex = hex[low]
            result.append(highHex)
            result.append(lowHex)
        return ''.join(result)
    
    #ok
    def hex2int(self, hexString):
        hex = "0123456789ABCDEF"
        result = []
        i = 0
        while i < len(hexString):
            high = hex.index(hexString[i])
            low = hex.index(hexString[i+1])
            result.append((high << 4) | (low))
            i += 2
        return result


    def T(self, preKey, index):
        preKey_4th = preKey #只是一个字的长度 4个字节
        preKey_4th.append(preKey_4th.pop(0))#左循环移动一位
        s_preKey_4th = self.s_premutate(preKey_4th) #4个字节
        Rcon = self.Rcon[index*4:(index+1)*4]
        result = (np.array(s_preKey_4th) ^ np.array(Rcon)).tolist()
        return result

    def s_premutate(self, bytes, type=1):#对每一个字节进行s盒替换
        result = []
        for byte in bytes:
            #row = (byte >> 4) & 0x0f
            #col = byte & (0x0f)
            #locate = row * 16 + col
            if type == 1:
                result.append(self.S[byte])
            else:
                result.append(self.invS[byte])
        return result

    def addOne(self, counter):
        one = 1
        index = len(counter) - 1
        while one and index >= 0:
            one = (counter[index] + one) // (2^8)
            counter[index] = (counter[index] + one) % (2^8)
            index -= 1
        return counter


    def saveKey(self):
        key = self.key_line.text()
        CTR0 = self.crt_line.text()
        temp = self.temp_line.text()
        if key and CTR0 and temp:
            self.subKey.clear()
            initKey = self.string2int(key)
            if len(initKey) > 16:
                initKey = initKey[:16]
            elif len(initKey) < 16:
                initKey.extend([0] * (16 - len(initKey)))
            self.subKey.append(initKey)

            # i+1 #每一轮的key是是个独立的list
            for i in range(10):
                preKey = self.subKey[i]#preKey是16个字节
                curKey = []#也应该是16个字节
                for j in range(4):
                    if j == 0:                        
                        t_preKey_4th = self.T(preKey[12:16], i)#是一个字，4字节
                        curKey.extend((np.array(preKey[0:4])^np.array(t_preKey_4th)).tolist())
                    else:#字与字异或得到下一个字
                        xor_result = (np.array(curKey[(j-1)*4:j*4])^np.array(preKey[j*4:(j+1)*4])).tolist()
                        curKey.extend(xor_result)
                self.subKey.append(curKey)
            
            L = self.encryption([0] * 16)#包括16个数字的列表
            flag = 0
            flag1 = 0
            if L[0] & 0x80 == 0:
                flag = 1
            if L[0] & 0x40 == 0:
                flag1 = 1
            l = ''
            for ll in L:
                l += "%02x"%(ll)
            L = int(l, 16)
            if flag:
                self.Key1 = (L << 1) & 0xffffffffffffffffffffffffffffffff#128位
            else:
                self.Key1 = ((L << 1) | (0x87)) & 0xffffffffffffffffffffffffffffffff
            if flag1:
                self.Key2 = (self.Key1 << 1) & 0xffffffffffffffffffffffffffffffff
            else:
                self.Key2 = ((self.Key1 << 1) | (0x87)) & 0xffffffffffffffffffffffffffffffff
            self.temp1 = "%032x"%self.Key1
            self.temp2 = "%032x"%self.Key2
            self.Key1 = []
            self.Key2 = []
            i = 0
            while i < len(self.temp1):
                self.Key1.append(int(self.temp1[i:i+2], 16))
                self.Key2.append(int(self.temp2[i:i+2], 16))
                i += 2
            
            self.temp = temp#字符串
            self.CTR0 = self.string2int(CTR0)#整数
            if len(self.CTR0) > 16:
                self.CTR0 = self.CTR0[:16]
            elif len(self.CTR0) < 16:
                self.CTR0.extend([0] * (16 - len(self.CTR0)))





    #ok
    def start_cmac(self, text):
        ints = self.string2int(text)
        flag = 0
        if len(ints) % 16 != 0:
            ints.extend([0]*(16-len(ints)%16))
            flag = 1
        blocks = [ints[i: i+16] for i in range(0, len(ints), 16)]#分成128位的块#类型是整数
        result = [[0]*16]
        for i in range(len(blocks)-1):
            result.append(self.encryption((np.array(blocks[i]) ^ np.array(result[i])).tolist()))#字节列表
        if flag == 0:
            result = self.encryption((np.array(blocks[len(blocks)-1]) ^ np.array(result[len(blocks)-1]) ^ np.array(self.Key1)).tolist())
        else:
            result = self.encryption((np.array(blocks[len(blocks)-1]) ^ np.array(result[len(blocks)-1]) ^ np.array(self.Key2)).tolist())
        enText = self.int2hex(result)
        return enText#字符串


    #对每一个128位，即16字节
    def encryption(self, block):#block是整形
        block = (np.array(block) ^ np.array(self.subKey[0])).tolist()#初始的轮密钥加
        for i in range(10):
            s_block = self.s_premutate(block)#16字节
            s_block_piece = [s_block[j:j+4] for j in range(0, len(s_block), 4)]
            for j in range(4):#行移位
                for k in range(j):
                    s_block_piece[j].append(s_block_piece[j].pop(0))
            #列混淆
            s_block_piece = np.array(s_block_piece)#s_block_piece是矩阵形式
            if i != 9:
                s_block_piece = self.colConfusion(s_block_piece, self.ConfusionMat)
            s_block_piece = s_block_piece.reshape(1, s_block_piece.size)[0]#矩阵形式reshape
            block = (s_block_piece ^ np.array(self.subKey[i+1])).tolist()
        return block

    
    def colConfusion(self, block, confusionMat):#block是一个矩阵4*4矩阵每一行4个字节,confusionMat是4*4矩阵
        result = []
        for i in range(4):#是confusionMat的每一行
            res_1 = []
            for j in range(4):#block的每一列
                res = self.matProduct(confusionMat[i], block[:,j])
                res_1.append(res)
            result.append(res_1)
        return np.array(result)
    

    def matProduct(self, row, col):#两个都是行向量
        ans = 0
        for i in range(len(row)):
            temp = self.byteProduct(row[i], col[i])
            ans ^= self.byteProduct(row[i], col[i])
        return ans
        
    def byteProduct(self, w, x):#单个数
        if w == 2:
            return self.GFMul2(x)
        elif w == 1:
            return x
        elif w == 3:
            return self.GFMul3(x)
        elif w == 9:
            return self.GFMul9(x)
        elif w == 11:
            return self.GFMulB(x)
        elif w == 13:
            return self.GFMulD(x)
        elif w == 14:
            return self.GFMulE(x)
    
    
    def GFMul2(self, x):
        if x & (0x80) != 0:
            return ((x << 1) & (0xff)) ^ (0x1b)
        else:
            return (x << 1) & (0xff)
    
    def GFMul3(self, x):
        return self.GFMul2(x) ^ x

    #错在不是单纯的加/异或
    def GFMul9(self, x):
        return self.GFMul2(self.GFMul2(self.GFMul2(x))) ^ x

    def GFMulB(self, x):
        return self.GFMul9(x) ^ self.GFMul2(x)

    def GFMulD(self, x):
        return self.GFMul9(x) ^ self.GFMul2(self.GFMul2(x))#就像是二进制一样

    def GFMulE(self, x):
        return self.GFMul2(self.GFMul2(self.GFMul2(x))) ^ self.GFMul2(self.GFMul2(x)) ^ self.GFMul2(x)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ccm = CCM()
    ccm.show()
    sys.exit(app.exec_())