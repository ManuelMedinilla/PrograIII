# una variable es un espacio de almacenamiento que tiene un nombre simbólico (un identificador) y está asociado con un valor o información.
# Los operadores aritméticos son símbolos que realizan operaciones matemáticas en variables y valores
def calculadora():
    numero1= float(input("Ingrese el primer numero:"))
    numero2= float(input("Ingrese el segundo numero numero:"))
    suma = numero1 + numero2
    resta = numero1 - numero2 
    multi =  numero1 * numero2 
    divi =  numero1 / numero2 
    print ("El resultado de la suma es:", suma)
    print ("El resultado de la resta es:", resta)
    print ("El resultado de la multiplicacion es:", multi)
    print ("El resultado de la division es:", divi)

#Los operadores relacionales se utilizan para comparar valores y devolver un resultado booleano. ><
def numeroso():
    cantidad = float(input("Ingrese un numero:"))
    if cantidad > 0:
     print("El numero ingresado es positivo")
    elif cantidad < 0:
     print ("El numero ingresado es negativo")
    else:
     print("El numero ingresado es 0")

#while (mientras): Permite ejecutar un bloque de código mientras una condición sea verdadera.
#for (para): Se utiliza para iterar sobre una secuencia
#Los operadores lógicos se utilizan para combinar o modificar condiciones en las expresiones lógicas. 
#and (y): Devuelve True si ambas condiciones son verdaderas.
#or (o): Devuelve True si al menos una de las condiciones es verdadera.
#not (no): Devuelve True si la condición es falsa y False si la condición es verdadera.
def pares():
    for a in range(2, 11, 2):
     print(a)

def suma_es_par(a, b):
    suma = a + b
    return suma % 2 == 0

def parametro():
    num1 = 3
    num2 = 5
    resul = suma_es_par(num1, num2)
    print(f"¿La suma de {num1} y {num2} es par? {resul}")


class Estudiante: #Se define una clase llamada Estudiante, que actúa como una plantilla para crear objetos que representan estudiantes.
    def __init__(self, nombre, edad, calificacion): #método especial __init__, que es el constructor de la clase. Este método se llama automáticamente cuando se crea un nuevo objeto de la clase.
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion #tiene tres parámetros: nombre, edad y calificacion

    def ha_aprobado(self): #Este método comprueba si la calificación del estudiante es mayor o igual a 60.
        if self.calificacion >= 60:
            return True
        else:
            return False
        
def alumno():
    estudiante1 = Estudiante("Manuel", 19, 81)
    estudiante2 = Estudiante("Harry", 19, 59)

    print(f"{estudiante1.nombre} ha aprobado: {estudiante1.ha_aprobado()}") #dos instancias 
    print(f"{estudiante2.nombre} ha aprobado: {estudiante2.ha_aprobado()}")

alumno()

while True: #while hace que el menu vuelva a aparecer
    print ("Laboratorio 3 - Manuel Medinilla 0901-22-1310")
    print("\nMenu Laboratorio 3:")
    print("1. Calculadora de operaciones aritmeticas")
    print("2. Numero positivo, negativo o 0")
    print("3. 10 primeros numeros pares")
    print("4. Parametros ")
    print("5. Clase estudiante")
    print("0. Salir")

    opcion = input("Seleccione una opcion (0-5): ")

    if opcion == "1":
        calculadora()
    elif opcion == "2":
        numeroso()
    elif opcion == "3":
        pares()
    elif opcion == "4":
        parametro()
    elif opcion == "5":
        alumno()
    elif opcion == "0":
        print("Programa terminado")
        break
    else:
        print("Opcion no valida. Por favor, seleccione una opcion valida.")