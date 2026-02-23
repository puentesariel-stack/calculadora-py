print("*********************************************")
print("CALCULADORA")
print("*********************************************** \n")
print("Elije una opcion:")
print("MENU \n")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Modulo \n")
numero=int(input("Opcion: "))
if numero>=1 and numero<=4:
    "utiliza la variable numero para todo"
    if numero==1:
        numero=int(input("Escribe el primer numero: "))
        numero +=int(input("Escribe el segundo numero: "))
        print("El resultado de la suma es: ", numero)
    elif numero==2:
        numero=int(input("Escribe el primer numero: "))
        numero -=int(input("Escribe el segundo numero: "))
        print("El resultado de la resta es:",numero)
    elif numero==3:
        numero=int(input("Escribe el primer numero: "))
        numero *=int(input("Escribe el segundo numero: "))
        print(">El resultado de la multiplicacion es: ",numero)
    elif numero==4:
        numero=int(input("Escribe el primer numero: "))
        numero %=int(input("Escribe el segundo numero: "))
        print("El resultado del modulo es: ",numero)
else:
    print("Opcion ingresada incorrecta.")
print("FIN")