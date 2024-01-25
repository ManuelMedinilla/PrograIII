def temperatura():
    print("Conversion de grados") #def se utiliza para definir una funcion, un bloque de codigo especifico. 
    celsius= float(input("Ingrese los grados celsius a convertir:"))
    faren = (celsius * 9/5)+32
    print ("Los grados Fahrenheit son:", faren) 

def segundos():
    print("Segundos transcurridos en el dia")
    horas= float(input("Ingrese la cantidad de horas transcurridas en el dia:"))
    segundos = 3600
    tiempo = horas * segundos
    print ("Los segundos transcurridos son:", tiempo)

def cambio():
    print("Dolares a Quetzales")
    dolar= float(input("Ingrese la cantidad de dolares a convertir:"))
    tasacambio= float(input("Ingrese la tasa de cambio actual:"))
    quetzales= dolar* tasacambio
    print ("La cantidad convertida de $ a Q es", quetzales)

def formula():
    # Solicitamos los coeficientes al usuario
        a = float(input("Ingrese el coeficiente a: "))
        b = float(input("Ingrese el coeficiente b: "))
        c = float(input("Ingrese el coeficiente c: "))

        # Calculamos el discriminante
        discriminante = (b**2 - 4*a*c)**0.5

        # Calculamos las soluciones usando la fórmula cuadrática
        solucion1 = (-b + discriminante) / (2*a)
        solucion2 = (-b - discriminante) / (2*a)

        # Mostramos las soluciones
        print(f"Las soluciones son: {solucion1} y {solucion2}")

def dato():
 variable = input("Ingresa una variable: ")

 if variable.isdigit():
    print("La variable ingresada es de tipo entero.")
 elif variable.replace('.', '', 1).isdigit():
    print("La variable ingresada es de tipo flotante.")
 else:
    print("La variable ingresada es de tipo cadena.")


while True: #while hace que el menu vuelva a aparecer
    print ("Manuel Medinilla 0901-22-1310")
    print("\nMenu:")
    print("1. Celsius a Fahrenheit")
    print("2. Segundos transcurridos en el dia")
    print("3. Dolares a Quetzales")
    print("4. Formula Cuadratica")
    print("5. Tipo de dato")
    print("0. Salir")

    opcion = input("Seleccione una opcion (0-5): ")

    if opcion == "1":
        temperatura()
    elif opcion == "2":
        segundos()
    elif opcion == "3":
        cambio()
    elif opcion == "4":
        formula()
    elif opcion == "5":
        dato()
    elif opcion == "0":
        print("Programa terminado")
        break
    else:
        print("Opcion no valida. Por favor, seleccione una opcion valida.")