# Archivo para demostrar la importación del demo_03b_name_main

print("Iniciando prueba de importación...")
print("Observa que NO se ejecuta el bloque 'if __name__ == '__main__''")

# Importar el módulo
import demo_03b_name_main

print("\n" + "="*40)
print("USANDO EL MÓDULO IMPORTADO")
print("="*40)

# Usar las funciones del módulo importado
print(f"Valor de PI desde el módulo: {demo_03b_name_main.PI}")
print(f"Versión del módulo: {demo_03b_name_main.VERSION}")

mensaje = demo_03b_name_main.saludar("Usuario desde importación")
print(f"{mensaje}")

area = demo_03b_name_main.calcular_area_circulo(3)
print(f"Area de círculo con radio 3: {area:.2f}")

print(f"\n__name__ en este archivo: '{__name__}'")
print(f"__name__ en el módulo importado: '{demo_03b_name_main.__name__}'")

print("\nImportación y uso completados")
print("Nota: La 'operación costosa' NO se ejecutó al importar")