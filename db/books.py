from sqlite3 import Error
from .connection import create_connection

def insert_book(data):
    conn = create_connection()
    sql = """ INSERT INTO books ( tittle, category, page_qty_uno, description) 
                VALUES(?, ?, ?, ?)
    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Nuevos datos agregados")
        return True, cur.lastrowid

    except Error as e:
        print ("Error de insercion" + str(e))
        return False
        
    finally:
        if conn:
            cur.close()
            conn.close()

def update_book(_id, data):
    conn = create_connection()

    sql = f""" UPDATE books SET
                                tittle = ?,
                                category = ?,
                                page_qty_dos = ?,
                                description_dos = ?
                                
               WHERE book_id = {_id}

    """

    try:
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        print("Libro Actualizado")
        return True
    except Error as e:
        print("Error al actualizar " + str(e))
    finally:
        if conn:
            cur.close()
            conn.close()

def delete_book(_id):
    conn = create_connection()
    sql = f"DELETE FROM books WHERE book_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("Libro eliminado")
        return True

    except Error as e:
        print ("Error al eliminar" + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

def select_all_books():
    conn = create_connection()
    sql = "SELECT * FROM books"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books

    except Error as e:
        print ("Error al seleccionar el libro" + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_id(_id):
    conn = create_connection()
    sql = f"SELECT * FROM books WHERE book_id = {_id}"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchone()
        return books

    except Error as e:
        print ("Error al seleccionar el id del libro" + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_title(title):
    conn = create_connection()
    sql = f"SELECT * FROM books WHERE title LIKE '%{title}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books

    except Error as e:
        print ("Error al buscar el libro" + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()

def select_book_by_category(category):
    conn = create_connection()
    sql = f"SELECT * FROM books WHERE category LIKE '%{category}%'"

    try:
        cur = conn.cursor()
        cur.execute(sql)
        books = cur.fetchall()
        return books

    except Error as e:
        print ("Error al buscar la categoria" + str(e))

    finally:
        if conn:
            cur.close()
            conn.close()
    