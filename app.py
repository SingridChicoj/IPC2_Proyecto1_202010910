import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename

#Clases
from senal import senal
from dato import dato

#Lista
from lista_datos import lista_datos
from lista_senal import lista_senal
from lista_patrones import lista_patrones
from lista_grupos import lista_grupos

jump = "------------------------------------------------------"

#Generalizando listas
lista_senales_temporal = lista_senal()
lista_datos_temporal = lista_datos()
lista_datos_patrones_temporal = lista_datos()

lista_patrones_temporal = lista_patrones()
lista_grupos_temporal = lista_grupos()

def cargar():
    #Abrir xml
    ruta = askopenfilename()
    nombre_archivo = open(ruta, "r")
    nombre_archivo.close()
    #Parsear para que nuestra aplicacion entienda que manipulara xml
    tree = ET.parse(ruta)
    raiz = tree.getroot()
    #Lectura de xml
    #Definimos mi lista que guarda todas mis senales
    for senal_temporal in raiz.findall('senal'):
        #Obteniendo atributos principales 
        nombre_senal = senal_temporal.get('nombre')
        t_senal = senal_temporal.get('t')
        A_senal = senal_temporal.get('A')
        #print(nombre_senal, t_senal, A_senal)
        #Inicializar nuestras listas)
        for dato_senal in senal_temporal.findall('dato'):
            tiempo_dato = dato_senal.get('t')
            ampli_dato = dato_senal.get('A')
            numero_dato = dato_senal.text
            nuevod = dato(int(tiempo_dato), int(ampli_dato), numero_dato)
            #Lista de datos
            lista_datos_temporal.insertar_dato_ordenado(nuevod)
            #Insercion en lista de patrones datos
            if numero_dato != "0":
                nuevod = dato(int(tiempo_dato), int(ampli_dato), 1)
                lista_datos_patrones_temporal.insertar_dato_ordenado(nuevod)
            else:
                nuevod = dato(int(tiempo_dato), int(ampli_dato), 0)
                lista_datos_patrones_temporal.insertar_dato_ordenado(nuevod)
        lista_senales_temporal.insertar_dato(senal(nombre_senal, t_senal, A_senal,
                                    lista_datos_temporal, lista_datos_patrones_temporal, lista_patrones_temporal, lista_grupos_temporal))

def menu():
    print(jump)
    print("Menu Principal:")
    print(jump)
    print("     1. Cargar archivo")
    print("     2. Procesar archivo")
    print("     3. Escribir archivo salida")
    print("     4. Mostrar datos del estudiante")
    print("     5. Generar gráfica") 
    print("     6. Inicializar sistema") 
    print("     7. Salida")
    print()
    entrada = input("Ingrese una opcion: ")
    print()
    print(jump)
    if entrada == "7":
        print("Adios, regresa pronto")
        quit()
    else:
        while entrada != "7":
            if entrada == "1":
                print("Cargando Archivo:")
                print()
                cargar()
                lista_senales_temporal.recorrer_imprimir()
                entrada = ""
                print("Archivo cargado...")
                print("")
                menu()
            elif entrada == "2":
                print("Procesando el archivo")
                print("")
                print("Calculando la matriz binaria")
                lista_senales_temporal.recorrer_imprimir_patrones()
                print("Mostrando grupos")
                lista_senales_temporal.calcular_patrones("Prueba1")
                entrada = ""
                menu()
            elif entrada == "3":
                print()
                lista_senales_temporal.escritura_xml()
                entrada = ""
                print("Se escribio el archivo, favor revisar")
                menu()
            elif entrada == "4":
                print("Datos del estudiante: ")
                print(" * Singrid Cristabel Chicoj Martinez", "\n",
                      "* 202010910",  "\n",
                      "* Introduccion a la Programacion y Computacion 2 Seccion D", "\n",
                      "* Ingenieria en Ciencias y Sistemas", "\n",
                      "* 4to Semestre y Parte del 5to Semeste :c")
                menu()
            elif entrada == "5":
                print("Tipos de Graficas")
                print("   1. Grafica Onda Original")
                print("   2. Grafica Onda Reducida")
                opcion = input("Seleccione una opcion: ")
                print()
                print(jump)
                if opcion == "1":
                    lista_senales_temporal.grafica_listaO()
                    menu()
                elif opcion == "2":
                    print("Proximamente")
                    #lista_senales_temporal.grafica_listaR()
                    menu()
            elif entrada == "6":
                print("Reiniciado")
                menu()
            else:
                print("Seleccione una opcion correcta")
                entrada = ""
                menu()

menu()
cargar()
#lista_senales_temporal.recorrer_imprimir_patrones()
#lista_senales_temporal.grafica_listaO()
#lista_senales_temporal.grafica_listaP()
lista_senales_temporal.calcular_patrones("Prueba1")
lista_senales_temporal.escritura_xml()
#lista_senales_temporal.grafica_listaR()