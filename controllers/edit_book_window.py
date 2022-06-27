from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from views.edit_book_window import EditBookForm
from db.books import select_book_by_id, update_book

class EditBookWindow(QWidget, EditBookForm):

    def __init__(self, parent=None, _id=None):
        self._id = _id
        super().__init__(parent)

        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.populate_inputs()
        self.editButton.clicked.connect(self.edit_book)


    def populate_inputs(self):
        data = select_book_by_id(self._id)
        
        self.titleLineEdit.setText(data[1])
        self.categoryLineEdit.setText(data[2])
        self.pageQtySpinBox_dos.setValue(int(data[4]))
        self.descriptionTextedit.setText(data[6])

    def check_inputs(self):
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        description_dos = self.descriptionTextedit.text()

        errors_count = 0

        if title == "": 
            print("El campo titulo es obligatorio")
            errors_count += 1

        if category == "": 
            print("El campo categoria es obligatorio")
            errors_count += 1
            
        if description_dos == "": 
            print("El campo descripcion es obligatorio")
            errors_count += 1

        if errors_count == 0:
            return True

    def edit_book(self):
        title = self.titleLineEdit.text()
        category = self.categoryLineEdit.text()
        description_dos = self.descriptionTextedit.text()
        page_qty_dos = self.pageQtySpinBox_dos.value()

        data = [title, category, page_qty_dos, description_dos]

        if self.check_inputs():
            
            if update_book(self._id, data):
                self.close()