class VistaArbol:

    def mostrar_menu(self):
        print("\n===== ARBOL AVL =====")
        print("1. Insertar numero")
        print("2. Mostrar recorrido Inorden")
        print("3. Mostrar estructura del arbol")
        print("4. Salir")

    def pedir_opcion(self):
        return input("Seleccione una opcion: ")

    def pedir_numero(self):
        return int(input("Ingrese un numero: "))

    def mostrar_arbol(self, numeros):
        print("\nRecorrido Inorden:")
        print(numeros)

    def mostrar_mensaje(self, mensaje):
        print(mensaje)
