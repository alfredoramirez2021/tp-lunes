import tkinter as tk
from functions import agregar_producto_gui, actualizar_cantidad_gui, vender_producto_gui, actualizar_inventario
from db import crear_base_datos

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

tk.Button(root, text="Agregar producto", command=lambda: agregar_producto_gui(entry_nombre, entry_precio, entry_cantidad, text_inventario)).grid(row=3, column=0, columnspan=2)

# Sección para actualizar cantidad
tk.Label(root, text="ID del producto a actualizar:").grid(row=4, column=0)
entry_id_actualizar = tk.Entry(root)
entry_id_actualizar.grid(row=4, column=1)

tk.Label(root, text="Nueva cantidad:").grid(row=5, column=0)
entry_nueva_cantidad = tk.Entry(root)
entry_nueva_cantidad.grid(row=5, column=1)

tk.Button(root, text="Actualizar cantidad", command=lambda: actualizar_cantidad_gui(entry_id_actualizar, entry_nueva_cantidad, text_inventario)).grid(row=6, column=0, columnspan=2)

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

tk.Button(root, text="Vender producto", command=lambda: vender_producto_gui(entry_id_vender, entry_cantidad_vender, entry_dinero_entregado, text_inventario)).grid(row=10, column=0, columnspan=2)

# Sección para mostrar inventario
tk.Label(root, text="Inventario:").grid(row=11, column=0, columnspan=2)
text_inventario = tk.Text(root, height=10, width=50)
text_inventario.grid(row=12, column=0, columnspan=2)

actualizar_inventario(text_inventario)

root.mainloop()
