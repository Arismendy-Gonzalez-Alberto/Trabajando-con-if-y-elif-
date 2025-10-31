a = int(input("Ingrese un año: "))

if a < 0:
    print("El Año invalido")
    print("Tiene que ser un número positivo")
    
elif a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f"El año {a} es bisiesto")
else:
    print(f"El año {a} no es bisiesto")