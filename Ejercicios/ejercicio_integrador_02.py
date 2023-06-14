ancho = int(input("Ingrese ancho del terreno: "))
alto = int(input("Ingrese alto del terreno: "))
precio_m2 = float(input("Ingrese precio del terreno: "))


cant_pasadas = 3

superficie = ancho * alto
precio_terreno = superficie * precio_m2

perimetro = 2 * ancho + 2 * alto
cant_alambre = perimetro * cant_pasadas

print("El precio del terreno es de USD",precio_terreno)
print("Cant metros para",cant_pasadas,"pasadas: ",cant_alambre,"m.")