temp = float(input("Temperatura en °C: "))
if temp < 0:
    print("Hace mucho frío")
elif temp <= 20:
    print("Clima fresco")
elif temp <= 30:
    print("Clima agradable")
else:
    print("Hace mucho calor")