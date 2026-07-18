from flask import Flask, render_template, request, redirect, url_for, session
from database import crear_tabla, crear_usuario_admin, verificar_usuario
from models import Producto

app = Flask(__name__)
app.secret_key = "clave-secreta-oxapampa"

crear_tabla()
crear_usuario_admin()

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]

        if verificar_usuario(usuario, contrasena):
            session["usuario"] = usuario
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Usuario o contraseña incorrectos")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "usuario" not in session:
        return redirect(url_for("login"))
    total_productos = len(Producto.listar_todos())
    return render_template("dashboard.html", total_productos=total_productos)

@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect(url_for("login"))

@app.route("/productos")
def productos():
    if "usuario" not in session:
        return redirect(url_for("login"))
    lista = Producto.listar_todos()
    return render_template("productos.html", productos=lista)

@app.route("/productos/nuevo", methods=["GET", "POST"])
def nuevo_producto():
    if "usuario" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        precio = float(request.form["precio"])
        stock = int(request.form["stock"])

        producto = Producto(nombre, categoria, precio, stock)
        producto.guardar()
        return redirect(url_for("productos"))

    return render_template("nuevo_producto.html")

@app.route("/productos/eliminar/<int:id_producto>")
def eliminar_producto(id_producto):
    if "usuario" not in session:
        return redirect(url_for("login"))
    Producto.eliminar(id_producto)
    return redirect(url_for("productos"))

@app.route("/productos/editar/<int:id_producto>", methods=["GET", "POST"])
def editar_producto(id_producto):
    if "usuario" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        nombre = request.form["nombre"]
        categoria = request.form["categoria"]
        precio = float(request.form["precio"])
        stock = int(request.form["stock"])

        Producto.actualizar(id_producto, nombre, categoria, precio, stock)
        return redirect(url_for("productos"))

    producto = Producto.buscar_por_id(id_producto)
    return render_template("editar_producto.html", producto=producto)

if __name__ == "__main__":
    app.run(debug=True)