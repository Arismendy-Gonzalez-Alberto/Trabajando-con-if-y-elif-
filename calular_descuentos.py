precio = float(input("Ingrese precio del producto: "))
if precio < 50:
    descuento = 0
elif precio <= 100:
    descuento = precio * 0.05
else:
    descuento = precio * 0.10
print("Precio final:", precio - descuento)