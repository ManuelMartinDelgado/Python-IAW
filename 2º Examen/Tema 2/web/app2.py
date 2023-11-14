from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hola():
    peso=""
    altura=""
    imc=""
    if (request.method == "POST"):
        peso = request.form.get("peso")
        altura = request.form.get("altura")
        imc=peso/altura*altura
        print(imc)
    return render_template("index2.html", f"ES peso=peso, altura=altura, imc=imc")

app.run()