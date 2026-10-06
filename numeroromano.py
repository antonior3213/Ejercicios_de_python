def numero_a_romano(num):

    if num < 1 or num > 3999:
        return "Número inválido. Debe estar entre 1 y 3999."

    resultado = ""

    while num >= 1000:
        num = num - 1000
        resultado = resultado + "M"
    while num >= 900:
        num = num - 900
        resultado = resultado + "CM"
    while num >= 500:
        num = num - 500
        resultado = resultado + "D"
    while num >= 400:
        num = num - 400
        resultado = resultado + "CD"
    while num >= 100:
        num = num - 100
        resultado = resultado + "C"
    while num >= 90:
        num = num - 90
        resultado = resultado + "XC"
    while num >= 50:
        num = num - 50
        resultado = resultado + "L"
    while num >= 40:
        num = num - 40
        resultado = resultado + "XL"
    while num >= 10:
        num = num - 10
        resultado = resultado + "X"
    while num >= 9:
        num = num - 9
        resultado = resultado + "IX"
    while num >= 5:
        num = num - 5
        resultado = resultado + "V"
    while num >= 4:
        num = num - 4
        resultado = resultado + "IV"
    while num >= 1:
        num = num - 1
        resultado = resultado + "I"

    return resultado


try:
    numero = int(input("Introduce un número entero: "))
    print(numero_a_romano(numero))
except ValueError:
    print("Entrada inválida. Debe ser un número entero.")