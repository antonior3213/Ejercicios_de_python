def fila(a, b):
    print(a, b, "|", int(a and b), "  ", int(a or b), "  ", int(not a))

print("TABLA DE VERDADES")
print("A B | AND | OR | NOT A")

fila(0, 0)
fila(0, 1)
fila(1, 0)
fila(1, 1)