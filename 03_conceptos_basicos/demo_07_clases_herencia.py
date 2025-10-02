# Demostración de clases básicas

print("Demo de Clases")
print("=" * 20)

# Clase simple
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre}")
    
    def cumpleanios(self):
        self.edad += 1
        print(f"Ahora tengo {self.edad} años")

# Crear objetos
print("1. Creando personas:")
juan = Persona("Juan", 25)
maria = Persona("María", 30)

juan.saludar()
maria.saludar()

print("\n2. Usando métodos:")
juan.cumpleanios()
maria.cumpleanios()

# Herencia simple
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamar al constructor padre
        self.carrera = carrera
    
    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}")

print("\n3. Herencia:")
ana = Estudiante("Ana", 20, "Informática")
ana.saludar()  # Método heredado
ana.estudiar()  # Método propio

print("\nDemo de clases completada")