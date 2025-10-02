# Declaración y asignación de variables

print("Demo de Variables")

# Variables básicas
nombre = "Python"
version = 3.9
es_interpretado = True

print(f"Lenguaje: {nombre}")
print(f"Versión: {version}")
print(f"Es interpretado? {es_interpretado}")

# Asignación múltiple
x, y, z = 1, 2, 3
print(f"x={x}, y={y}, z={z}")

# Asignación en cadena
a = b = c = 0
print(f"a={a}, b={b}, c={c}")

# Intercambio de variables (pythónico)
primera = "A"
segunda = "B"
print(f"Antes del intercambio: primera={primera}, segunda={segunda}")

primera, segunda = segunda, primera
print(f"Después del intercambio: primera={primera}, segunda={segunda}")

# Convenciones de nombres
CONSTANTE = 100  # Constante (por convención, en mayúsculas)
mi_variable = "snake_case"  # Recomendado en Python
_privada = "variable privada"  # Por convención, variable "privada"

print(f"Constante: {CONSTANTE}")
print(f"Variable snake_case: {mi_variable}")
print(f"Variable 'privada': {_privada}")

# Variables dinámicas - Python permite cambiar el tipo
numero = 42
print(f"numero es un {type(numero).__name__}: {numero}")

numero = "Ahora soy texto"
print(f"numero es un {type(numero).__name__}: {numero}")

numero = [1, 2, 3]
print(f"numero es una {type(numero).__name__}: {numero}")

print("\nDemo de variables completada")