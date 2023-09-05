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
            actual = None
        self.contadorG = 0

    def graficaR(self, nombre_senal, ngrupo, amplitud):
        nombre_senal = "Matriz Reducida"
        f = open('bb.dot', 'w')
        #Estilo del grafo
        text = """
                digraph G {"A = """ + amplitud + """", "g = """ + ngrupo +""""->" """+ nombre_senal+""""
                bgcolor="#3990C4" style="filled" subgraph cluster1{fillcolor = "blue:red" style="filled"
                node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
                a0 [ label=<
                <TABLE border="0" cellspacing="10" cellpadding="10" 
                style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        salto_linea_fila = actual.grupo.el_grupo #Inicia en 1
        fila_inicial = False
        while actual != None:
            #Si mi fila actual es diferente a la que viene
            if salto_linea_fila != actual.grupo.el_grupo:
                salto_linea_fila = actual.grupo.el_grupo
                fila_inicial = False
                #Cerramos la fila
                text += """</TR>\n"""
            if fila_inicial == False: 
                fila_inicial = True
                #Abrir la fila
                text += """<TR>"""
                text += """<TD border = "3" bgcolor="pink"  gradientangle="315">"""+"g="+str(actual.grupo.ngrupo)+"  (t ="+str(actual.grupo.el_grupo)+")"+"""</TD>\n"""
                text += """<TD border = "3" bgcolor="gray"  gradientangle="315">"""+str(actual.grupo.cadena_grupo)+"""</TD>\n"""
            actual = actual.siguiente
        text += """</TR></TABLE>>];
                }
                }\n"""
        f.write(text) 
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz\bin'
        os.system('dot -Tpng bb.dot -o grafo.png')
        print("Terminado")    