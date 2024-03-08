#definir datos de los productos
p_payaso = 112
p_muneca = 75
# Solicitar cantidad ventas de los productos
num_payasos_vendidos = int(input('ingresar numero de productos payasos vendidos: '))
num_munecas_vendidos = int(input('ingresar numero de productos muñecas vendidos: '))
# calcular peso total
peso_total = (num_payasos_vendidos * p_payaso) + (num_munecas_vendidos * p_muneca)
# Mostrar resultado peso total del paquete enviado
print(f'El peso total del paquete a enviar es de: {peso_total} g')