# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ListBookForm(object):
    def setupUi(self, ListBookForm):
        if not ListBookForm.objectName():
            ListBookForm.setObjectName(u"ListBookForm")
        ListBookForm.resize(1100, 550)
        ListBookForm.setMinimumSize(QSize(1100, 550))
        ListBookForm.setMaximumSize(QSize(1100, 550))
        self.buttsFrame = QFrame(ListBookForm)
        self.buttsFrame.setObjectName(u"buttsFrame")
        self.buttsFrame.setGeometry(QRect(80, 10, 1100, 91))
        self.buttsFrame.setMaximumSize(QSize(16777215, 16777215))
        self.buttsFrame.setFrameShape(QFrame.StyledPanel)
        self.buttsFrame.setFrameShadow(QFrame.Raised)
        self.open_new_button = QPushButton(self.buttsFrame)
        self.open_new_button.setObjectName(u"open_new_button")
        self.open_new_button.setGeometry(QRect(50, 10, 71, 51))
        self.open_new_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_new_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon = QIcon()
        icon.addFile(u"./assets/agregar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_new_button.setIcon(icon)
        self.open_new_button.setIconSize(QSize(50, 50))
        self.open_new_button.setFlat(True)
        self.label = QLabel(self.buttsFrame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 60, 91, 31))
        self.delete_book_button_2 = QPushButton(self.buttsFrame)
        self.delete_book_button_2.setObjectName(u"delete_book_button_2")
        self.delete_book_button_2.setGeometry(QRect(450, 10, 71, 51))
        self.delete_book_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.delete_book_button_2.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"./assets/eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_book_button_2.setIcon(icon1)
        self.delete_book_button_2.setIconSize(QSize(50, 50))
        self.delete_book_button_2.setFlat(True)
        self.open_edit_button = QPushButton(self.buttsFrame)
        self.open_edit_button.setObjectName(u"open_edit_button")
        self.open_edit_button.setGeometry(QRect(850, 10, 71, 51))
        self.open_edit_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.open_edit_button.setStyleSheet(u"QPushButton:hover\n"
"{\n"
"	border-style: solid;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background-color: #0069c0;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"./assets/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_edit_button.setIcon(icon2)
        self.open_edit_button.setIconSize(QSize(50, 50))
        self.open_edit_button.setFlat(True)
        self.label_2 = QLabel(self.buttsFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(440, 60, 91, 31))
        self.label_3 = QLabel(self.buttsFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(840, 60, 91, 31))
        self.frame = QFrame(ListBookForm)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 110, 941, 41))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 71, 16))
        self.searchByCombobox = QComboBox(self.frame)
        self.searchByCombobox.setObjectName(u"searchByCombobox")
        self.searchByCombobox.setGeometry(QRect(70, 10, 161, 22))
        self.parameterLineEdit = QLineEdit(self.frame)
        self.parameterLineEdit.setObjectName(u"parameterLineEdit")
        self.parameterLineEdit.setGeometry(QRect(240, 10, 411, 20))
        self.refreshButton = QPushButton(self.frame)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(800, 10, 131, 25))
        icon3 = QIcon()
        icon3.addFile(u"../../app/assets/icons/refresh-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon3)
        self.searchButton = QPushButton(self.frame)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setGeometry(QRect(660, 10, 131, 25))
        icon4 = QIcon()
        icon4.addFile(u"../../app/assets/icons/search-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon4)
        self.listBookTablet = QTableWidget(ListBookForm)
        if (self.listBookTablet.columnCount() < 1):
            self.listBookTablet.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.listBookTablet.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.listBookTablet.setObjectName(u"listBookTablet")
        self.listBookTablet.setGeometry(QRect(10, 160, 1071, 341))
        self.listBookTablet.horizontalHeader().setDefaultSectionSize(152)
        self.listBookTablet.horizontalHeader().setHighlightSections(True)
        self.listBookTablet.horizontalHeader().setProperty("showSortIndicator", True)
        self.listBookTablet.horizontalHeader().setStretchLastSection(False)
        self.listBookTablet.verticalHeader().setVisible(True)
        self.listBookTablet.verticalHeader().setCascadingSectionResizes(False)
        self.label_5 = QLabel(ListBookForm)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 510, 61, 16))
        self.bookQtyLabel = QLabel(ListBookForm)
        self.bookQtyLabel.setObjectName(u"bookQtyLabel")
        self.bookQtyLabel.setGeometry(QRect(90, 510, 41, 16))

        self.retranslateUi(ListBookForm)

        QMetaObject.connectSlotsByName(ListBookForm)
    # setupUi

    def retranslateUi(self, ListBookForm):
        ListBookForm.setWindowTitle(QCoreApplication.translate("ListBookForm", u"Gestor de articulos", None))
#if QT_CONFIG(tooltip)
        self.open_new_button.setToolTip(QCoreApplication.translate("ListBookForm", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Agregar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_new_button.setText("")
        self.label.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Agregar</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.delete_book_button_2.setToolTip(QCoreApplication.translate("ListBookForm", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Agregar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.delete_book_button_2.setText("")
#if QT_CONFIG(tooltip)
        self.open_edit_button.setToolTip(QCoreApplication.translate("ListBookForm", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">Agregar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_edit_button.setText("")
        self.label_2.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Eliminar</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Editar</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("ListBookForm", u"Buscar por: ", None))
        self.refreshButton.setText(QCoreApplication.translate("ListBookForm", u"ACTUALIZAR", None))
        self.searchButton.setText(QCoreApplication.translate("ListBookForm", u"BUSCAR", None))
        ___qtablewidgetitem = self.listBookTablet.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ListBookForm", u"asdasd", None));
        self.label_5.setText(QCoreApplication.translate("ListBookForm", u"<html><head/><body><p><span style=\" font-weight:600;\">Cantidad:</span></p></body></html>", None))
        self.bookQtyLabel.setText(QCoreApplication.translate("ListBookForm", u"##", None))
    # retranslateUi

