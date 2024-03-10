# Leer dos números por teclado
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# usar funcion para mostrar menu
def mostrar_menu():
    print("Menú:")
    print("1. Mostrar la suma de los dos números")
    print("2. Mostrar la resta de los dos números")
    print("3. Mostrar la multiplicación de los dos números")
    opcion = input("Seleccione una opción (1, 2, 3): ")
    return opcion
# Mostrar el menú y obtener la opción del usuario
opcion = mostrar_menu() 
# Realizar la operación seleccionada por el usuario
if opcion == "1":
    resultado = num1 + num2
    print("La suma de", num1, "y", num2, "es:", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("La resta de", num1, "menos", num2, "es:", resultado)
elif opcion == "3":
    resultado = num1 * num2
    print("La multiplicación de", num1, "y", num2, "es:", resultado)
else:
    print("La opcion elegida es incorrecta. Por favor, seleccione una opción válida (1, 2, 3).")