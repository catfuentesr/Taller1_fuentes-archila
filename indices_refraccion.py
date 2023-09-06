import matplotlib.pyplot as plt
import numpy as np

def long_de_onda_vs_indice_de_refraccion(archivo):
    dic = []
    a = open(archivo, "r", encoding = "UTF-8")
    linea = ""
    while "data: |" not in linea:
        linea = a.readline()
    linea = a.readline()
    while linea != "" and "SPECS:" not in linea:
        datos = linea.strip("\n").split(" ")
        tupla = (datos[-2],datos[-1])
        dic.append(tupla)
        linea = a.readline()
    a.close()
    return dic
    

#print(long_de_onda_vs_indice_de_refraccion("Adhesivos_Opticos\Iezzi.yml"))

def graficar_kapton():
    datos = long_de_onda_vs_indice_de_refraccion("Plásticos_Comerciales\French.yml")
    x = []
    y = []
    for i in datos:
        try:
            x.append(float(i[0]))
            y.append(float(i[1]))
        except:
            continue
    n_promedio = round(sum(y)/len(y), 4)
    desviacion_estandar = round(np.std(y), 4)
    plt.plot(x, y)
    plt.xlabel("Longitud de onda")
    plt.ylabel("Índice de refracción")
    plt.title(f"Kapton, n promedio = {n_promedio}, desviación estándar = {desviacion_estandar}")
    plt.show()

#graficar_kapton()
    
def graficar_NOA138():
    datos = long_de_onda_vs_indice_de_refraccion("Adhesivos_Opticos\Joseph.yml")
    x = []
    y = []
    for i in datos:
        try:
            x.append(float(i[0]))
            y.append(float(i[1]))
        except:
            continue
    n_promedio = round(sum(y)/len(y), 4)
    desviacion_estandar = round(np.std(y), 4)
    plt.plot(x, y)
    plt.xlabel("Longitud de onda")
    plt.ylabel("Índice de refracción")
    plt.title(f"NOA138, n promedio = {n_promedio}, desviación estándar = {desviacion_estandar}")
    plt.show()
    
#graficar_NOA138()

def graficar(material):
    datos = long_de_onda_vs_indice_de_refraccion(material)
    x = []
    y = []
    for i in datos:
        try:
            x.append(float(i[0]))
            y.append(float(i[1]))
        except:
            continue
    n_promedio = round(sum(y)/len(y), 4)
    desviacion_estandar = round(np.std(y), 4)
    nombres = material.split("\\")
    print(nombres)
    carpeta = nombres[-2]
    nombre = nombres[-1]
    plt.plot(x, y)
    plt.xlabel("Longitud de onda")
    plt.ylabel("Índice de refracción")
    plt.title(f"{nombre}, n promedio = {n_promedio}, desviación estándar = {desviacion_estandar}")
    plt.savefig(f"{carpeta}\{nombre}.png")
    plt.show()
    
#graficar("Mezclas\Mathar-1.3.yml")

def graficar_todo():
    archivo = "indices_refraccion.csv"
    a = open(archivo, "r", encoding="UTF-8")
    a.readline()
    linea = a.readline()
    while linea != "":
        datos = linea.strip("\n").split(",")
        carpeta = datos[0]
        documento = datos[3].split("/")[-1]
        graficar(f"{carpeta}\{documento}")
        linea = a.readline()
    a.close()

#graficar_todo()