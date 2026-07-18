from database import conectar

class Producto:

    def __init__(self, nombre, categoria, precio, stock, id=None):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def guardar(self):
        conexion = conectar()
        cursor = conexion.cursor()

        cursor.execute("""
        INSERT INTO productos(nombre, categoria, precio, stock)
        VALUES (?, ?, ?, ?)
        """, (self.nombre, self.categoria, self.precio, self.stock))

        conexion.commit()
        conexion.close()

    @staticmethod
    def listar_todos():
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        conexion.close()
        return productos

    @staticmethod
    def buscar_por_id(id_producto):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        producto = cursor.fetchone()
        conexion.close()
        return producto

    @staticmethod
    def actualizar(id_producto, nombre, categoria, precio, stock):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("""
        UPDATE productos
        SET nombre = ?, categoria = ?, precio = ?, stock = ?
        WHERE id = ?
        """, (nombre, categoria, precio, stock, id_producto))
        conexion.commit()
        conexion.close()

    @staticmethod
    def eliminar(id_producto):
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        conexion.close()