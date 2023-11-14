from flask import Flask, request, render_template

app = Flask(__name__)

def calculo_imc(altura,peso):
    altura= float(altura)
    peso= float(peso)
    imc= peso / (altura**2)
    return imc

def clasificacion_imc (imc): 
    if imc < 18.5:
        return("Bajo peso")
    elif 18.5 < imc < 24.9:
        return("Normal")
    elif 24.9 < imc < 29.9:
        return("Sobrepeso")
    elif imc> 30.0:
        return("Obesidad")
    
    
    
@app.route("/", methods=["POST", "GET"])
def index ():
    try:
        if (request.method == "POST"):
            peso = request.form.get("peso")
            altura = request.form.get("altura")
            imc=round(calculo_imc(altura,peso),2)
            clasificacion=clasificacion_imc(imc)
            return render_template("index2.html", imc=imc, clasificacion=clasificacion)
        return render_template ("index2.html")
    except ValueError:
        return("hola")
app.run()