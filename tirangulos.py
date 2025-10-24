a, b, c = float(input("Lado 1: ")), float(input("Lado 2: ")), float(input("Lado 3: "))
if a == b == c:
    print("Equilátero")
elif a == b or b == c or a == c:
    print("Isósceles")
else:
    print("Escaleno")