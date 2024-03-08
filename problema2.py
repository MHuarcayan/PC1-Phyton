#Solicitar monto consumo total
monto_consumo = float(input("Ingresa el monto de consumo: $"))
# Solicitar porcentaje de propina a dejar
porc_propina = float(input("Ingresar el porcentaje de propina que desea dejar: %"))
# Calculo de la propina
propina = monto_consumo * (porc_propina / 100)
# Mostrar la cantidad de propina que dejo el usuario
print(f"La cantidad de propina  que deja el usuario es: {propina} $")