# definir datos numerico
N = int(input('Ingresar un numero entero positivo: '))
# verificar si numero entero es positivo y calculo de suma
if N < 0:
    print('El numero ingresado no es un entero positivo')
else:
    suma_enteros = N * (N + 1) / 2
# Mostrar suma enteros 1 a N
print('La suma de todos los enteros del 1 a', N, 'es:', suma_enteros)