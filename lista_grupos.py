from nodo_grupo import nodo_grupo
from dato import dato

#Importaciones
import sys
import os

class lista_grupos():
    def __init__(self):
        self.primero = None
        self.contadorG = 0

    def insertar_dato(self, grupo):
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
        print("------------------------------------------------------")
        actual = self.primero
        while actual != None:
            print("Numero de Grupo: ", actual.grupo.ngrupo, "Grupo: ", actual.grupo.el_grupo, "Cadena grupo: ", actual.grupo.cadena_grupo)
            print("Numeros: ", actual.grupo.cadena_grupo)
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
        self.contadorG = 0

    def graficaR(self, nombre_senal, amplitud):
        f = open('bb.dot', 'w')
        #Estilo del grafo
        text = """
                digraph G {"A = """ + amplitud +""""->" """+ nombre_senal+ "\n Reducida"""+""""
                bgcolor="#decfee" subgraph cluster1{fillcolor = "#9fdbe6:#7678bc" style="filled" 
                node [shape=rectangle fillcolor="#ca8bf5:#3e4160" gradientangle=90]
                a0 [ label=<
                <TABLE border="0" cellspacing="10" cellpadding="10" 
                bgcolor="#9fdbe6:#7678bc" gradientangle="315">\n"""
        actual = self.primero
        salto_linea_fila = actual.grupo.ngrupo #Inicia en 1
        fila_inicial = False
        while actual != None:
            #Si mi fila actual es diferente a la que viene
            if salto_linea_fila != actual.grupo.ngrupo:
                salto_linea_fila = actual.grupo.ngrupo
                fila_inicial = False
                #Cerramos la fila
                text += """</TR>\n"""
            if fila_inicial == False: 
                fila_inicial = True
                #Abrir la fila
                text += """<TR>"""
                text += """<TD border = "2" bgcolor="#c9d2f5"  gradientangle="315">"""+"g="+str(actual.grupo.ngrupo)+"  (t ="+str(actual.grupo.el_grupo)+")"+"""</TD>\n"""
                text += """<TD border = "2" bgcolor="#e5f3ee"  gradientangle="315">"""+str(actual.grupo.cadena_grupo)+"""</TD>\n"""
            actual = actual.siguiente
        text += """</TR></TABLE>>];
                }
                }\n"""
        f.write(text) 
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz\bin'
        os.system('dot -Tpng bb.dot -o grafo_reducida.png')
        print("Terminado")    