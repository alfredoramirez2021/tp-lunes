import sqlite3

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

def agregar_producto(nombre, precio, cantidad):
    conn = sqlite3.connect('ventas_inventario.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO productos (nombre, precio, cantidad)
    VALUES (?, ?, ?)
    ''', (nombre, precio, cantidad))
    conn.commit()
    conn.close()

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

