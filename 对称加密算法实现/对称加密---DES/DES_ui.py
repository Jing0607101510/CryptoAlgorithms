# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DES.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(752, 595)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.label.setObjectName("label")
        self.key = QtWidgets.QLineEdit(Form)
        self.key.setGeometry(QtCore.QRect(60, 20, 611, 31))
        self.key.setObjectName("key")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 72, 15))
        self.label_2.setObjectName("label_2")
        self.textEdit_1 = QtWidgets.QTextEdit(Form)
        self.textEdit_1.setGeometry(QtCore.QRect(60, 80, 681, 81))
        self.textEdit_1.setObjectName("textEdit_1")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(680, 20, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 60, 741, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 200, 72, 15))
        self.label_3.setObjectName("label_3")
        self.textBrowser_1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_1.setGeometry(QtCore.QRect(60, 190, 681, 81))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 320, 751, 21))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.encry = QtWidgets.QPushButton(Form)
        self.encry.setGeometry(QtCore.QRect(60, 290, 93, 28))
        self.encry.setObjectName("encry")
        self.clear_1 = QtWidgets.QPushButton(Form)
        self.clear_1.setGeometry(QtCore.QRect(170, 290, 93, 28))
        self.clear_1.setObjectName("clear_1")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 350, 72, 15))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 340, 681, 87))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 440, 72, 15))
        self.label_5.setObjectName("label_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 440, 681, 101))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.decry = QtWidgets.QPushButton(Form)
        self.decry.setGeometry(QtCore.QRect(60, 550, 93, 28))
        self.decry.setObjectName("decry")
        self.clear_2 = QtWidgets.QPushButton(Form)
        self.clear_2.setGeometry(QtCore.QRect(170, 550, 93, 28))
        self.clear_2.setObjectName("clear_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "密钥"))
        self.label_2.setText(_translate("Form", "明文"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.label_3.setText(_translate("Form", "密文"))
        self.encry.setText(_translate("Form", "加密"))
        self.clear_1.setText(_translate("Form", "清除"))
        self.label_4.setText(_translate("Form", "密文"))
        self.label_5.setText(_translate("Form", "明文"))
        self.decry.setText(_translate("Form", "解密"))
        self.clear_2.setText(_translate("Form", "清除"))

