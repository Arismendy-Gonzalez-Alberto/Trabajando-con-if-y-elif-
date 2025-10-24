salario = float(input("Ingrese salario mensual: "))
if salario < 10000:
    impuesto = 0
elif salario <= 30000:
    impuesto = salario * 0.10
else:
    impuesto = salario * 0.20
print("Impuesto a pagar:", impuesto)