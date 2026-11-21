from Control.ControlArbol import ControlArbol
from Vista.VistaArbol import VistaArbol


class ArbolAVL:

    def __init__(self):

        self.arbol = ControlArbol()
        self.raiz = None
        self.vista = VistaArbol()

    def ejecutar(self):

        while True:

            self.vista.mostrar_menu()

            opcion = self.vista.pedir_opcion()

            if opcion == "1":

                try:
                    numero = self.vista.pedir_numero()

                    self.raiz = self.arbol.insertar(
                        self.raiz, numero
                    )

                    self.vista.mostrar_mensaje(
                        "Numero insertado correctamente."
                    )

                except ValueError:
                    self.vista.mostrar_mensaje(
                        "Debe ingresar un numero entero."
                    )

            elif opcion == "2":

                resultado = self.arbol.inorden(self.raiz)
                self.vista.mostrar_arbol(resultado)

            elif opcion == "3":

                self.vista.mostrar_mensaje(
                    "\nESTRUCTURA DEL ARBOL AVL:"
                )
                self.arbol.mostrar_arbol(self.raiz)

            elif opcion == "4":

                self.vista.mostrar_mensaje("Saliendo...")
                break

            else:
                self.vista.mostrar_mensaje("Opcion no valida.")
