# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GCM.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(663, 800)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 72, 15))
        self.label.setObjectName("label")
        self.key_line = QtWidgets.QLineEdit(Form)
        self.key_line.setGeometry(QtCore.QRect(70, 10, 461, 31))
        self.key_line.setObjectName("key_line")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 72, 15))
        self.label_2.setObjectName("label_2")
        self.textEdit_1 = QtWidgets.QTextEdit(Form)
        self.textEdit_1.setGeometry(QtCore.QRect(70, 200, 531, 201))
        self.textEdit_1.setObjectName("textEdit_1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 420, 131, 16))
        self.label_3.setObjectName("label_3")
        self.textBrowser_1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_1.setGeometry(QtCore.QRect(60, 450, 531, 91))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.encry = QtWidgets.QPushButton(Form)
        self.encry.setGeometry(QtCore.QRect(70, 760, 93, 28))
        self.encry.setObjectName("encry")
        self.clear1 = QtWidgets.QPushButton(Form)
        self.clear1.setGeometry(QtCore.QRect(180, 760, 93, 28))
        self.clear1.setObjectName("clear1")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 30, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 72, 15))
        self.label_4.setObjectName("label_4")
        self.IV_line = QtWidgets.QLineEdit(Form)
        self.IV_line.setGeometry(QtCore.QRect(70, 50, 461, 31))
        self.IV_line.setObjectName("IV_line")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 121, 16))
        self.label_6.setObjectName("label_6")
        self.relate_line = QtWidgets.QLineEdit(Form)
        self.relate_line.setGeometry(QtCore.QRect(140, 130, 451, 31))
        self.relate_line.setObjectName("relate_line")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(60, 580, 531, 161))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 550, 171, 16))
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 100, 661, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "密钥："))
        self.label_2.setText(_translate("Form", "消息："))
        self.label_3.setText(_translate("Form", "GCM消息认证码："))
        self.encry.setText(_translate("Form", "加密"))
        self.clear1.setText(_translate("Form", "清除"))
        self.pushButton.setText(_translate("Form", "确定"))
        self.label_4.setText(_translate("Form", "IV:"))
        self.label_6.setText(_translate("Form", "附加认证信息："))
        self.label_7.setText(_translate("Form", "包括消息认证码的密文："))

