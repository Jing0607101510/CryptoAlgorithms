# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vigenere.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(608, 874)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 72, 15))
        self.label_2.setObjectName("label_2")
        self.textEdit_1 = QtWidgets.QTextEdit(Form)
        self.textEdit_1.setGeometry(QtCore.QRect(10, 120, 581, 111))
        self.textEdit_1.setObjectName("textEdit_1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 260, 72, 15))
        self.label_3.setObjectName("label_3")
        self.textBrowser_1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_1.setGeometry(QtCore.QRect(10, 280, 581, 141))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.encry = QtWidgets.QPushButton(Form)
        self.encry.setGeometry(QtCore.QRect(30, 440, 93, 28))
        self.encry.setObjectName("encry")
        self.clear1 = QtWidgets.QPushButton(Form)
        self.clear1.setGeometry(QtCore.QRect(170, 440, 93, 28))
        self.clear1.setObjectName("clear1")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(70, 20, 511, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 520, 581, 111))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 680, 581, 141))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 490, 72, 15))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 660, 72, 15))
        self.label_5.setObjectName("label_5")
        self.decry = QtWidgets.QPushButton(Form)
        self.decry.setGeometry(QtCore.QRect(40, 840, 93, 28))
        self.decry.setObjectName("decry")
        self.clear2 = QtWidgets.QPushButton(Form)
        self.clear2.setGeometry(QtCore.QRect(170, 840, 93, 28))
        self.clear2.setObjectName("clear2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "密钥："))
        self.label_2.setText(_translate("Form", "明文"))
        self.label_3.setText(_translate("Form", "密文"))
        self.encry.setText(_translate("Form", "加密"))
        self.clear1.setText(_translate("Form", "清除"))
        self.label_4.setText(_translate("Form", "密文"))
        self.label_5.setText(_translate("Form", "明文"))
        self.decry.setText(_translate("Form", "解密"))
        self.clear2.setText(_translate("Form", "清除"))

