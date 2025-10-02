# Tipos de datos básicos en Python

print("=== Demo de Tipos de Datos ===")

# Números
entero = 42
flotante = 3.14159
complejo = 3 + 4j

print("--- NÚMEROS ---")
print(f"Entero: {entero} ({type(entero).__name__})")
print(f"Flotante: {flotante} ({type(flotante).__name__})")
print(f"Complejo: {complejo} ({type(complejo).__name__})")

# Cadenas
texto = "Hola mundo"
texto_multilinea = """Este es un
texto de múltiples
líneas"""

print("\n--- CADENAS ---")
print(f"Texto: '{texto}' ({type(texto).__name__})")
print(f"Texto multilínea: {repr(texto_multilinea)} ({type(texto_multilinea).__name__})")

# Booleanos
verdadero = True
falso = False

print("\n--- BOOLEANOS ---")
print(f"Verdadero: {verdadero} ({type(verdadero).__name__})")
print(f"Falso: {falso} ({type(falso).__name__})")

# Estructuras de datos
lista = [1, 2, 3, "texto", True]
tupla = (1, 2, 3)
diccionario = {"nombre": "Ana", "edad": 25, "activo": True}
conjunto = {1, 2, 3, 4, 5}

print("\n--- ESTRUCTURAS DE DATOS ---")
print(f"Lista: {lista} ({type(lista).__name__})")
print(f"Tupla: {tupla} ({type(tupla).__name__})")
print(f"Diccionario: {diccionario} ({type(diccionario).__name__})")
print(f"Conjunto: {conjunto} ({type(conjunto).__name__})")

# Tipo especial - None
vacio = None
print(f"\nValor None: {vacio} ({type(vacio).__name__})")

# Conversión de tipos
print("\n--- CONVERSIÓN DE TIPOS ---")
numero_str = "123"
numero_int = int(numero_str)
numero_float = float(numero_str)

print(f"String '{numero_str}' -> int: {numero_int}")
print(f"String '{numero_str}' -> float: {numero_float}")
print(f"Int {numero_int} -> bool: {bool(numero_int)}")
print(f"Int 0 -> bool: {bool(0)}")

print("\n✅ Demo de tipos de datos completada")