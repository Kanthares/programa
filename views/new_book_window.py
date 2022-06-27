# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_book_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class NewbookForm(object):
    def setupUi(self, NewbookWindow):
        if not NewbookWindow.objectName():
            NewbookWindow.setObjectName(u"NewbookWindow")
        NewbookWindow.resize(405, 379)
        self.label = QLabel(NewbookWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(NewbookWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.tittleLineEdit = QLineEdit(NewbookWindow)
        self.tittleLineEdit.setObjectName(u"tittleLineEdit")
        self.tittleLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(NewbookWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 13))
        self.categoryLineEdit = QLineEdit(NewbookWindow)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(30, 130, 271, 20))
        self.label_4 = QLabel(NewbookWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 131, 16))
        self.pageQtySpinBox = QSpinBox(NewbookWindow)
        self.pageQtySpinBox.setObjectName(u"pageQtySpinBox")
        self.pageQtySpinBox.setGeometry(QRect(30, 180, 121, 22))
        self.pageQtySpinBox.setMaximum(10000)
        self.label_5 = QLabel(NewbookWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 220, 111, 16))
        self.descriptionTextEdit_3 = QLineEdit(NewbookWindow)
        self.descriptionTextEdit_3.setObjectName(u"descriptionTextEdit_3")
        self.descriptionTextEdit_3.setGeometry(QRect(30, 240, 131, 21))
        self.addButton = QPushButton(NewbookWindow)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(160, 330, 101, 31))
        self.addButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.addButton.setStyleSheet(u"QpushButton \n"
"{\n"
"	height: 2em;\n"
"	border-style: solid;\n"
"	border-width: 2px;\n"
"	border-color: #0069c0;\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	backgroud-color: #0069c0;\n"
"	color: green;\n"
"}")

        self.retranslateUi(NewbookWindow)

        QMetaObject.connectSlotsByName(NewbookWindow)
    # setupUi

    def retranslateUi(self, NewbookWindow):
        NewbookWindow.setWindowTitle(QCoreApplication.translate("NewbookWindow", u"Nuevo Producto", None))
        self.label.setText(QCoreApplication.translate("NewbookWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Nuevo Producto</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("NewbookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Producto:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("NewbookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Tipo:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("NewbookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Cantidad de entrada: </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("NewbookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Fecha de entrada:</span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("NewbookWindow", u"Agregar", None))
    # retranslateUi

