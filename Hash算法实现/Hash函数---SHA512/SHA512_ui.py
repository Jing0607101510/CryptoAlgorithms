# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SHA512.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(573, 554)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 50, 72, 15))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(80, 50, 471, 361))
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 430, 72, 15))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(80, 420, 471, 61))
        self.textBrowser.setObjectName("textBrowser")
        self.confirm = QtWidgets.QPushButton(Form)
        self.confirm.setGeometry(QtCore.QRect(80, 500, 93, 28))
        self.confirm.setObjectName("confirm")
        self.clear = QtWidgets.QPushButton(Form)
        self.clear.setGeometry(QtCore.QRect(200, 500, 93, 28))
        self.clear.setObjectName("clear")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "文本"))
        self.label_2.setText(_translate("Form", "HASH值"))
        self.confirm.setText(_translate("Form", "确定"))
        self.clear.setText(_translate("Form", "清除"))

