# Diferentes formas de importar módulos

print("=== Demo de Importación de Módulos ===")

# 1. Importar módulo completo
import math
import datetime

# 2. Importar función específica
from random import randint, choice
from os import getcwd

# 3. Importar con alias
import json as js
import sys as sistema

# 4. Importar múltiples elementos
from collections import Counter, defaultdict

# Usar los módulos importados
print(f"π = {math.pi:.4f}")
print(f"√16 = {math.sqrt(16)}")
print(f"Fecha actual: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}")

print(f"Número aleatorio entre 1-10: {randint(1, 10)}")
frutas = ["manzana", "banana", "naranja"]
print(f"Fruta aleatoria: {choice(frutas)}")

print(f"Directorio actual: {getcwd()}")
print(f"Versión de Python: {sistema.version_info.major}.{sistema.version_info.minor}")

# Ejemplo con json
datos = {"nombre": "Python", "version": 3.9}
json_string = js.dumps(datos)
print(f"JSON: {json_string}")

# Ejemplo con collections
palabras = ["python", "java", "python", "javascript", "python"]
contador = Counter(palabras)
print(f"Contador de palabras: {contador}")

print("\n✅ Demo de importación completada")