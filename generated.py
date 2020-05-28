# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(282, 197)
        self.min = QtWidgets.QLCDNumber(Form)
        self.min.setGeometry(QtCore.QRect(10, 80, 81, 41))
        self.min.setStyleSheet("border: none;\n"
"color: green;")
        self.min.setObjectName("min")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 21, 41))
        self.label_2.setStyleSheet("font: 75 14pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.sec = QtWidgets.QLCDNumber(Form)
        self.sec.setGeometry(QtCore.QRect(80, 80, 81, 41))
        self.sec.setMinimumSize(QtCore.QSize(81, 0))
        self.sec.setStyleSheet("border: none;\n"
"color: green;\n"
"")
        self.sec.setObjectName("sec")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(170, 80, 51, 41))
        self.label_3.setStyleSheet("font: 75 14pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 201, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.dao = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.dao.setObjectName("dao")
        self.horizontalLayout.addWidget(self.dao)
        self.zheng = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.zheng.setObjectName("zheng")
        self.horizontalLayout.addWidget(self.zheng)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 140, 201, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.start.setObjectName("start")
        self.horizontalLayout_2.addWidget(self.start)
        self.stop = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.stop.setObjectName("stop")
        self.horizontalLayout_2.addWidget(self.stop)
        self.setzero = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.setzero.setObjectName("setzero")
        self.horizontalLayout_2.addWidget(self.setzero)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "分"))
        self.label_3.setText(_translate("Form", "秒"))
        self.dao.setText(_translate("Form", "倒计时"))
        self.zheng.setText(_translate("Form", "正计时"))
        self.start.setText(_translate("Form", "开始"))
        self.stop.setText(_translate("Form", "暂停"))
        self.setzero.setText(_translate("Form", "清零"))
