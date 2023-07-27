#Importar las dependencias de flask
from flask import Flask, render_template

#Crear el objeto Flask 
app = Flask(__name__)

#Crear una ruta de prueba
@app.route("/hello")
def hello():
    return'hello'

#ruta paises
@app.route("/paises")
def paises():
    
    username="lojpropio"
   #SUPERFICIE EN KM2 y NUMERO DE PAISES Y DENSIDAD
    continentes =[
        {
            
        "nombre": "America",
       "poblacion": 1036900579,
       "superficie": "42549000 km2",
       "numeropaises": 35,
       "densidad": "22,8 hab/km2",
       "paises" :[
          {
              "nom" :"Colombia",
              "mon" :"Peso",
              "cap" :"Bogota"
              },
          {
              
              "nom" :"Venezuela",
              "mon" :"Bolivar",
              "cap" :"Caracas"
              },
          {
              
              "nom" :"Ecuador",
              "mon" :"Dolar",
              "cap" :"Quito"
          }
       ]
        },
        {
        "nombre": "Europa",
       "poblacion": 747747395,
        "superficie": "10530751 km2",
       "numeropaises": 50,
       "densidad": "71 hab/km2" ,
       "paises" :[
          {
              
              "nom" :"España",
              "mon" :"Euro",
              "cap" :"Madrid"
              },
          {
              "nom" :"Inglaterra",
              "mon" :"Libra Esterlina",
              "cap" :"Londres "
              }
       ]
        }
    ]
       
       
   
   
    return render_template('paises.html',
                           username = username,
                           continentes = continentes)

