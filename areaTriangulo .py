#vamos a crear un programa que calcule el area del triangulo
b = int(input("Dime la base del triangulo: "))
h = int(input("Dime la altura del triangulo: "))
if b <= 0 or h <= 0:
    print("Error: La base y ls altura debem ser valores positivos.")
else:
    resultado = b * h / 2


print(resultado)