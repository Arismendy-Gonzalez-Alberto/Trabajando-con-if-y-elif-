n1 = float(input("Ingrese primer número: "))
n2 = float(input("Ingrese segundo número: "))
n3 = float(input("Ingrese tercer número: "))

if n1 > n2 and n1 > n3:
    print("El mayor es:", n1)

elif n2 > n1 and n2 > n3:
    print("El mayor es:", n2)

elif n3 > n1 and n3 > n2:
    print("El mayor es:", n3)

else:
    print("Son iguales")