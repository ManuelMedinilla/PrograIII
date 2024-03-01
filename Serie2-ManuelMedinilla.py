def listacomopa():
    print("Ingrese una lista como parámetro.")
    lista = input("Ingrese una lista de números separados por espacios: ").split()
    lista = [int(num) for num in lista]
    suma = sum(lista)
    print("La suma de los elementos de la lista es:", suma)

def cadin():
    palabra = input("Ingrese una palabra: ")
    inversa = palabra[::-1]
    print("La palabra invertida es:", inversa)

def sumpa():
    numeros = input("Ingrese una lista de números separados por espacios: ").split()
    numeros = [int(num) for num in numeros]
    suma_pares = sum(num for num in numeros if num % 2 == 0)
    print("La suma de los números pares en la lista es:", suma_pares)

def diccion():
    libro = {
        "título": "Halo Reach: El Jefe Maestro",
        "autor": "Microsoft",
        "año de publicación": 2012
    }
    libro["género"] = "accion"
    print("Diccionario del libro:", libro)

while True:
    print("Serie 2 - Primer Parcial - Manuel Medinilla 0901-22-1310")
    print("\nMenu:")
    print("1. Lista como parametro")
    print("2. Cadena invertida")
    print("3. Suma de números pares")
    print("4. Diccionario de un libro")
    print("0. Salir")

    opcion = input("Seleccione una opcion (0-4): ")

    if opcion == "1":
        listacomopa()
    elif opcion == "2":
        cadin()
    elif opcion == "3":
        sumpa()
    elif opcion == "4":
        diccion()
    elif opcion == "0":
        print("Programa terminado")
        break
    else:
        print("Opcion no valida. Por favor, seleccione una opcion valida.")
