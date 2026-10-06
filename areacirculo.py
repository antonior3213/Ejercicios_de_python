import math

radio = float(input("Ingrese el valor del radio: "))

if radio > 0:
    area = math.pi * radio ** 2
    longitud = math.ceil(area / 2)
    print(f"Área: {area} metros cuadrados, Longitud: {longitud} metros")
else:
    print("El radio debe ser un número positivo")