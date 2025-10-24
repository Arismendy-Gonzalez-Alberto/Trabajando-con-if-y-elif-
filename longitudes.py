a, b, c = float(input("Lado 1: ")), float(input("Lado 2: ")), float(input("Lado 3: "))
if a + b > c and a + c > b and b + c > a:
    print("Sí forman triángulo")
else:
    print("No forman triángulo")
