Sistema de Gestión de Comercio con Python y Tkinter
Descripción

Este proyecto es un sistema de gestión de comercio que permite registrar productos, compras y ventas, y mantiene un inventario actualizado utilizando una interfaz gráfica de usuario construida con tkinter. La aplicación también realiza cálculos de pérdidas y ganancias basadas en la información registrada.
Estructura del Proyecto

El proyecto está dividido en tres archivos principales:

    main.py: Archivo principal para iniciar la aplicación.
    ui.py: Maneja la interfaz gráfica de usuario.
    database.py: Maneja las operaciones de la base de datos con SQLite.

Instalación

Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde python.org.

    Clona este repositorio o descarga los archivos.
    Navega al directorio del proyecto en tu terminal.

Ejecución

Para iniciar la aplicación, ejecuta el siguiente comando en tu terminal:

python main.py

Archivos
main.py

Archivo principal que inicia la aplicación.

from ui import create_main_window

if __name__ == "__main__":
    create_main_window()

database.py

Maneja todas las operaciones relacionadas con la base de datos utilizando SQLite.

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

ui.py

Maneja la interfaz gráfica de usuario utilizando tkinter.

import tkinter as tk
from tkinter import messagebox
from database import Database

class App:
    def __init__(self, root):
        self.db = Database()
        self.root = root
        self.root.title("Gestión de Comercio")
        self.root.geometry("600x400")

        # Crear componentes
        self.create_widgets()

    def create_widgets(self):
        # Etiquetas y entradas para agregar productos
        self.label_nombre = tk.Label(self.root, text="Nombre del Producto")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self.root)
        self.entry_nombre.pack()

        self.label_precio_compra = tk.Label(self.root, text="Precio de Compra")
        self.label_precio_compra.pack()
        self.entry_precio_compra = tk.Entry(self.root)
        self.entry_precio_compra.pack()

        self.label_precio_venta = tk.Label(self.root, text="Precio de Venta")
        self.label_precio_venta.pack()
        self.entry_precio_venta = tk.Entry(self.root)
        self.entry_precio_venta.pack()

        self.label_stock = tk.Label(self.root, text="Stock Inicial")
        self.label_stock.pack()
        self.entry_stock = tk.Entry(self.root)
        self.entry_stock.pack()

        self.btn_add_product = tk.Button(self.root, text="Agregar Producto", command=self.add_product)
        self.btn_add_product.pack(pady=10)

        # Etiquetas y entradas para registrar compras
        self.label_producto_compra = tk.Label(self.root, text="Producto (ID) para Comprar")
        self.label_producto_compra.pack()
        self.entry_producto_compra = tk.Entry(self.root)
        self.entry_producto_compra.pack()

        self.label_cantidad_compra = tk.Label(self.root, text="Cantidad de Compra")
        self.label_cantidad_compra.pack()
        self.entry_cantidad_compra = tk.Entry(self.root)
        self.entry_cantidad_compra.pack()

        self.btn_add_compra = tk.Button(self.root, text="Registrar Compra", command=self.add_compra)
        self.btn_add_compra.pack(pady=10)

        # Etiquetas y entradas para registrar ventas
        self.label_producto_venta = tk.Label(self.root, text="Producto (ID) para Vender")
        self.label_producto_venta.pack()
        self.entry_producto_venta = tk.Entry(self.root)
        self.entry_producto_venta.pack()

        self.label_cantidad_venta = tk.Label(self.root, text="Cantidad de Venta")
        self.label_cantidad_venta.pack()
        self.entry_cantidad_venta = tk.Entry(self.root)
        self.entry_cantidad_venta.pack()

        self.btn_add_venta = tk.Button(self.root, text="Registrar Venta", command=self.add_venta)
        self.btn_add_venta.pack(pady=10)

        # Botón para mostrar el stock
        self.btn_show_stock = tk.Button(self.root, text="Mostrar Stock", command=self.show_stock)
        self.btn_show_stock.pack(pady=10)

    def add_product(self):
        nombre = self.entry_nombre.get()
        precio_compra = float(self.entry_precio_compra.get())
        precio_venta = float(self.entry_precio_venta.get())
        stock = int(self.entry_stock.get())

        self.db.add_product(nombre, precio_compra, precio_venta, stock)
        messagebox.showinfo("Info", "Producto agregado con éxito")

    def add_compra(self):
        producto_id = int(self.entry_producto_compra.get())
        cantidad = int(self.entry_cantidad_compra.get())

        self.db.add_compra(producto_id, cantidad)
        messagebox.showinfo("Info", "Compra registrada con éxito")

    def add_venta(self):
        producto_id = int(self.entry_producto_venta.get())
        cantidad = int(self.entry_cantidad_venta.get())

        self.db.add_venta(producto_id, cantidad)
        messagebox.showinfo("Info", "Venta registrada con éxito")

    def show_stock(self):
        stock_data = self.db.get_stock()
        stock_message = "\n".join([f"Producto: {d[0]}, Stock: {d[1]}" for d in stock_data])
        messagebox.showinfo("Stock", stock_message)

def create_main_window():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

Agregar Producto

    Ingresa el nombre, precio de compra, precio de venta y stock inicial del producto en los campos correspondientes.
    Haz clic en "Agregar Producto" para guardar el producto en la base de datos.

Registrar Compra

    Ingresa el ID del producto y la cantidad de compra en los campos correspondientes.
    Haz clic en "Registrar Compra" para registrar la compra y actualizar el stock.

Registrar Venta

    Ingresa el ID del producto y la cantidad de venta en los campos correspondientes.
    Haz clic en "Registrar Venta" para registrar la venta y actualizar el stock.

Mostrar Stock

    Haz clic en "Mostrar Stock" para ver el stock actual de todos los productos.

Contribución

Las contribuciones son bienvenidas. Si deseas mejorar este proyecto, por favor, envía un pull request.
Licencia

Este proyecto está bajo la Licencia MIT.

