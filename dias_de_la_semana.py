dia = int(input("Ingrese número (1-7): "))
dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

if dia < 1 or dia > 7:
    print("invalido")