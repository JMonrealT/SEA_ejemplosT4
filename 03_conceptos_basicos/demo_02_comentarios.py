# Este es un comentario de una línea

"""
Este es un comentario
de múltiples líneas
o docstring
"""

def saludar(nombre):
    """
    Función que saluda a una persona
    Args: nombre (str): Nombre de la persona
    Returns: str: Mensaje de saludo
    """
    return f"Hola, {nombre}!"

# Comentarios inline
edad = 25  # Esta es la edad en años

print("=== Demo de Comentarios ===")
print(saludar("Ana"))  # Llamada a la función
print(f"Edad: {edad}")

# Comentarios para explicar código complejo
resultado = sum(x**2 for x in range(10) if x % 2 == 0)  # Suma de cuadrados de pares
print(f"Suma de cuadrados de números pares del 0-9: {resultado}")

print("\n✅ Demo de comentarios completada")