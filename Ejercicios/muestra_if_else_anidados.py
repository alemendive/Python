
x = int(input("Coloca un numero entero: "))

if x != 0:
    if x > 0:
        resultado = "positivo"
    else:
        resultado = "negativo"
else:
    resultado = "neutro"


print(x, "es", resultado)