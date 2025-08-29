# Calculadora
print("Menu de opciones")
print("1. suma")
print("2. resta")
print("3. multiplicacion")
print("4. division")
print("5. potencia")

x= int(input("seleccione una opcion del 1 al 5"))

if x == 3:
    print("ingrese dos numeros")
    a= int(input())
    b= int(input())
    print("el resultado es", a*b)
