from flask import Flask
import numpy as np
from flask_cors import CORS
app = Flask (__name__)
CORS(app)

@app.route("/")
def HolaFlask():
    return "<h1>Hola Flask!</h1> <hr>"

@app.route("/notas")
@app.route("/notas/<float:nota1>/<float:nota2>/<float:nota3>")
def notas(nota1=0,nota2=0,nota3=0):
    resultado = (nota1*0.3)+(nota2*0.3)+(nota3*0.4)
    return f"<h1>El resultado es: {resultado}</h1> <hr>"

@app.route("/edades")
@app.route("/edades/<int:edad>")
def edades(edad = 0):
    if edad < 18:
        R = "Menor de edad"
    elif (edad < 60):
        R = "Adulto" 
    else:
        R = "Adulto Mayor"
    return f"<h1>El resultado es: {R}</h1> <hr>"

@app.route("/arreglos")
@app.route("/arreglos/<int:valores>/<int:columnas>")
@app.route("/arreglos/<int:valores>/<int:columnas>/<int:filas>")
def arreglos(valores = 0, columnas = 0, filas  = 0):
    if filas == 0:
        arreglo = np.ramdon.randint(valores, size=columnas)
    else:
        arreglo = np.ramdon.randint(valores, size=(filas, columnas))
    return f"<h1>El resultado es: {arreglo}</h1> <hr>"

if __name__ == '__main__':
    app.run(debug = True)