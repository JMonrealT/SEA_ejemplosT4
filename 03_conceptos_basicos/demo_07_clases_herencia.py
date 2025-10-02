# Demostración de clases y herencia

print("Demo de Clases y Herencia")

# Clase base
class Vehiculo:
    # Variable de clase (compartida por todas las instancias)
    ruedas_por_defecto = 4
    
    def __init__(self, marca, modelo):
        # Variables de instancia
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        self.encendido = False
    
    def encender(self):
        self.encendido = True
        print(f"{self} se ha encendido")
    
    def acelerar(self, incremento):
        if not self.encendido:
            print(f"{self} debe estar encendido para acelerar")
            return
        
        self.velocidad += incremento
        print(f"{self} acelera a {self.velocidad} km/h")
    
    def frenar(self):
        self.velocidad = 0
        print(f"{self} se detiene")
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"

# Herencia - Clase derivada
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llamar al constructor padre
        self.puertas = puertas
    
    def tocar_claxon(self):
        print(f"{self} toca el claxon: BEEP BEEP!")
    
    def info_completa(self):
        return f"{self} - {self.puertas} puertas"

# Otra clase derivada con comportamiento diferente
class Motocicleta(Vehiculo):
    ruedas_por_defecto = 2  # Sobrescribir variable de clase
    
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)
        self.cilindrada = cilindrada
    
    def hacer_caballito(self):
        if self.velocidad > 20:
            print(f"{self} hace un caballito espectacular!")
        else:
            print(f"{self} necesita más velocidad para hacer caballito")
    
    def acelerar(self, incremento):
        # Sobrescribir método con comportamiento específico
        if not self.encendido:
            print(f"❌ {self} debe estar encendido para acelerar")
            return
        
        self.velocidad += incremento * 1.5  # Las motos aceleran más rápido
        print(f"{self} acelera rápidamente a {self.velocidad} km/h")

# Clase con herencia múltiple (concepto avanzado)
class Electrico:
    def __init__(self):
        self.bateria = 100
    
    def cargar_bateria(self):
        self.bateria = 100
        print("Batería cargada al 100%")

class CocheElectrico(Coche, Electrico):
    def __init__(self, marca, modelo, puertas, autonomia):
        Coche.__init__(self, marca, modelo, puertas)
        Electrico.__init__(self)
        self.autonomia = autonomia
    
    def acelerar(self, incremento):
        if self.bateria <= 0:
            print(f"{self} no tiene batería")
            return
        
        super().acelerar(incremento)
        self.bateria -= 2  # Gastar batería
        print(f"Batería restante: {self.bateria}%")

# Demo de uso
print("1. Creando vehículos:")
mi_coche = Coche("Toyota", "Corolla", 4)
mi_moto = Motocicleta("Honda", "CBR", 600)
mi_tesla = CocheElectrico("Tesla", "Model 3", 4, 500)

print(f"Coche: {mi_coche.info_completa()}")
print(f"Moto: {mi_moto} - {mi_moto.cilindrada}cc - {mi_moto.ruedas_por_defecto} ruedas")
print(f"Tesla: {mi_tesla.info_completa()} - {mi_tesla.autonomia}km autonomía")

print("\n2. Probando métodos:")
# Encender vehículos
mi_coche.encender()
mi_moto.encender()
mi_tesla.encender()

print("\n3. Acelerando:")
mi_coche.acelerar(50)
mi_moto.acelerar(50)  # Acelera más rápido
mi_tesla.acelerar(60)

print("\n4. Métodos específicos:")
mi_coche.tocar_claxon()
mi_moto.hacer_caballito()
mi_tesla.cargar_bateria()

print("\n5. Acelerando más:")
mi_moto.acelerar(30)
mi_moto.hacer_caballito()  # Ahora con suficiente velocidad

# Gastar batería del Tesla
for i in range(20):
    mi_tesla.acelerar(10)

print("\n6. Frenando:")
mi_coche.frenar()
mi_moto.frenar()
mi_tesla.frenar()

print("\n7. Verificando herencia:")
print(f"¿mi_coche es instancia de Vehiculo? {isinstance(mi_coche, Vehiculo)}")
print(f"¿mi_coche es instancia de Coche? {isinstance(mi_coche, Coche)}")
print(f"¿mi_tesla es instancia de Electrico? {isinstance(mi_tesla, Electrico)}")

print("\nDemo de clases y herencia completada")