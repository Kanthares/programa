from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.new_book_window import NewbookForm
from db.books import insert_book
import shutil
import os

class NewbookWindow(QWidget, NewbookForm):

    def __init__(self, parent=None):
        super().__init__(parent) 
        
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.addButton.clicked.connect(self.add_book)
    
    def check_inputs(self):
        title = self.tittleLineEdit.text()
        category = self.categoryLineEdit.text()
        page_qty_uno = self.pageQtySpinBox.value()
        description = self.descriptionTextEdit_3.text()

        errors_count = 0

        if title == "": 
            print("El campo titulo es obligatorio")
            errors_count += 1

        if category == "": 
            print("El campo categoria es obligatorio")
            errors_count += 1
            
        if description == "": 
            print("El campo descripcion es obligatorio")
            errors_count += 1

        if page_qty_uno == 0:
            print("El campo cantidad es obligatorio")
            errors_count +=1

        if errors_count == 0:
            return True

    def add_book(self):
        title = self.tittleLineEdit.text()
        page_qty_uno = self.pageQtySpinBox.value()
        category = self.categoryLineEdit.text()
        description = self.descriptionTextEdit_3.text()

        if self.check_inputs():
            data = (title, category,  page_qty_uno, description)
            if insert_book(data):
                self.clean_inputs()
            else:
                print("Error")
    
    def clean_inputs(self):
        self.tittleLineEdit.clear()
        self.categoryLineEdit.clear()
        self.pageQtySpinBox.setValue(0)
        self.descriptionTextEdit_3.clear()