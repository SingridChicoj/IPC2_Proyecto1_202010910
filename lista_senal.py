from nodo_senal import nodo_senal

class lista_senal:
    def __init__(self):
        self.primero = None
        self.contador_senal = 0
    
    def insertar_datos(self, senal):
        if self.primero is None:
            self.primero = nodo_senal(senal= senal)
            self.contador_senal += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_senal(senal = senal)
        self.contador_senal += 1

    def recorrer_imprimir(self):
        print("Total de senales almacenadas: ", self.contador_senal)
        print("")
        print("")
        print("")
        print("------------------------------------------------")
        actual = self.primero
        while actual != None:
            print("Nombre: ", actual.senal.nombre, "Tiempo: ", actual.senal.tiempo, "Amplitud: ", actual.senal.amplitud)
            actual.senal.Ldatos.recorrer_imprimir()
            actual.senal.Lpatrones.recorrer_imprimir()
            actual = actual.siguiente
        print("------------------------------------------------")

    def grafica_listaO(self):
        actual = self.primero
        while actual != None:
            actual.senal.Ldatos.grafica(actual.senal.nombre, str(actual.senal.tiempo), str(actual.senal.amplitud))
            actual = actual.siguiente
    
    def grafica_listaP(self):
        actual = self.primero
        while actual != None:
            actual.senal.Lpatrones.grafica(actual.senal.nombre, str(actual.senal.tiempo), str(actual.senal.amplitud))
            actual = actual.siguiente