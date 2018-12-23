#几个问题
#1.如何处理大小写的问题？ ---》都处理成大写字母
#2.如何处理不是字母的问题？ -----》不处理含有非字母的情况！---》直接将非字母去掉
#3.如何处理填充字符x或者z？ -----》填充x;注意如果同一组有两个x的话要删除一个，如果相邻两组ax，ab这样，可以确定插入了x
#4.最后是否需要加入x
#4.解密的时候如何去掉填充的字符？ ----》
from PyQt5.QtWidgets import QApplication, QWidget, QTextBrowser
import sys
from Playfair_ui import Ui_Form
import numpy as np 

class Playfair_Widget(QWidget, Ui_Form):
    def __init__(self):
        super(Playfair_Widget, self).__init__()
        self.setupUi(self)
        self.textBrowserList = []
        self.keyBox = np.array(["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]).reshape(5,5)
        for i in range(25):
            row = i / 5
            col = i % 5
            textBrowser = QTextBrowser()
            self.textBrowserList.append(textBrowser)
            self.gridLayout.addWidget(textBrowser, row, col, 1, 1)
        for i in range(25):
            r = int(i / 5)
            c = i % 5
            self.textBrowserList[i].setText(self.keyBox[c][r])
        self.setupSignal()
    
    def setupSignal(self):
        self.encryption.clicked.connect(self.onEncryptionClicked)
        self.decryption.clicked.connect(self.onDecryptionClicked)
        self.clear_1.clicked.connect(self.onClear1Clicked)
        self.clear_2.clicked.connect(self.onClear2Clicked)
        self.pushButton.clicked.connect(self.showKeyBox)

    
    def onClear1Clicked(self):
        self.lineEdit_2.clear()
        self.lineEdit_1.clear()

    def onClear2Clicked(self):
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

    def showKeyBox(self):
        keyString = self.key.text()
        soloChar = list(set(keyString))#soloChar是一个列表
        soloChar.sort(key=keyString.index)
        keys = []
        for ch in soloChar:
            if ch.isalpha():
                ch = str.upper(ch)
                keys.append(ch)
        for i in range(26):
            ch = chr(ord('A') + i)
            if ch not in keys:
                keys.append(ch)
        if 'J' in soloChar or 'j' in soloChar:
            keys.remove("I")
        else:
            keys.remove("J")

        for i in range(25):
            self.textBrowserList[i].setText(keys[i])
        self.keyBox = np.array(keys)
        self.keyBox = self.keyBox.reshape(5,5)

    
    def onEncryptionClicked(self):
        plainText = self.lineEdit_1.text()
        if plainText:
            chars = [str.upper(ch) for ch in plainText if ch.isalpha()]
            while "I" in self.keyBox and "J" in chars:
                chars[chars.index("J")] = "I"
            while "J" in self.keyBox and "I" in chars:
                chars[chars.index("I")] = "J"
            i = 0 
            while i < len(chars):
                if i + 1 < len(chars):
                    if chars[i] == chars[i+1]:
                        chars.insert(i+1, 'X')
                        i += 2
                    else:
                        i += 2
                else:
                    chars.append('X')
                    i += 2

            i = 0
            result = []
            while i < len(chars):
                ch1 = chars[i]
                ch2 = chars[i+1]

                ch1row, ch1col = np.argwhere(self.keyBox == ch1)[0]
                ch2row, ch2col = np.argwhere(self.keyBox == ch2)[0]

                #判断是否同一列
                if ch1col == ch2col:
                    ench1 = self.keyBox[(ch1row+1)%5][ch1col]
                    ench2 = self.keyBox[(ch2row+1)%5][ch2col]
                elif ch1row == ch2row:
                    ench1 = self.keyBox[ch1row][(ch1col+1)%5]
                    ench2 = self.keyBox[ch2row][(ch2col+1)%5]
                else:
                    ench1 = self.keyBox[ch1row][ch2col]
                    ench2 = self.keyBox[ch2row][ch1col]
                
                result.append(ench1)
                result.append(ench2)
                i += 2
            
            resultText = ''.join(result)
            self.lineEdit_2.setText(resultText)
        



    def onDecryptionClicked(self):
        encryptionText = self.lineEdit_3.text()
        if encryptionText:
            chars = [str.upper(ch) for ch in encryptionText if ch.isalpha()]

            while "I" in self.keyBox and "J" in chars:
                chars[chars.index("J")] = "I"
            while "J" in self.keyBox and "I" in chars:
                chars[chars.index("I")] = "J"
            
            if len(chars) % 2 == 1:
                chars.append("X")
            
            result = []
            i = 0

            while i < len(chars):
                ch1 = chars[i]
                ch2 = chars[i+1]

                ch1row, ch1col = np.argwhere(self.keyBox == ch1)[0]
                ch2row, ch2col = np.argwhere(self.keyBox == ch2)[0]

                #判断是否同一列
                if ch1col == ch2col:
                    ench1 = self.keyBox[(ch1row-1)%5][ch1col]
                    ench2 = self.keyBox[(ch2row-1)%5][ch2col]
                elif ch1row == ch2row:
                    ench1 = self.keyBox[ch1row][(ch1col-1)%5]
                    ench2 = self.keyBox[ch2row][(ch2col-1)%5]
                else:
                    ench1 = self.keyBox[ch1row][ch2col]
                    ench2 = self.keyBox[ch2row][ch1col]
                
                result.append(ench1)
                result.append(ench2)

                i += 2

            i = 0
            while i < len(result):
                if i + 2 < len(result) and result[i] == result[i+2] and result[i+1] == "X":
                    result.pop(i+1)
                    i += 1
                elif  i == len(result) - 2 and result[i+1] == "X":
                    result.pop()
                    i += 2
                elif i == len(result) - 1 and result[i] == "X":
                    result.pop()
                    i += 2
                else:
                    i += 2
            result = ''.join(result)
            self.lineEdit_4.setText(result)
            



if __name__ == "__main__":
    app = QApplication(sys.argv)
    playfair = Playfair_Widget()
    playfair.show()
    sys.exit(app.exec_())

