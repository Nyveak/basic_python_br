from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

@app.get("/")
def initialEndpoint():
	return {"message":"Hola Mundo"}

#Exercise 1

@app.get("/exercise1")
def exercise1():
	nombre = "Kevin"
	return {"exercise": 1, "value": nombre}

#Exercise 2

@app.get("/exercise2")
def exercise2(a: int = 0, b: int = 0):
	return {"exercise": 2, "resultado": a + b}

#Exercise 3

@app.get("/exercise3")
def exercise3(num: int):
	return {"exercise": 3, "numero": num, "es par": num % 2 == 0} 

#Exercise 4

@app.get("/exercise4")
def exercise4():
	lista = [1, 2, 3, 4, 5]
	recorrido = [n for n in lista]
	return {"exercise": 4, "Lista": recorrido}

#Exercise 5

@app.get("/exercise5")
def exercise5(a: int, b: int):
	resultado = a * b
	return {"exercise": 5, "Resultado": resultado}

#Exercise 6

@app.get("/exercise6")
def exercise6():
        persona = {
                "nombre": "Kevin",
                "edad": 24,
                "ciudad": "Barranquilla"
        }

        return {"exercise": 6, "persona": persona}	
