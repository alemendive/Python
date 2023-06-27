
def mifuncion(nombre="Juan"):
    print("Hola", nombre)


def operaciones(a, b):
   return a + b, a - b, a * b, a / b

def sumador(**kwargs):
    inicial = kwargs['inicial'] if 'incial' in kwargs else 0
    final = kwargs['final'] if 'final' in kwargs else inicial

    resultado = 0

    for x in range(inicial, final + 1):
        resultado += x

    return resultado

anonima = lambda nombre, nombre2: print("hola", nombre, "adios", nombre2)
anonima("pepe", "juan")


def sumatoria(x):
    return x + x


