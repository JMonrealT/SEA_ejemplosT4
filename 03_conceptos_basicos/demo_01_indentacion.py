# Demostración de indentación en Python
print("Demo de indentación:")

# Estructura condicional - requiere indentación
numero = 5
if numero > 0:
    print("  ✓ Número positivo")
    if numero > 10:
        print("    ✓ Y mayor que 10")
    else:
        print("    ✓ Pero menor o igual a 10")
else:
    print("  ✗ Número no positivo")

# Bucle - también requiere indentación
print("\nConteo:")
for i in range(3):
    print(f"  Número: {i}")

# Error común - indentación incorrecta (comentado para evitar error)
# if True:
# print("Error - falta indentación")  # IndentationError

print("\n✅ Demo de indentación completada")