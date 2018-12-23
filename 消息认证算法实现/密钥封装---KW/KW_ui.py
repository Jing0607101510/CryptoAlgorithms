# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KW.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(655, 901)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 161, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 511, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(550, 50, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 141, 16))
        self.label_2.setObjectName("label_2")
        self.textEdit_1 = QtWidgets.QTextEdit(Form)
        self.textEdit_1.setGeometry(QtCore.QRect(30, 140, 611, 121))
        self.textEdit_1.setObjectName("textEdit_1")
        self.textBrowser_1 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_1.setGeometry(QtCore.QRect(30, 320, 611, 121))
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 290, 141, 16))
        self.label_3.setObjectName("label_3")
        self.en = QtWidgets.QPushButton(Form)
        self.en.setGeometry(QtCore.QRect(40, 460, 93, 28))
        self.en.setObjectName("en")
        self.clear1 = QtWidgets.QPushButton(Form)
        self.clear1.setGeometry(QtCore.QRect(160, 460, 93, 28))
        self.clear1.setObjectName("clear1")
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 100, 651, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 500, 651, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(31, 530, 151, 20))
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(Form)
        self.textEdit_2.setGeometry(QtCore.QRect(30, 560, 601, 111))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(30, 690, 111, 16))
        self.label_5.setObjectName("label_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 710, 601, 121))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.de = QtWidgets.QPushButton(Form)
        self.de.setGeometry(QtCore.QRect(40, 850, 93, 28))
        self.de.setObjectName("de")
        self.clear2 = QtWidgets.QPushButton(Form)
        self.clear2.setGeometry(QtCore.QRect(160, 850, 93, 28))
        self.clear2.setObjectName("clear2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "密钥加密密钥："))
        self.pushButton.setText(_translate("Form", "确定"))
        self.label_2.setText(_translate("Form", "需要封装的密钥："))
        self.label_3.setText(_translate("Form", "封装后的密钥："))
        self.en.setText(_translate("Form", "封装"))
        self.clear1.setText(_translate("Form", "清除"))
        self.label_4.setText(_translate("Form", "被封装的密钥："))
        self.label_5.setText(_translate("Form", "解封后的密钥："))
        self.de.setText(_translate("Form", "解封"))
        self.clear2.setText(_translate("Form", "清除"))

