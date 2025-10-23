# mi_calculadora.py - Módulo simple con funciones matemáticas

print(f"📦 Cargando módulo 'mi_calculadora'...")
print(f"📍 __name__ = '{__name__}'")

def sumar(a, b):
    """Suma dos números"""
    return a + b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

# Este código SOLO se ejecuta si ejecutamos el archivo directamente
if __name__ == '__main__':
    print("\n" + "="*50)
    print("🏃 EJECUTANDO COMO SCRIPT PRINCIPAL")
    print("="*50)
    
    # Código de prueba
    print("\nProbando las funciones:")
    print(f"  5 + 3 = {sumar(5, 3)}")
    print(f"  5 × 3 = {multiplicar(5, 3)}")
    
    print("\n✅ Pruebas completadas")
    print("="*50)

print(f"✓ Módulo 'mi_calculadora' cargado\n")
