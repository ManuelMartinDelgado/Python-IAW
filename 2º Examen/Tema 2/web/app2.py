from flask import Flask, request, render_template

app = Flask(__name__)

def caculo_imc(altura,peso):
    altura= altura
    peso=altura
    imc=peso/altura*altura
    return imc
try: 
    if imc < 18.5 :
        print("Bajo peso")
    elif 
    
    
    
    @app.route("/", methods=["POST", "GET"])
    def index ():
        peso=""
        altura=""
        if (request.method == "POST"):
            peso = request.form.get("peso")
            altura = request.form.get("altura")
        return render_template("index2.html")

app.run()