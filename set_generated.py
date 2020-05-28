# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'set.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(326, 133)
        Dialog.setStyleSheet(u"font-size: 16px;\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 10, 121, 31))
        self.label.setStyleSheet(u"width: 200px;\n"
"")
        self.set_min = QSpinBox(Dialog)
        self.set_min.setObjectName(u"set_min")
        self.set_min.setGeometry(QRect(80, 50, 42, 22))
        self.set_sec = QSpinBox(Dialog)
        self.set_sec.setObjectName(u"set_sec")
        self.set_sec.setGeometry(QRect(160, 50, 42, 22))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 50, 21, 21))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 50, 54, 20))
        self.ok = QPushButton(Dialog)
        self.ok.setObjectName(u"ok")
        self.ok.setGeometry(QRect(50, 90, 75, 31))
        self.cancel = QPushButton(Dialog)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setGeometry(QRect(170, 90, 75, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u8bbe\u7f6e\u5012\u8ba1\u65f6\u65f6\u95f4", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u5206", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u79d2", None))
        self.ok.setText(QCoreApplication.translate("Dialog", u"\u5b8c\u6210", None))
        self.cancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

