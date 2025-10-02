# Demostración de ámbitos (scopes) en Python

print("=== Demo de Scopes (Ámbitos) ===")

# Variable global
variable_global = "Soy global"

def funcion_externa():
    # Variable local a funcion_externa
    variable_local = "Soy local externa"
    
    def funcion_interna():
        # Variable local a funcion_interna
        variable_muy_local = "Soy muy local"
        
        # Acceso a variables de diferentes ámbitos
        print("Desde función interna:")
        print(f"  - Global: {variable_global}")
        print(f"  - Local externa: {variable_local}")
        print(f"  - Muy local: {variable_muy_local}")
    
    funcion_interna()
    print("Desde función externa:")
    print(f"  - Global: {variable_global}")
    print(f"  - Local: {variable_local}")
    # print(f"  - Muy local: {variable_muy_local}")  # Error: no accesible

# Demostración de modificación con global
contador_global = 0

def incrementar_global():
    global contador_global
    contador_global += 1
    print(f"Contador global incrementado: {contador_global}")

def intentar_modificar_sin_global():
    # Esto crea una variable local, no modifica la global
    contador_global = 100
    print(f"Contador local (no afecta global): {contador_global}")

# Demostración de nonlocal
def funcion_con_nonlocal():
    contador_local = 0
    
    def incrementar():
        nonlocal contador_local
        contador_local += 1
        return contador_local
    
    def resetear():
        nonlocal contador_local
        contador_local = 0
    
    return incrementar, resetear

# Ejecución de demos
print("1. Demo de jerarquía de scopes:")
funcion_externa()

print("\n2. Demo de 'global':")
print(f"Contador global inicial: {contador_global}")
incrementar_global()
incrementar_global()
intentar_modificar_sin_global()
print(f"Contador global final: {contador_global}")

print("\n3. Demo de 'nonlocal':")
incrementador, reseteador = funcion_con_nonlocal()
print(f"Incremento 1: {incrementador()}")
print(f"Incremento 2: {incrementador()}")
print(f"Incremento 3: {incrementador()}")
reseteador()
print(f"Después de resetear: {incrementador()}")

# Regla LEGB (Local, Enclosing, Global, Built-in)
print("\n4. Demostración de regla LEGB:")

# Built-in
print(f"len es una función built-in: {len}")

# Global
len = "Ahora len es una variable global"  # Sombreamos la función built-in
print(f"len global: {len}")

def mostrar_legb():
    # Enclosing (ya visto arriba)
    # Local
    len = "len local en función"
    print(f"len local: {len}")

mostrar_legb()
print(f"len global después de función: {len}")

# Restaurar la función built-in (para buenas prácticas)
del len
print(f"len built-in restaurado: {len([1,2,3])}")

print("\n✅ Demo de scopes completada")