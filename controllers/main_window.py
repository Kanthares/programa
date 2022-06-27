from PySide2.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView
from views.main_window import ListBookForm
from db.books import select_all_books, select_book_by_title, select_book_by_category, delete_book

class ListBookWindow(QWidget, ListBookForm):

    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.open_new_button.clicked.connect(self.open_new_book_window)
        self.open_edit_button.clicked.connect(self.open_edit_window)
        self.table_config()
        self.populate_combobox()
        self.populate_table(select_all_books())
        self.refreshButton.clicked.connect( lambda: self.populate_table(select_all_books()))
        self.searchButton.clicked.connect(self.search)
        self.delete_book_button_2.clicked.connect(self.remove_book)

    def open_new_book_window(self):
        from controllers.new_book_window import NewbookWindow
        window = NewbookWindow(self)
        window.show()

    def open_edit_window(self):
        from controllers.edit_book_window import EditBookWindow
        selected_row = self.listBookTablet.selectedItems()

        if selected_row:
            book_id = int(selected_row[0].text())
            window = EditBookWindow(self, book_id)
            window.show()

        self.listBookTablet.clearSelection()

    def remove_book(self):
        selected_row = self.listBookTablet.selectedItems()

        if selected_row:
            book_id = int(selected_row[0].text())
            row = selected_row[0].row()

            if delete_book(book_id):
               self.listBookTablet.removeRow(row)
            
        self.records_qty()
    
    def table_config(self):
        column_headers = ("ID","Producto", "Categoria",  "Cantidad de entrada", "Cantidad de salida", "Fecha de entrada", "Fecha de salida")
        self.listBookTablet.setColumnCount(len(column_headers))
        self.listBookTablet.setHorizontalHeaderLabels(column_headers)

        self.listBookTablet.setSelectionBehavior(QAbstractItemView.SelectRows)


    def populate_table(self, data):
        self.listBookTablet.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.listBookTablet.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
        self.records_qty()

    def add_new_book_row(self, data):
        qty_rows = self.listBookTablet.rowCount()
        index_row = qty_rows
        qty_rows += 1
        self.listBookTablet.setRowCount(qty_rows)
   
        for (index_cell, cell) in enumerate(data):
            self.listBookTablet.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def search_book_by_title(self, title):
        data = select_book_by_title(title)

        self.populate_table(data)


    def populate_combobox(self):
        cb_options = ("","Producto", "Categoria")
        self.searchByCombobox.addItems(cb_options)

    def search_book_by_category(self, category):
        data = select_book_by_category(category)

        self.populate_table(data)

    def search(self):
        option_selected = self.searchByCombobox.currentText()
        parameter = self.parameterLineEdit.text()

        if option_selected == "":
            print("Debe seleccionar una opcion")
        else:
            if parameter == "":
                print("Debe escribir lo que desea consultar")
            else:
                if option_selected == "Titulo":
                    self.search_book_by_title(parameter)
                elif option_selected == "Categoria":
                    self.search_book_by_category(parameter)

            self.records_qty()

    def records_qty(self):
        qty_rows = str(self.listBookTablet.rowCount())
        self.bookQtyLabel.setText(qty_rows)