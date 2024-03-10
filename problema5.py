# datos de show vistos por usuario
cantidad_show = int(input('Ingresar la cantidad de shows musicales vistos en el ultimo año: '))
# Verificando si el usuario vio mas de 3 shows
vio_mas_de_3 = cantidad_show > 3
# Mostrando valores (falso o verdadero)
print('usted vio mas de 3 shows musicales este año?', vio_mas_de_3)