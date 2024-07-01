import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('comercio.db')
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                precio_compra REAL NOT NULL,
                precio_venta REAL NOT NULL,
                stock INTEGER NOT NULL
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Compras (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto_id INTEGER,
                cantidad INTEGER NOT NULL,
                fecha DATE NOT NULL,
                FOREIGN KEY (producto_id) REFERENCES Productos (id)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Ventas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                producto_id INTEGER,
                cantidad INTEGER NOT NULL,
                fecha DATE NOT NULL,
                FOREIGN KEY (producto_id) REFERENCES Productos (id)
            )
        ''')
        self.conn.commit()

    def add_product(self, nombre, precio_compra, precio_venta, stock):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO Productos (nombre, precio_compra, precio_venta, stock)
            VALUES (?, ?, ?, ?)
        ''', (nombre, precio_compra, precio_venta, stock))
        self.conn.commit()

    def add_compra(self, producto_id, cantidad):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO Compras (producto_id, cantidad, fecha)
            VALUES (?, ?, DATE('now'))
        ''', (producto_id, cantidad))
        cursor.execute('''
            UPDATE Productos
            SET stock = stock + ?
            WHERE id = ?
        ''', (cantidad, producto_id))
        self.conn.commit()

    def add_venta(self, producto_id, cantidad):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO Ventas (producto_id, cantidad, fecha)
            VALUES (?, ?, DATE('now'))
        ''', (producto_id, cantidad))
        cursor.execute('''
            UPDATE Productos
            SET stock = stock - ?
            WHERE id = ?
        ''', (cantidad, producto_id))
        self.conn.commit()

    def get_stock(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            SELECT nombre, stock
            FROM Productos
        ''')
        return cursor.fetchall()
