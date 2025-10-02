# 02. Estructuras de Datos

## 📖 Descripción

Las estructuras de datos son fundamentales en Python. Esta sección cubre listas, tuplas, diccionarios y conjuntos, enseñándote cómo almacenar, organizar y manipular datos de manera eficiente.

## 🎯 Objetivos de aprendizaje

Al completar esta sección, serás capaz de:

- Trabajar con listas y sus métodos
- Usar tuplas para datos inmutables
- Crear y manipular diccionarios
- Utilizar conjuntos para operaciones matemáticas
- Elegir la estructura de datos apropiada para cada situación

## 📚 Contenido

### 1. Listas (Lists)

- Creación y acceso a elementos
- Métodos: append(), insert(), remove(), pop()
- Slicing y indexación
- List comprehensions

### 2. Tuplas (Tuples)

- Características de inmutabilidad
- Creación y acceso
- Desempaquetado de tuplas
- Casos de uso prácticos

### 3. Diccionarios (Dictionaries)

- Pares clave-valor
- Métodos: keys(), values(), items()
- Creación y modificación
- Dictionary comprehensions

### 4. Conjuntos (Sets)

- Operaciones matemáticas (unión, intersección)
- Eliminación de duplicados
- Set comprehensions
- Métodos: add(), remove(), discard()

### 5. Estructuras anidadas

- Listas de listas
- Diccionarios con listas
- Combinaciones complejas

## 💻 Ejemplos de código

```python
# Listas
frutas = ["manzana", "banana", "naranja"]
frutas.append("uva")
print(frutas[1])  # banana

# List comprehension
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)  # [1, 4, 9, 16, 25]

# Diccionarios
persona = {
    "nombre": "Carlos",
    "edad": 30,
    "ciudad": "Madrid"
}
persona["profesion"] = "Ingeniero"

# Conjuntos
numeros = {1, 2, 3, 4, 5}
pares = {2, 4, 6, 8}
interseccion = numeros & pares  # {2, 4}
```

## 🏋️ Ejercicios prácticos

1. **Gestor de contactos**: Usando diccionarios para almacenar información
2. **Análisis de texto**: Contar palabras únicas con conjuntos
3. **Lista de compras**: Manipulación avanzada de listas
4. **Matriz de datos**: Trabajar con listas anidadas

## 🔗 Enlaces útiles

- [Documentación sobre estructuras de datos](https://docs.python.org/es/3/tutorial/datastructures.html)
- [Python Collections module](https://docs.python.org/3/library/collections.html)

## ⬅️ Tema anterior
**[01. Fundamentos de Python](../01_python_basics/README.md)**

## ➡️ Siguiente tema
**[03. Control de Flujo](../03_control_flow/README.md)**