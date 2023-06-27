class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota)

    def mostrar_resultado(self):
        if self.nota >= 5:
            resultado = "Aprobado"
        else:
            resultado = "Desaprobado"

        print("Resultado: ", resultado)


alumno1 = Alumno("Juan", 8)

alumno1.imprimir_datos()

alumno1.mostrar_resultado()