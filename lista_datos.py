from nodo_dato import nodo_dato

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

    def recorrer_imprimir(self):
        print("--------------------------------------------")
        actual = self.primero
        while actual != None:
            print("T: ", actual.dato.time, "A: ", actual.dato.amplitude, "Numero: ", actual.dato.numero)
            actual = actual.siguiente
        print("--------------------------------------------")

    def grafica(self, nombre_senal, tiempo, amplitud):
        f = open('bb.dot', 'w')
        #Estilo del grafo
        text = """
                digraph G {"tiempo = """ + tiempo + """", "Amplitud = """ + amplitud +""""->" """+ nombre_senal+""""
                bgcolor="#3990C4" style="filled" subgraph cluster1{fillcolor = "blue:red" style="filled"
                node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
                a0 [ label=<
                <TABLE border="0" cellspacing="10" cellpadding="10" 
                style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
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
                text += """<TD border = "3" bgcolor="pink"  gradientangle="315">"""+str(actual.dato.numero)+"""</TD>\n"""
            else: 
                text += """<TD border = "3" bgcolor="gray"  gradientangle="315">"""+str(actual.dato.numero)+"""</TD>\n"""
            actual = actual.siguiente
        text += """</TR></TABLE>>];
                }
                }\n"""
        f.write(text) 
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz\bin'
        os.system('dot -Tpng bb.dot -o grafo.png')
        print("Terminado")
