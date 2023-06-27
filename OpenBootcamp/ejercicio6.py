class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

coche1 = Coche("Rojo", 4, 2, 200, 2000)

print("Color: ", coche1.color)
print("Ruedas: ", coche1.ruedas)
print("Puertas: ", coche1.puertas)
print("Velocidad: ", coche1.velocidad)
print("Cilindrada: ", coche1.cilindrada)
