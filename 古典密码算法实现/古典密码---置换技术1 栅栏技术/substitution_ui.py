# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'substitution.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(624, 833)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 30, 72, 15))
        self.label.setObjectName("label")
        self.textEdit_1 = QtWidgets.QTextEdit(Form)
        self.textEdit_1.setGeometry(QtCore.QRect(20, 60, 591, 121))
        self.textEdit_1.setObjectName("textEdit_1")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 210, 72, 15))
        self.label_2.setObjectName("label_2")
        self.textBrowser_1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_1.setGeometry(QtCore.QRect(20, 240, 591, 131))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 470, 72, 15))
        self.label_3.setObjectName("label_3")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 490, 581, 111))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 610, 72, 15))
        self.label_4.setObjectName("label_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 630, 581, 131))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.encry = QtWidgets.QPushButton(Form)
        self.encry.setGeometry(QtCore.QRect(30, 390, 93, 28))
        self.encry.setObjectName("encry")
        self.clear1 = QtWidgets.QPushButton(Form)
        self.clear1.setGeometry(QtCore.QRect(140, 390, 93, 28))
        self.clear1.setObjectName("clear1")
        self.decry = QtWidgets.QPushButton(Form)
        self.decry.setGeometry(QtCore.QRect(30, 780, 93, 28))
        self.decry.setObjectName("decry")
        self.clear2 = QtWidgets.QPushButton(Form)
        self.clear2.setGeometry(QtCore.QRect(150, 780, 93, 28))
        self.clear2.setObjectName("clear2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "明文"))
        self.label_2.setText(_translate("Form", "密文"))
        self.label_3.setText(_translate("Form", "密文"))
        self.label_4.setText(_translate("Form", "明文"))
        self.encry.setText(_translate("Form", "加密"))
        self.clear1.setText(_translate("Form", "清除"))
        self.decry.setText(_translate("Form", "解密"))
        self.clear2.setText(_translate("Form", "清除"))

