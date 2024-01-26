def holamundo():
    print("¡Hola Mundo!")

def holamundo2():
    mensaje = "¡Hola Mundo!"
    print(mensaje)
    
def nombre():
    nom= str(input("Ingrese su nombre:"))
    print ("¡Hola", nom + "!") 
        
        
def operacion():
    print("El resultado de la operacion (3+3/2*5)^2 es:")
    resultado = (6/10)**2
    print ("El resultado de la operacion es:", resultado)

def horass():
    horas= int(input("Ingrese la cantidad de horas trabajadas:"))
    pago=  float(input("Ingrese el pago por hora de la empresa:"))
    pagofinal = horas*pago
    print ("El pago por las horas trabajadas son:", pagofinal)

while True: #while hace que el menu vuelva a aparecer
    print ("Laboratorio 2 - Manuel Medinilla 0901-22-1310")
    print("\nMenu Laboratorio 2:")
    print("1. Cadena Hola mundo")
    print("2. Hola mundo en Variable")
    print("3. Nombre del usuario")
    print("4. Operacion Aritmetica ")
    print("5. Horas trabajadas")
    print("0. Salir")

    opcion = input("Seleccione una opcion (0-5): ")

    if opcion == "1":
        holamundo()
    elif opcion == "2":
        holamundo2()
    elif opcion == "3":
        nombre()
    elif opcion == "4":
        operacion()
    elif opcion == "5":
        horass()
    elif opcion == "0":
        print("Programa terminado")
        break
    else:
        print("Opcion no valida. Por favor, seleccione una opcion valida.")