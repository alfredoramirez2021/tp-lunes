# Sistema de Ventas e Inventario

Este proyecto es un sistema de ventas e inventario básico que permite agregar productos, actualizar cantidades, vender productos y ver el inventario utilizando una interfaz gráfica creada con Tkinter y una base de datos SQLite.

## Estructura del Proyecto

El proyecto está dividido en tres archivos principales:

1. `db.py` - Gestión de la base de datos.
2. `functions.py` - Funciones de lógica de negocio.
3. `main.py` - Interfaz gráfica con Tkinter.

## Instalación

1. **Clona el repositorio**:
    ```bash
    https://github.com/alfredoramirez2021/tp-lunes/tree/main
    ```

2. **Asegúrate de tener Python instalado**. Puedes descargarlo desde [python.org](https://www.python.org/).

## Ejecución del Proyecto

1. **Ejecuta el archivo principal**:
    ```bash
    python main.py
    ```

Esto abrirá la interfaz gráfica de Tkinter.

## Descripción de los Archivos

### `db.py`

Este archivo se encarga de gestionar la conexión a la base de datos y las operaciones CRUD (Crear, Leer, Actualizar, Borrar).

- `crear_base_datos()`: Crea la base de datos y la tabla de productos si no existen.
- `agregar_producto(nombre, precio, cantidad)`: Agrega un producto a la base de datos.
- `actualizar_cantidad(producto_id, nueva_cantidad)`: Actualiza la cantidad de un producto existente.
- `ver_inventario()`: Devuelve una lista con todos los productos en el inventario.
- `vender_producto(producto_id, cantidad_vendida, dinero_entregado)`: Realiza la venta de un producto, actualiza la cantidad en la base de datos y calcula el cambio.

### `functions.py`

Este archivo contiene las funciones que interactúan con `db.py` y son utilizadas por la interfaz gráfica.

- `agregar_producto_gui(entry_nombre, entry_precio, entry_cantidad, text_inventario)`: Obtiene los valores de entrada, agrega un producto a la base de datos y actualiza la vista del inventario.
- `actualizar_cantidad_gui(entry_id_actualizar, entry_nueva_cantidad, text_inventario)`: Obtiene los valores de entrada, actualiza la cantidad de un producto y actualiza la vista del inventario.
- `vender_producto_gui(entry_id_vender, entry_cantidad_vender, entry_dinero_entregado, text_inventario)`: Obtiene los valores de entrada, realiza la venta de un producto, muestra el detalle de la venta y actualiza la vista del inventario.
- `actualizar_inventario(text_inventario)`: Actualiza la vista del inventario con los datos actuales de la base de datos.

### `main.py`

Este archivo contiene la configuración de la interfaz gráfica con Tkinter.

- **Crear la base de datos**: Llama a `crear_base_datos()` para asegurarse de que la base de datos y la tabla de productos existen.
- **Crear la interfaz gráfica**: Configura y muestra la interfaz gráfica utilizando Tkinter.

## Funcionalidades

### Agregar Productos

1. Ingresar el nombre del producto.
2. Ingresar el precio del producto.
3. Ingresar la cantidad del producto.
4. Hacer clic en "Agregar producto".

### Actualizar Cantidad de Productos

1. Ingresar el ID del producto a actualizar.
2. Ingresar la nueva cantidad del producto.
3. Hacer clic en "Actualizar cantidad".

### Vender Productos

1. Ingresar el ID del producto a vender.
2. Ingresar la cantidad a vender.
3. Ingresar el dinero entregado.
4. Hacer clic en "Vender producto".

### Ver Inventario

El inventario se muestra automáticamente en la sección de inventario de la interfaz gráfica.

Paso a Paso

db.py

    Conexión a la base de datos y creación de la tabla de productos:
        crear_base_datos(): Establece una conexión con la base de datos SQLite y crea una tabla de productos si no existe.

    Agregar producto:
        agregar_producto(nombre, precio, cantidad): Inserta un nuevo producto en la tabla de productos con el nombre, precio y cantidad proporcionados.

    Actualizar cantidad de producto:
        actualizar_cantidad(producto_id, nueva_cantidad): Actualiza la cantidad de un producto existente basado en su ID.

    Ver inventario:
        ver_inventario(): Recupera todos los productos de la tabla y los devuelve como una lista de tuplas.

    Vender producto:
        vender_producto(producto_id, cantidad_vendida, dinero_entregado):
            Recupera la cantidad y el precio del producto basado en su ID.
            Calcula el valor total de la venta y el cambio basado en el dinero entregado.
            Actualiza la cantidad del producto en la tabla y devuelve el detalle de la venta.

functions.py

    Agregar producto desde la GUI:
        agregar_producto_gui(entry_nombre, entry_precio, entry_cantidad, text_inventario):
            Obtiene los valores de entrada de los campos de la GUI.
            Llama a agregar_producto() para agregar el producto a la base de datos.
            Actualiza la vista del inventario en la GUI.

    Actualizar cantidad de producto desde la GUI:
        actualizar_cantidad_gui(entry_id_actualizar, entry_nueva_cantidad, text_inventario):
            Obtiene los valores de entrada de los campos de la GUI.
            Llama a actualizar_cantidad() para actualizar la cantidad del producto en la base de datos.
            Actualiza la vista del inventario en la GUI.

    Vender producto desde la GUI:
        vender_producto_gui(entry_id_vender, entry_cantidad_vender, entry_dinero_entregado, text_inventario):
            Obtiene los valores de entrada de los campos de la GUI.
            Llama a vender_producto() para realizar la venta.
            Muestra el detalle de la venta y actualiza la vista del inventario en la GUI.

    Actualizar la vista del inventario en la GUI:
        actualizar_inventario(text_inventario):
            Recupera todos los productos de la base de datos.
            Limpia y actualiza el campo de texto de la GUI con los productos actuales.

main.py

    Crear la base de datos:
        Llama a crear_base_datos() para asegurarse de que la base de datos y la tabla de productos existen.

    Crear la interfaz gráfica:
        Configura y muestra la interfaz gráfica utilizando Tkinter.
        Proporciona campos de entrada y botones para agregar productos, actualizar cantidades y vender productos.
        Muestra el inventario en un campo de texto.

Ejecución del programa

    El usuario interactúa con la interfaz gráfica para agregar productos, actualizar cantidades y vender productos.
    Las acciones del usuario en la GUI llaman a las funciones de functions.py, que a su vez interactúan con db.py para realizar operaciones en la base de datos.
    La vista del inventario se actualiza automáticamente en la GUI para reflejar los cambios realizados en la base de datos.



