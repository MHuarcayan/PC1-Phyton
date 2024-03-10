# solicitar datos del cliente
edad_usuario = int(input('Por favor, ingresar su edad: '))
# determinar precio entrada
if edad_usuario < 4:
    precio_entrada = 0  
elif 4 <= edad_usuario <= 18:
    precio_entrada = 5  
else:
    precio_entrada = 10 

# Mostrar el precio de la entrada al cliente
print('El precio de la entrada para el cliente es: $', precio_entrada)