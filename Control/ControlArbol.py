from Modelo.Nodo import Nodo
from Vista.VistaArbol import VistaArbol

class ControlArbol:

    def obtener_altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if nodo is None:
            return 0

        return (self.obtener_altura(nodo.izquierda) -
                self.obtener_altura(nodo.derecha))

    def rotacion_derecha(self, y):
        x = y.izquierda
        T2 = x.derecha

        x.derecha = y
        y.izquierda = T2

        y.altura = 1 + max(
            self.obtener_altura(y.izquierda),
            self.obtener_altura(y.derecha)
        )

        x.altura = 1 + max(
            self.obtener_altura(x.izquierda),
            self.obtener_altura(x.derecha)
        )

        return x

    def rotacion_izquierda(self, x):
        y = x.derecha
        T2 = y.izquierda

        y.izquierda = x
        x.derecha = T2

        x.altura = 1 + max(
            self.obtener_altura(x.izquierda),
            self.obtener_altura(x.derecha)
        )

        y.altura = 1 + max(
            self.obtener_altura(y.izquierda),
            self.obtener_altura(y.derecha)
        )

        return y

    def insertar(self, nodo, valor):

        if nodo is None:
            return Nodo(valor)

        if valor < nodo.valor:
            nodo.izquierda = self.insertar(
                nodo.izquierda, valor
            )

        elif valor > nodo.valor:
            nodo.derecha = self.insertar(
                nodo.derecha, valor
            )

        else:
            return nodo

        nodo.altura = 1 + max(
            self.obtener_altura(nodo.izquierda),
            self.obtener_altura(nodo.derecha)
        )

        balance = self.obtener_balance(nodo)

        if balance > 1 and valor < nodo.izquierda.valor:
            return self.rotacion_derecha(nodo)

        if balance < -1 and valor > nodo.derecha.valor:
            return self.rotacion_izquierda(nodo)

        if balance > 1 and valor > nodo.izquierda.valor:
            nodo.izquierda = self.rotacion_izquierda(
                nodo.izquierda
            )
            return self.rotacion_derecha(nodo)

        if balance < -1 and valor < nodo.derecha.valor:
            nodo.derecha = self.rotacion_derecha(
                nodo.derecha
            )
            return self.rotacion_izquierda(nodo)

        return nodo

    def inorden(self, nodo):
        if nodo is not None:
            return (
                self.inorden(nodo.izquierda)
                + [nodo.valor]
                + self.inorden(nodo.derecha)
            )

        return []

    def mostrar_arbol(self, nodo, nivel=0, prefijo="Raiz: "):
        self.vista = VistaArbol()

        if nodo is not None:
            self.vista.mostrar_mensaje(
                " " * (nivel * 5) + prefijo + str(nodo.valor)
            )

            self.mostrar_arbol(
                nodo.derecha, nivel + 1, "Derecha: "
            )

            self.mostrar_arbol(
                nodo.izquierda, nivel + 1, "Izquierda: "
            )