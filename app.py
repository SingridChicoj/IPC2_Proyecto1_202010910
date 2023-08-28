import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename

#Clases
from senal import senal
from dato import dato

#Lista
from lista_datos import lista_datos
from lista_senal import lista_senal

#Abrir xml
ruta = askopenfilename()
nombre_archivo = open(ruta, "r")
nombre_archivo.close()

#Parsear para que nuestra aplicacion entienda que manipulara xml
tree = ET.parse(ruta)
raiz = tree.getroot()

#Lectura de xml
#Definimos mi lista que guarda todas mis senales
lista_senales_temporal = lista_senal()
for senal_temporal in raiz.findall('senal'):
    #Obteniendo atributos principales 
    nombre_senal = senal_temporal.get('nombre')
    t_senal = senal_temporal.get('t')
    A_senal = senal_temporal.get('A')
    print(nombre_senal, t_senal, A_senal)
    #Inicializar nuestras listas
    lista_datos_temporal = lista_datos()
    lista_datos_patrones_temporal = lista_datos()
    for dato_senal in senal_temporal.findall('dato'):
        tiempo_dato = dato_senal.get('t')
        ampli_dato = dato_senal.get('A')
        numero_dato = dato_senal.text
        nuevod = dato(int(tiempo_dato), int(ampli_dato), numero_dato)
        #Lista de datos
        lista_datos_temporal.insertar_dato(nuevod)
        #Insercion en lista de patrones datos
        if numero_dato != "0":
            nuevod = dato(int(tiempo_dato), int(ampli_dato), 1)
            lista_datos_patrones_temporal.insertar_dato(nuevod)
        else:
            nuevod = dato(int(tiempo_dato), int(ampli_dato), 0)
            lista_datos_patrones_temporal.insertar_dato(nuevod)
    lista_senales_temporal.insertar_datos(senal(nombre_senal, t_senal, A_senal,
                                                lista_datos_temporal, lista_datos_patrones_temporal))
lista_senales_temporal.recorrer_imprimir()
#lista_senales_temporal.grafica_listaO()
lista_senales_temporal.grafica_listaP()