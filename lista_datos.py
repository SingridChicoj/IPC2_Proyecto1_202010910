from nodo_dato import nodo_dato

class lista_datos:
    def __init__(self):
        self.primero = None
        self.contador_datos = 0

    def insertar_dato(self, dato):
        #Si el primer nodo es nulo
        if self.primero is None:
            self.primero = nodo_dato(dato = dato)
            self.contador_datos += 1
            return
        #Temporal para recorrer nuestra lista
        actual = self.primero

        #Ejecuta el ciclo, mientras actual.siguiente exista
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_dato(dato = dato)
        self.contador_datos += 1

    def recorrer_imprimir(self):
        print("--------------------------------------------")
        actual = self.primero
        while actual != None:
            print("T: ", actual.dato.time, "A: ", actual.dato.amplitude, "Numero: ", actual.dato.numero)
            actual = actual.siguiente
        print("--------------------------------------------")
