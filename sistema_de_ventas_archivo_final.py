import sqlite3
import tkinter as tk
from tkinter import messagebox

# Conexión a la base de datos y creación de la tabla de productos si no existe
def crear_base_datos():
    conn = sqlite3.connect('ventas_inventario.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        precio REAL NOT NULL,
        cantidad INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Funciones para gestionar el inventario
def agregar_producto(nombre, precio, cantidad):
    conn = sqlite3.connect('ventas_inventario.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO productos (nombre, precio, cantidad)
    VALUES (?, ?, ?)
    ''', (nombre, precio, cantidad))
    conn.commit()
    conn.close()
    print("Producto añadido con éxito.")

def actualizar_cantidad(producto_id, nueva_cantidad):
    conn = sqlite3.connect('ventas_inventario.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE productos
    SET cantidad = ?
    WHERE id = ?
    ''', (nueva_cantidad, producto_id))
    conn.commit()
    conn.close()
    print("Cantidad actualizada con éxito.")

def ver_inventario():
    conn = sqlite3.connect('ventas_inventario.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()
    conn.close()
    return productos

def vender_producto(producto_id, cantidad_vendida, dinero_entregado):
    conn = sqlite3.connect('ventas_inventario.db')
    cursor = conn.cursor()
    cursor.execute('SELECT cantidad, precio, nombre FROM productos WHERE id = ?', (producto_id,))
    producto = cursor.fetchone()
    cantidad_disponible = producto[0]
    precio = producto[1]
    nombre = producto[2]
    
    if cantidad_disponible >= cantidad_vendida:
        nueva_cantidad = cantidad_disponible - cantidad_vendida
        valor_total = precio * cantidad_vendida
        cambio = dinero_entregado - valor_total
        
        cursor.execute('''
        UPDATE productos
        SET cantidad = ?
        WHERE id = ?
        ''', (nueva_cantidad, producto_id))
        conn.commit()
        conn.close()
        
        detalle_venta = f"Producto: {nombre}\nCantidad Vendida: {cantidad_vendida}\nPrecio Unitario: {precio}\nValor Total: {valor_total}\nDinero Entregado: {dinero_entregado}\nCambio: {cambio}"
        
        return detalle_venta
    else:
        conn.close()
        return "No hay suficiente stock disponible."

# Funciones para la interfaz gráfica
def agregar_producto_gui():
    nombre = entry_nombre.get()
    precio = float(entry_precio.get())
    cantidad = int(entry_cantidad.get())
    agregar_producto(nombre, precio, cantidad)
    messagebox.showinfo("Información", "Producto añadido con éxito.")
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    actualizar_inventario()

def actualizar_cantidad_gui():
    producto_id = int(entry_id_actualizar.get())
    nueva_cantidad = int(entry_nueva_cantidad.get())
    actualizar_cantidad(producto_id, nueva_cantidad)
    messagebox.showinfo("Información", "Cantidad actualizada con éxito.")
    entry_id_actualizar.delete(0, tk.END)
    entry_nueva_cantidad.delete(0, tk.END)
    actualizar_inventario()

def vender_producto_gui():
    producto_id = int(entry_id_vender.get())
    cantidad_vendida = int(entry_cantidad_vender.get())
    dinero_entregado = float(entry_dinero_entregado.get())
    detalle_venta = vender_producto(producto_id, cantidad_vendida, dinero_entregado)
    messagebox.showinfo("Detalle de Venta", detalle_venta)
    entry_id_vender.delete(0, tk.END)
    entry_cantidad_vender.delete(0, tk.END)
    entry_dinero_entregado.delete(0, tk.END)
    actualizar_inventario()

def actualizar_inventario():
    inventario = ver_inventario()
    text_inventario.delete(1.0, tk.END)
    for producto in inventario:
        text_inventario.insert(tk.END, f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}\n")

# Crear la base de datos
crear_base_datos()

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Sistema de Ventas e Inventario")

# Sección para agregar productos
tk.Label(root, text="Nombre del producto:").grid(row=0, column=0)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1)

tk.Label(root, text="Precio:").grid(row=1, column=0)
entry_precio = tk.Entry(root)
entry_precio.grid(row=1, column=1)

tk.Label(root, text="Cantidad:").grid(row=2, column=0)
entry_cantidad = tk.Entry(root)
entry_cantidad.grid(row=2, column=1)

tk.Button(root, text="Agregar producto", command=agregar_producto_gui).grid(row=3, column=0, columnspan=2)

# Sección para actualizar cantidad
tk.Label(root, text="ID del producto a actualizar:").grid(row=4, column=0)
entry_id_actualizar = tk.Entry(root)
entry_id_actualizar.grid(row=4, column=1)

tk.Label(root, text="Nueva cantidad:").grid(row=5, column=0)
entry_nueva_cantidad = tk.Entry(root)
entry_nueva_cantidad.grid(row=5, column=1)

tk.Button(root, text="Actualizar cantidad", command=actualizar_cantidad_gui).grid(row=6, column=0, columnspan=2)

# Sección para vender productos
tk.Label(root, text="ID del producto a vender:").grid(row=7, column=0)
entry_id_vender = tk.Entry(root)
entry_id_vender.grid(row=7, column=1)

tk.Label(root, text="Cantidad a vender:").grid(row=8, column=0)
entry_cantidad_vender = tk.Entry(root)
entry_cantidad_vender.grid(row=8, column=1)

tk.Label(root, text="Dinero entregado:").grid(row=9, column=0)
entry_dinero_entregado = tk.Entry(root)
entry_dinero_entregado.grid(row=9, column=1)

tk.Button(root, text="Vender producto", command=vender_producto_gui).grid(row=10, column=0, columnspan=2)

# Sección para mostrar inventario
tk.Label(root, text="Inventario:").grid(row=11, column=0, columnspan=2)
text_inventario = tk.Text(root, height=10, width=50)
text_inventario.grid(row=12, column=0, columnspan=2)

actualizar_inventario()

root.mainloop()
