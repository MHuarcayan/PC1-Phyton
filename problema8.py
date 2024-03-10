#Programa para mostrar segun hora que comida del dia es ahora
hora_comida = str(input("Ingrese la hora(ejemplo 18:50): "))

hora_comida, minutos_comida = hora_comida.split(":")
hora_comida = int(hora_comida)
minutos_comida = int(minutos_comida)
momento_comida = None


if 7 <= hora_comida <= 8:
    momento_comida = "Desayunar"
    print(f"Es la hora de {momento_comida}")
else:
    if 12 <= hora_comida <= 13:
        momento_comida = "Almorzar"
        print(f"Es la hora de {momento_comida}")
    else:
        if 18 <= hora_comida <= 19:
            momento_comida = "Cenar"
            print(f"Es la hora de {momento_comida}")