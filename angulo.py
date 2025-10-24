angulo = float(input("Ingrese ángulo en grados: "))
if angulo < 90:
    print("Agudo")
elif angulo == 90:
    print("Recto")
elif angulo < 180:
    print("Obtuso")
elif angulo == 180:
    print("Llano")
else:
    print("Ángulo mayor a 180°")