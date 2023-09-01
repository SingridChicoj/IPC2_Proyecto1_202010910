from nodo_patron import nodo_patron


class lista_patrones():
    def __init__(self):
        self.primero = None
        self.contadorP = 0

    def insertar_dato(self, patron):
        if self.primero is None:
            self.primero = nodo_patron(patron=patron)
            self.contadorP += 1
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo_patron(patron=patron)
        self.contadorP += 1

    def recorrer_imprimir(self):
        print("Total de patrones almacenadas: ", self.contadorP)
        print("")
        print("------------------------------------------------------")
        actual = self.primero
        while actual != None:
            print("Tiempo: ", actual.patron.tiempo,
                  "Cadena Patron: ", actual.patron.cadena_patron)
            actual = actual.siguiente
        print("------------------------------------------------------")

    def eliminar(self, tiempo):
        actual = self.primero
        anterior = None
        while actual and actual.patron.tiempo != tiempo:
            anterior = actual
            actual = actual.siguiente
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None

    def coincidencias(self):
        print("")
        print("")
        print("")
        resultado = ""  # Guarda mis coincidencias
        # Mientras la lista tenga algo y no este vacia
        while self.primero:
            actual = self.primero
            tiempo_string = ""
            while actual:
                #print(actual.patron.cadena_patron)
                if actual.patron.cadena_patron == self.primero.patron.cadena_patron:
                    tiempo_string += str(actual.patron.tiempo) + ","
                actual = actual.siguiente
            recolector_texto = ""
            for digito in tiempo_string:
                if digito.isdigit():
                    recolector_texto += digito
                else:
                    if recolector_texto != "":
                        self.eliminar(int(recolector_texto))
                        recolector_texto = ""
                    else:
                        recolector_texto = ""
            resultado += tiempo_string + "--"
        return resultado
