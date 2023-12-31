from nodo_senal import nodo_senal
from grupo import grupo

#Importaciones
import xml.etree.ElementTree as ET

class lista_senal:
    def __init__(self):
        self.primero = None
        self.contador_senal = 0
    
    def clear(self):
        self.primero = None
        self.contador_senal = 0
    
    def insertar_dato(self, senal):
        if self.primero is None:
            self.primero = nodo_senal(senal = senal)
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
        print("------------------------------------------------------")
        actual = self.primero
        while actual != None:
            print("Nombre: ", actual.senal.nombre, "Tiempo: ", actual.senal.tiempo, "Amplitud: ", actual.senal.amplitud)
            actual.senal.Ldatos.recorrer_imprimir()
            actual = actual.siguiente
    
    def recorrer_imprimir_patrones(self):
        print("Total de patrones almacenadas: ", self.contador_senal)
        print("")
        print("------------------------------------------------------")
        actual = self.primero
        while actual != None:
            print("Nombre: ", actual.senal.nombre, "Tiempo: ", actual.senal.tiempo, "Amplitud: ", actual.senal.amplitud)
            actual.senal.Lpatrones.recorrer_imprimir()
            actual = actual.siguiente

    def grafica_listaO(self):
        actual = self.primero
        while actual != None:
            actual.senal.Ldatos.graficaO(actual.senal.nombre, str(actual.senal.tiempo), str(actual.senal.amplitud))
            actual = actual.siguiente
    
    def grafica_listaP(self):
        actual = self.primero
        while actual != None:
            actual.senal.Lpatrones.grafica(actual.senal.nombre, str(actual.senal.tiempo), str(actual.senal.amplitud))
            actual = actual.siguiente

    def grafica_listaR(self):
        actual = self.primero
        while actual != None:
            actual.senal.Lgrupo.graficaR(actual.senal.nombre, str(actual.senal.amplitud))
            actual = actual.siguiente

    
    def calcular_patrones(self, nombre_senal):
        nombreS = nombre_senal
        actual = self.primero
        while actual != None:
            if actual.senal.nombre == nombre_senal or nombre_senal == nombreS:
                actual.senal.PatronesTiempo = actual.senal.Lpatrones.devolver_patrones_tiempo(actual.senal.PatronesTiempo)
                actual.senal.PatronesTiempo.recorrer_imprimir()
                lista_patrones_temporal = actual.senal.PatronesTiempo
                grupos_sin_analizar = lista_patrones_temporal.coincidencias()
                print(grupos_sin_analizar)
                recolector_texto = ""
                ngrupo = 0
                for digito in grupos_sin_analizar:
                    if digito.isdigit() or digito == ",":
                        recolector_texto += digito
                    elif digito == "-" and recolector_texto != "":
                        ngrupo += 1
                        cadena_grupo = actual.senal.Ldatos.devolver_cadena_grupo(recolector_texto)
                        actual.senal.Lgrupo.insertar_dato(grupo = grupo(recolector_texto,cadena_grupo, ngrupo))
                        '''for datoC in cadena_grupo:
                            for dato in datoC:
                                if dato  == "\n":'''
                        recolector_texto = ""
                    else:
                        recolector_texto = ""
                actual.senal.Lgrupo.recorrer_imprimir()
                return
            actual = actual.siguiente
        print ("No se encontró la carcel")


    def escritura_xml(self):
        mis_senales = ET.Element("senalesReducidas")
        actual = self.primero
        while actual != None:
            lista_senal = ET.SubElement(mis_senales,"senal " + " nombre="+actual.senal.nombre+"   A="+str(actual.senal.amplitud))
            actualLgrupo = actual.senal.Lgrupo.primero
            while actualLgrupo != None:
                num_grupo = ET.SubElement(lista_senal, "grupo " + "grupo=" + str(actualLgrupo.grupo.ngrupo))
                grupos = ET.SubElement(num_grupo, "tiempos")
                grupos.text = str(actualLgrupo.grupo.el_grupo)
                dgrupos = ET.SubElement(num_grupo, "datosGrupo")
                dato = ET.SubElement(dgrupos, "datos")
                dato.text = str(actualLgrupo.grupo.cadena_grupo)
                actualLgrupo = actualLgrupo.siguiente
            actual = actual.siguiente

            #General xml
            my_data = ET.tostring(mis_senales)
            my_data = str(my_data)
            self.pretty(mis_senales)
            arbol_xml = ET.ElementTree(mis_senales)
            ruta = input("Escribir una ruta especifica: ")
            arbol_xml.write(ruta, encoding = "UTF-8", xml_declaration = True)
            #arbol_xml.write('salida.xml', encoding = "UTF-8", xml_declaration = True)
    
    def pretty(self, element, indent = '    '):
        cola = [(0, element)]
        while cola:
            level, element = cola.pop(0)
            hijos = [(level + 1, hijo) for hijo in list(element)]
            if hijos:
                element.text = '\n' + indent * (level + 1)
            if cola:
                element.tail = '\n' + indent * cola[0][0]
            else:
                element.tail = '\n' + indent * (level - 1)
            cola[0:0] = hijos