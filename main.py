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

#Exercise 7

@app.get("/exercise7")
def exercise7():
        persona = {
                "nombre": "Kevin",
                "edad": 24,
                "ciudad": "Barranquilla"
        }
        claves = list(persona.keys())
        return {"exercise": 7, "claves": claves}

#Exercise 8

class Producto:
        def __init__(self, nombre: str, precio: float):
                self.nombre = nombre
                self.precio = precio

        def to_dict(self):
                return {
                        "nombre": self.nombre,
                        "precio": self.precio
                }

@app.get("/exercise8")
def exercise8():
        producto = Producto("Teclado", 150000)
        return {"exercise": 8, "producto": producto.to_dict()}

#Exercise 9

@app.get("/exercise9")
def exercise9(a: int = 0, b: int = 1):
        try:
                resultado = a / b
                return {"exercise": 9, "resultado": resultado}
        except ZeroDivisionError:
                return {"exercise": 9, "error": "No se puede dividir por cero"}
        except Exception as e:
                return {"exercise": 9, "error": str(e)}

#Exercise 10

@app.get("/exercise10")
def exercise10():
        lista = list(range(1, 11))
        return {"exercise": 10, "lista": lista}

#Exercise 11

@app.get("/exercise11")
def exercise11():
        lista = [1, 2, 3, 4, 5]
        duplicada = [n * 2 for n in lista]
        return {"exercise": 11, "original": lista, "duplicada": duplicada}
