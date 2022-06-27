# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_book_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class EditBookForm(object):
    def setupUi(self, EditBookWindow):
        if not EditBookWindow.objectName():
            EditBookWindow.setObjectName(u"EditBookWindow")
        EditBookWindow.resize(405, 376)
        self.label = QLabel(EditBookWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 381, 20))
        self.label.setFrameShape(QFrame.Box)
        self.label_2 = QLabel(EditBookWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 60, 61, 13))
        self.titleLineEdit = QLineEdit(EditBookWindow)
        self.titleLineEdit.setObjectName(u"titleLineEdit")
        self.titleLineEdit.setGeometry(QRect(30, 80, 351, 20))
        self.label_3 = QLabel(EditBookWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 61, 13))
        self.categoryLineEdit = QLineEdit(EditBookWindow)
        self.categoryLineEdit.setObjectName(u"categoryLineEdit")
        self.categoryLineEdit.setGeometry(QRect(30, 130, 271, 20))
        self.label_4 = QLabel(EditBookWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 160, 111, 16))
        self.pageQtySpinBox_dos = QSpinBox(EditBookWindow)
        self.pageQtySpinBox_dos.setObjectName(u"pageQtySpinBox_dos")
        self.pageQtySpinBox_dos.setGeometry(QRect(30, 180, 111, 22))
        self.pageQtySpinBox_dos.setMaximum(10000)
        self.label_5 = QLabel(EditBookWindow)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 220, 121, 16))
        self.descriptionTextedit = QLineEdit(EditBookWindow)
        self.descriptionTextedit.setObjectName(u"descriptionTextedit")
        self.descriptionTextedit.setGeometry(QRect(30, 240, 191, 21))
        self.editButton = QPushButton(EditBookWindow)
        self.editButton.setObjectName(u"editButton")
        self.editButton.setGeometry(QRect(150, 330, 101, 31))
        self.editButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.editButton.setStyleSheet(u"QpushButton \n"
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

        self.retranslateUi(EditBookWindow)

        QMetaObject.connectSlotsByName(EditBookWindow)
    # setupUi

    def retranslateUi(self, EditBookWindow):
        EditBookWindow.setWindowTitle(QCoreApplication.translate("EditBookWindow", u"Editar Producto", None))
        self.label.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Editar Producto</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Producto:</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Tipo:</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Cantidad de salida: </span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("EditBookWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Fecha de salida:</span></p></body></html>", None))
        self.editButton.setText(QCoreApplication.translate("EditBookWindow", u"Agregar", None))
    # retranslateUi

