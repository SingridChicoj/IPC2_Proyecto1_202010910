from nodo_senal import nodo_senal
from grupo import grupo


class lista_senal:
    def __init__(self):
        self.primero = None
        self.contador_senal = 0
    
    def insertar_dato(self, senal):
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

    def calcular_patrones(self, nombre_senal):
        actual = self.primero
        while actual != None:
            if actual.senal.nombre == nombre_senal:
                actual.senal.PatronesTiempo = actual.senal.Lpatrones.devolver_patrones_tiempo(actual.senal.PatronesTiempo)
                actual.senal.PatronesTiempo.recorrer_imprimir()
                lista_patrones_temporal = actual.senal.PatronesTiempo
                grupos_sin_analizar = lista_patrones_temporal.coincidencias()
                print(grupos_sin_analizar)
                recolector_texto = ""
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito == ",":
                        recolector_texto += digito
                    elif digito == "-" and recolector_texto != "":
                        cadena_grupo = actual.senal.Ldatos.devolver_cadena_grupo(recolector_texto)
                        actual.senal.Lgrupo.insertar_dato(grupo = grupo(recolector_texto,cadena_grupo))
                        recolector_texto = ""
                    else:
                        recolector_texto = ""
                actual.senal.Lgrupo.recorrer_imprimir()
                return
            actual = actual.siguiente
        print ("No se encontró la carcel")