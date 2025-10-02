# Demostración de ámbitos (scopes) en Python

print("Demo de Scopes")
print("=" * 30)

# Variable global
nombre = "Soy global"

def mostrar_scopes():
    # Variable local
    edad = 25
    
    print(f"Variable global: {nombre}")
    print(f"Variable local: {edad}")

print("1. Variables globales y locales:")
mostrar_scopes()

# Demostración de la palabra clave 'global'
contador = 0

def incrementar():
    global contador
    contador += 1
    print(f"Contador: {contador}")

print("\n2. Modificar variable global:")
print(f"Contador inicial: {contador}")
incrementar()
incrementar()
print(f"Contador final: {contador}")

# Error común: intentar modificar sin 'global'
def ejemplo_error():
    # Esta línea crearía una variable local nueva
    # contador = contador + 1  # Error!
    print("Para modificar variable global, usa 'global'")

print("\n3. Diferencia local vs global:")
x = "Global"

def funcion():
    x = "Local"  # Nueva variable local
    print(f"Dentro de función: {x}")

funcion()
print(f"Fuera de función: {x}")

print("\nDemo de scopes completada")