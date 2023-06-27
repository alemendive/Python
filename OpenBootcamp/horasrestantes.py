import time


hora_actual = time.localtime().tm_hour

if hora_actual >= 19:
    print("Es hora de ir a casa.")
else:
    horas_restantes = 19 - hora_actual
    print("Aún quedan", horas_restantes, "horas")