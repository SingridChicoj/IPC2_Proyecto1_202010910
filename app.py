import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename

#Clases
from senal import senal
from dato import dato

#Lista
from lista_datos import lista_datos
from lista_senales import lista_senales

#Abrir xml
ruta = askopenfilename()
nombre_archivo = open(ruta, "r")
nombre_archivo.close()

#Parsear para que nuestra aplicacion entienda que manipulara xml
tree = ET.parse(ruta)
raiz = tree.getroot()

#Lectura de xml
#Definimos mi lista que guarda todas mis senales
lista_senales_temporal = lista_senales()
for senales_temporal in raiz.findall('senal'):
    #Obteniendo atributos principales 
    nombre_senal = senales_temporal.get('nombre')
    t_senal = senales_temporal.get('t')
    A_senal = senales_temporal.get('A')
    print(nombre_senal, t_senal, A_senal)
    