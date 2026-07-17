import sqlite3

def conectar():
    conexion = sqlite3.connect("inventario.db")
    return conexion

def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        categoria TEXT NOT NULL,
        precio REAL NOT NULL,
        stock INTEGER NOT NULL
    )
    """)

    conexion.commit()
    conexion.close()