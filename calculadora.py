# Calculadora
print("Menu de opciones")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
print("5. potencia")

x= int(input("seleccione una opcion del 1 al 5"))
if x==5:
    print("potencia")
    a= int(input("ingrese la base de la potencia"))
    b= int(input("ingrese el exponente de la potencia"))
    print("el resultado es",a**b)
    