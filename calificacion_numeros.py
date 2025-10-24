numeros = [float(input(f"Número {i+1}: ")) for i in range(3)]
positivos = all(n > 0 for n in numeros)
negativos = all(n < 0 for n in numeros)
ceros = any(n == 0 for n in numeros)

if ceros:
    print("Hay ceros")
elif positivos:
    print("Todos positivos")
elif negativos:
    print("Todos negativos")
else:
    print("Mixtos")
