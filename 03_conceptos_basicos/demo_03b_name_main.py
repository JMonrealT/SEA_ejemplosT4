# Demostración del uso de if __name__ == '__main__'

# Este archivo se está cargando...
print("Cargando archivo...")

# Variables y funciones que pueden ser importadas por otros módulos
PI = 3.14159
VERSION = "1.0.0"

def saludar(nombre):
    """Función que puede ser importada desde otros módulos"""
    return f"Hola, {nombre}!"

def calcular_area_circulo(radio):
    """Calcula el área de un círculo"""
    return PI * radio ** 2

def operacion_costosa():
    """Simula una operación que solo queremos ejecutar si corremos directamente"""
    print("Ejecutando operación costosa...")
    resultado = sum(range(100000))  # Más pequeño para ser más rápido
    print(f"Operación completada. Resultado: {resultado}")
    return resultado

# Código que se ejecuta siempre (al importar o ejecutar)
print(f"Configurando módulo: {__name__}")

# ============================================================================
# EL PUNTO CLAVE: if __name__ == '__main__'
# ============================================================================

if __name__ == '__main__':
    # Este bloque SOLO se ejecuta cuando el archivo se ejecuta directamente
    # NO se ejecuta cuando el archivo es importado como módulo
    
    print("\n" + "="*40)
    print("EJECUTANDO COMO SCRIPT PRINCIPAL")
    print("="*40)
    
    print(f"El valor de __name__ es: '{__name__}'")
    print("Esto significa que estamos ejecutando este archivo directamente")
    
    # Código que solo queremos que se ejecute como script principal
    print("\n1. Probando funciones del módulo:")
    mensaje = saludar("Estudiante")
    print(f"   {mensaje}")
    
    area = calcular_area_circulo(5)
    print(f"   Area de circulo con radio 5: {area:.2f}")
    
    print("\n2. Ejecutando operación costosa:")
    operacion_costosa()
    
    print("\n3. Información del módulo:")
    print(f"   PI = {PI}")
    print(f"   VERSION = {VERSION}")
    
    print("\n4. Procesando lista de nombres:")
    nombres = ["Ana", "Carlos", "Maria"]
    for nombre in nombres:
        print(f"   - {saludar(nombre)}")
    
    print("\n5. Ejecutando pruebas básicas:")
    assert calcular_area_circulo(1) == PI, "Error en cálculo de área"
    print("   Todas las pruebas pasaron")
    
    print("\n" + "="*40)
    print("SCRIPT PRINCIPAL COMPLETADO")
    print("="*40)

# Código que se ejecuta siempre (al final)
print(f"Finalizando carga del módulo: {__name__}")

"""
¿QUE ES __name__?

- __name__ es una variable especial de Python
- Cuando ejecutas un archivo directamente: __name__ == '__main__'
- Cuando importas un archivo como módulo: __name__ == nombre_del_archivo

¿PARA QUE SIRVE?

1. SEPARAR CÓDIGO DE IMPORTACIÓN vs EJECUCIÓN:
   - Funciones y variables: se pueden importar
   - Código de prueba: solo se ejecuta directamente

2. CREAR SCRIPTS REUTILIZABLES:
   - El mismo archivo puede ser módulo Y script
   - Facilita testing y desarrollo modular

EJEMPLO DE USO:

Para probar este concepto:

1. Ejecutar directamente:
   python3 demo_03b_name_main.py
   
2. Importar desde otro archivo:
   import demo_03b_name_main
   print(demo_03b_name_main.saludar("Mundo"))

Observa la diferencia en la salida!
"""