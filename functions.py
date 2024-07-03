import tkinter as tk
from tkinter import messagebox
from db import agregar_producto, actualizar_cantidad, ver_inventario, vender_producto

def agregar_producto_gui(entry_nombre, entry_precio, entry_cantidad, text_inventario):
    nombre = entry_nombre.get()
    precio = float(entry_precio.get())
    cantidad = int(entry_cantidad.get())
    agregar_producto(nombre, precio, cantidad)
    messagebox.showinfo("Información", "Producto añadido con éxito.")
    entry_nombre.delete(0, tk.END)
    entry_precio.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    actualizar_inventario(text_inventario)

def actualizar_cantidad_gui(entry_id_actualizar, entry_nueva_cantidad, text_inventario):
    producto_id = int(entry_id_actualizar.get())
    nueva_cantidad = int(entry_nueva_cantidad.get())
    actualizar_cantidad(producto_id, nueva_cantidad)
    messagebox.showinfo("Información", "Cantidad actualizada con éxito.")
    entry_id_actualizar.delete(0, tk.END)
    entry_nueva_cantidad.delete(0, tk.END)
    actualizar_inventario(text_inventario)

def vender_producto_gui(entry_id_vender, entry_cantidad_vender, entry_dinero_entregado, text_inventario):
    producto_id = int(entry_id_vender.get())
    cantidad_vendida = int(entry_cantidad_vender.get())
    dinero_entregado = float(entry_dinero_entregado.get())
    detalle_venta = vender_producto(producto_id, cantidad_vendida, dinero_entregado)
    messagebox.showinfo("Detalle de Venta", detalle_venta)
    entry_id_vender.delete(0, tk.END)
    entry_cantidad_vender.delete(0, tk.END)
    entry_dinero_entregado.delete(0, tk.END)
    actualizar_inventario(text_inventario)

def actualizar_inventario(text_inventario):
    inventario = ver_inventario()
    text_inventario.delete(1.0, tk.END)
    for producto in inventario:
        text_inventario.insert(tk.END, f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}\n")
