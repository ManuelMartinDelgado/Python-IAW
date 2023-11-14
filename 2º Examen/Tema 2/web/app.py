from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hola():
    usuario=""
    contrasena=""
    if (request.method == "POST"):
        usuario = request.form.get("usuario")
        contrasena = request.form.get("contrasena")
        print(usuario, contrasena)
    return render_template("index.html", usuario=usuario, contrasena=contrasena)

@app.route("/baloncesto")
def baloncesto():
    return "Hola, esto es basketball"

@app.route("/pruebaPost", methods=["POST", "GET"])
def pruebaPost():
    if (request.method == "POST"):
        return "Esto es un POST"
    elif (request.method == "GET"):
        return "Estoy haciendo un get"
    return "Hola, esto es basketball"

app.run()






