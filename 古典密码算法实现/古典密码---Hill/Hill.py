from PyQt5.QtWidgets import QApplication, QWidget
import sys
import numpy as np 
from Hill_ui import Ui_Form

class Hill_Widget(QWidget, Ui_Form):
    def __init__(self):
        super(Hill_Widget, self).__init__()
        self.setupUi(self)
        self.setupSignal()
        self.Mat = np.mat([[17, 17, 5], [21, 18, 21], [2, 2, 19]])
        self.invMat = np.mat([[4, 9, 15], [15, 17, 6], [24, 0, 17]])
        self.len = 3

    def setupSignal(self):
        self.clear_1.clicked.connect(self.onClear1Clicked)
        self.clear_2.clicked.connect(self.onClear2Clicked)
        self.encryption_1.clicked.connect(self.onEncryptionClicked)
        self.decryption_2.clicked.connect(self.onDecryptionClicked)
    
    def onClear1Clicked(self):
        self.lineEdit_1.clear()
        self.lineEdit_2.clear()
    
    def onClear2Clicked(self):
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()

    def onEncryptionClicked(self):
        plainText = self.lineEdit_1.text()
        if plainText:
            chars = [str.upper(ch) for ch in plainText if ch.isalpha()]
            if len(chars) % 3 != 0:
                s = 3 - len(chars) % 3
                chars.extend(["A"] * s)
            charNum = []
            for c in chars:
                charNum.append((ord(c)-ord("A")) % 26)
            charGroup = [charNum[i: i+3] for i in range(0, len(charNum), self.len)]
            charGroup = np.mat(charGroup)

            encryptionText = (np.dot(charGroup, self.Mat)) % 26
            encryptionText = encryptionText.reshape(1, encryptionText.size).A[0].tolist()
            plainText = []

            for num in encryptionText:
                plainText.append(chr(num+ord("A")))
            encryptionText = ''.join(plainText)
            self.lineEdit_2.setText(encryptionText)
    
    def onDecryptionClicked(self):
        enText = self.lineEdit_3.text()
        if enText:
            chars = [str.upper(ch) for ch in enText if ch.isalpha()]
            if len(chars) % 3 != 0:
                chars.extend(["A"] * (3 - len(chars) % 3))
            charNum = []
            for c in chars:
                charNum.append((ord(c) - ord("A"))%26)
            charGroup = [charNum[i:i+3] for i in range(0, len(charNum), self.len)]
            charGroup = np.mat(charGroup)

            decryptionText = (np.dot(charGroup, self.invMat)) % 26
            decryptionText = decryptionText.reshape(1, decryptionText.size).A[0].tolist()
            plainText = []
            for num in decryptionText:
                plainText.append(chr(num + ord("A")))
            plainText = ''.join(plainText)
            self.lineEdit_4.setText(plainText)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    hill = Hill_Widget()
    hill.show()
    sys.exit(app.exec_())