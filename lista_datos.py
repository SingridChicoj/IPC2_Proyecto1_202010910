from nodo_dato import nodo_dato
from patron import patron

#Importaciones
import sys
import os

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

    def insertar_dato_ordenado(self, dato):
        nuevo_dato = nodo_dato(dato = dato)
        self.contador_datos += 1
        if self.primero is None:
            self.primero = nuevo_dato
            return
        if dato.time < self.primero.dato.time or (
            dato.time == self.primero.dato.time and dato.amplitude <= self.primero.dato.amplitude):
            nuevo_dato.siguiente = self.primero
            self.primero = nuevo_dato
            return
        actual = self.primero
        while actual.siguiente is not None and (
                dato.time > actual.siguiente.dato.time or(
                    dato.time == actual.siguiente.dato.time and dato.amplitude > actual.siguiente.dato.amplitude)):
            actual = actual.siguiente
        nuevo_dato.siguiente = actual.siguiente
        actual.siguiente = nuevo_dato

    
    def recorrer_imprimir(self):
        print("------------------------------------------------------")
        actual = self.primero
        while actual != None:
            print("T: ", actual.dato.time, "A: ", actual.dato.amplitude, "Numero: ", actual.dato.numero)
            actual = actual.siguiente
        print("------------------------------------------------------")
    

    def clear(self):
        if self.primero is not None:
            self.primero = None
            return
        actual = self.primero
        while actual is None:
            actual = actual
            actual = None
            return
        self.contador_datos = 0
    

    def graficaO(self, nombre_senal, tiempo, amplitud):
        f = open('bb.dot', 'w')
        #Estilo del grafo
        text = """
                digraph G {"tiempo = """ + tiempo + """", "Amplitud = """ + amplitud +""""->" """+ nombre_senal+""""
                bgcolor="#decfee" subgraph cluster1{fillcolor = "#9fdbe6:#7678bc" style="filled" 
                node [shape=rectangle fillcolor="#ca8bf5:#3e4160" gradientangle=90]
                a0 [ label=<
                <TABLE border="0" cellspacing="10" cellpadding="10" 
                bgcolor="#9fdbe6:#7678bc" gradientangle="315">\n"""
        actual = self.primero
        salto_linea_fila = actual.dato.time #Inicia en 1
        fila_inicial = False
        while actual != None:
            #Si mi fila actual es diferente a la que viene
            if salto_linea_fila != actual.dato.time:
                salto_linea_fila = actual.dato.time
                fila_inicial = False
                #Cerramos la fila
                text += """</TR>\n"""
            if fila_inicial == False: 
                fila_inicial = True
                #Abrir la fila
                text += """<TR>"""
                text += """<TD border = "2" bgcolor="#c9d2f5"  gradientangle="315">"""+str(actual.dato.numero)+"""</TD>\n"""
            else: 
                text += """<TD border = "2" bgcolor="#e5f3ee"  gradientangle="315">"""+str(actual.dato.numero)+"""</TD>\n"""
            actual = actual.siguiente
        text += """</TR></TABLE>>];
                }
                }\n"""
        f.write(text) 
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz\bin'
        os.system('dot -Tpng bb.dot -o grafo_original.png')
        print("Terminado")    

    def devolver_patrones_tiempo(self, PatronesTiempo):
        actual = self.primero
        salto_fila = actual.dato.time
        fila_inicial = False
        recoletor_patron = ""
        while actual != None:
            if salto_fila != actual.dato.time:
                fila_inicial = False
                PatronesTiempo.insertar_dato(patron(salto_fila, recoletor_patron))
                recoletor_patron = ""
                salto_fila = actual.dato.time
            if fila_inicial == False:
                fila_inicial == True
                recoletor_patron += str(actual.dato.numero) + "-"
            else:
                recoletor_patron += str(actual.dato.numero) + "-"
            actual = actual.siguiente
        PatronesTiempo.insertar_dato(patron(salto_fila, recoletor_patron))
        return PatronesTiempo

    def devolver_cadena_grupo(self, grupo):
        string_resultado = ""
        string_temporal = ""
        recolector_texto = ""
        for digito in grupo:
            if digito.isdigit():
                recolector_texto += digito
            else:
                string_temporal = ""
                #Recorremos la lista y recuperamos los valores para el grupo
                actual = self.primero
                while actual != None:
                    if actual.dato.time == int(recolector_texto):
                        string_temporal += actual.dato.numero + ","
                    actual = actual.siguiente
                string_resultado += string_temporal
                recolector_texto = ""
        return string_resultado
    
