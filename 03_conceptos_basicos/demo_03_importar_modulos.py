# Diferentes formas de importar módulos

print("Demo de Importación de Módulos")

# 1. Importar módulo completo
import math
import datetime

# 2. Importar función específica  
from random import randint, choice
from os import getcwd

# 3. Importar con alias
import json as js

# Usar los módulos importados
print("Usando math:")
print(f"PI = {math.pi:.4f}")
print(f"Raíz de 16 = {math.sqrt(16)}")

print("\nUsando datetime:")
print(f"Fecha actual: {datetime.datetime.now().strftime('%Y-%m-%d')}")

print("\nUsando random:")
print(f"Número aleatorio: {randint(1, 10)}")
frutas = ["manzana", "banana", "naranja"]
print(f"Fruta aleatoria: {choice(frutas)}")

print("\nUsando os:")
print(f"Directorio actual: {getcwd()}")

print("\nUsando json con alias:")
datos = {"nombre": "Python", "version": 3.9}
json_string = js.dumps(datos)
print(f"JSON: {json_string}")

print("\nDemo completada")