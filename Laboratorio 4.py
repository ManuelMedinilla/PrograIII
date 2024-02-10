# Definición de la clase Cola
class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, elemento):
        self.items.append(elemento)

    def dequeue(self):
        return self.items.pop(0)

    def __len__(self):
        return len(self.items)

# Implementación de una pila
def implementar_pila():
    # Implementación de una pila
    pila = []

    def push(elemento):
        pila.append(elemento)

    def pop():
        if not pila:
            return "La pila está vacía"
        return pila.pop()

    def peek():
        if not pila:
            return "La pila está vacía"
        return pila[-1]

    # Invertir el orden de una lista
    lista = [1, 2, 3, 4, 5]
    print("Lista original:", lista)
    for elemento in lista:
        push(elemento)
    lista_invertida = []
    while pila:
        lista_invertida.append(pop())
    print("Lista invertida:", lista_invertida)

# Implementación de una cola
def implementar_cola():
    # Implementación de una cola
    cola = Cola()

    def enqueue(elemento):
        cola.enqueue(elemento)

    def dequeue():
        return cola.dequeue()

    def front():
        return cola.items[0] if cola.items else "La cola está vacía"

    # Simulación del proceso de atención en una fila
    for i in range(1, 6):
        enqueue("Cliente " + str(i))
    print("Atendiendo en orden:")
    while cola.items:
        print("Atendiendo a:", dequeue())

# Verificación de paréntesis balanceados
def verificar_parentesis_balanceados():
    # Verificación de paréntesis balanceados
    def balanceados(cadena):
        pila = []
        for caracter in cadena:
            if caracter == '(':
                pila.append(caracter)
            elif caracter == ')':
                if not pila:
                    return False
                pila.pop()
        return not pila

    cadena = input("Ingrese una cadena de paréntesis: ")
    if balanceados(cadena):
        print("Los paréntesis están balanceados.")
    else:
        print("Los paréntesis no están balanceados.")

# Implementación de una cola con dos pilas
def implementar_cola_con_pilas():
    # Implementación de una cola con dos pilas
    class ColaConPilas:
        def __init__(self):
            self.pila_entrada = []
            self.pila_salida = []

        def enqueue(self, elemento):
            self.pila_entrada.append(elemento)

        def dequeue(self):
            if not self.pila_salida:
                while self.pila_entrada:
                    self.pila_salida.append(self.pila_entrada.pop())
            if not self.pila_salida:
                return "La cola está vacía"
            return self.pila_salida.pop()

    cola_con_pilas = ColaConPilas()
    for i in range(1, 6):
        cola_con_pilas.enqueue("Cliente " + str(i))
    print("Atendiendo en orden:")
    for _ in range(5):
        print("Atendiendo a:", cola_con_pilas.dequeue())

# Revertir la mitad de una cola
def revertir_mitad_de_cola():
    # Revertir la mitad de una cola
    def revertir_mitad(cola):
        pila_auxiliar = []
        tamano_original = len(cola)

        for _ in range(tamano_original // 2):
            pila_auxiliar.append(cola.dequeue())

        while pila_auxiliar:
            cola.enqueue(pila_auxiliar.pop())

        for _ in range(tamano_original // 2):
            cola.enqueue(cola.dequeue())

    # Simulación de una cola
    cola = Cola()
    for i in range(1, 11):
        cola.enqueue(i)
    print("Cola original:", cola.items)
    revertir_mitad(cola)
    print("Cola con mitad revertida:", cola.items)

# Menú principal
while True:
    print("\nMenú:")
    print("1. Implementación de una Pila")
    print("2. Implementación de una Cola")
    print("3. Verificación de Paréntesis Balanceados")
    print("4. Implementación de una Cola con Dos Pilas")
    print("5. Revertir la Mitad de una Cola")
    print("0. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == "1":
        implementar_pila()
    elif opcion == "2":
        implementar_cola()
    elif opcion == "3":
        verificar_parentesis_balanceados()
    elif opcion == "4":
        implementar_cola_con_pilas()
    elif opcion == "5":
        revertir_mitad_de_cola()
    elif opcion == "0":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")
