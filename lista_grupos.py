from nodo_grupo import nodo_grupo

class lista_grupos():
    def __init__(self):
        self.primero = None
        self.contadorG = 0

    def insertar(self, grupo):
        if self.primero is None:
            self.primero = nodo_grupo(grupo = grupo)
            self.contadorG += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_grupo(grupo = grupo)
        self.contadorG += 1

    def recorrer_imprimir(self):
        print("Total de grupos almacenadas: ", self.contadorG)
        print("")
        print("")
        print("")
        print("------------------------------------------------")
        actual = self.primero
        while actual != None:
            print("Grupo: ", actual.grupo.el_grupo, "Cadena grupo: ", actual.grupo.Cgrupo)
            actual = actual.siguiente
        print("------------------------------------------------")