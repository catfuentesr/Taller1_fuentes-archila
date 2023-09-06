#MINERALES

import matplotlib.pyplot as plt
import numpy as np

#2.1 CLASE MINERAL
class Mineral:
    def __init__(self,nombre,dureza,rompimiento_por_fractura,color,composicion,lustre,specific_gravity,sistema_cristalino):
        self.nombre= nombre
        self.dureza= dureza
        self.lustre= lustre
        self.rompimiento_por_fractura= rompimiento_por_fractura
        self.color = color
        self.composicion=composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = specific_gravity

    def rompimiento(self): #Cambia TRUE a VERDADERO y FALSE a FALSO
        if 'TRUE' == self.rompimiento_por_fractura:
            return 'VERDADERO'
        else:
            return 'FALSO'
   
#2.2 MÉTODOS DE LA CLASE
    def silicato(self):
        if 'Si' in self.composicion and 'O' in self.composicion:
            return True
        else:
            return False
        
    
    def densidad(self):
        densidad_agua = 1000
        densidad_material = self.specific_gravity * densidad_agua
        return densidad_material 
    
    
    def color_graficado(nombre_mineral, minerales): #como van a meterle el mineral? por el nombre?
        for i in range(0,len(minerales)):
            if nombre_mineral == minerales[i].nombre:
                color_hex = minerales[i].color

        fig, ax = plt.subplots()
        ax.set_axis_off()
        fig.patch.set_facecolor(color_hex)
        plt.show()
#Probar abajo, despues de crear mineral Mineral.color_graficado("grafito",minerales)

    def caracteristicas(self):
        print("Dureza:", self.dureza)
        if self.rompimiento_por_fractura == True: 
            print("Tipo de rompimiento: Fractura")
        else:
            print("Tipo de rompimiento: Escisión")
        print("Sistema de organización de átomos:", self.sistema_cristalino)


#2.3 LISTA MINERALES Separar 
#Guardar minerales en arreglo 
minerales = [] 
with open("minerales.txt", "r") as archivo: #Leer el archivo 
    lineas = archivo.readlines() #Separar por líneas el archivo en una lista
    for linea in lineas[1:]: #Desde la 2da línea hasta la última
        datos = linea.strip().split("\t") #Cómo leer datos (separados por tabulación)
        nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino = datos #Guarda los elementos en variables individuales
        dureza = float(dureza)
        rompimiento_por_fractura = rompimiento_por_fractura == "TRUE" 
        specific_gravity = float(specific_gravity)
        minerales.append(Mineral(nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino)) #Agrega datos a la matriz




#Escribir numero de minerales silicatos
def cantidad_minerales_silicatos(minerales):
    contador = 0
    for i in range(0,len(minerales)):
        if Mineral.silicato(minerales[i]) == True:
            contador += 1
    return contador

#Calcular la densidad promedio 
def calcular_densidad_promedio(minerales):
    suma_densidades = 0
    for i in range(0,len(minerales)):
        suma_densidades += Mineral.densidad(minerales[i])
    return suma_densidades / len(minerales)
        

#2.4 EXPANSIÓN TÉRMICA MINERALES 

#Crear clase que hereda a la clase Mineral 
class ExpansionTermicaMineral(Mineral):
#Almacena datos en dos listas diferentes
    def leer_archivo(archivo_csv):
        temperaturas = [] 
        volumenes = []    
        with open(archivo_csv, "r") as archivo:
                    lineas = archivo.readlines()
                    for linea in lineas[1:]:  
                        temperatura, volumen = linea.strip().split(",")
                        temperaturas.append(float(temperatura))
                        volumenes.append(float(volumen))
 
#Cálculo de derivada
        dV = []
        dT = []
        alfas = []
        
    #Primera celda con método de diferencias por derecha
        V = (volumenes[1]-volumenes[0])/1
        dV.append(V)
        T = (temperaturas[1]-temperaturas[0])/(1)
        dT.append(T)
        alfa = (1/volumenes[0])*(V/T)
        alfas.append(alfa)
        
    #Celdas 2 a 9 con método de diferencias centrales   
        for i in range(1,len(volumenes)-1):
            V = (volumenes[i+1]-volumenes[i-1])/(2)
            dV.append(V)
            T = (temperaturas[i+1]-temperaturas[i-1])/(2)
            dT.append(T)
            alfa = (1/volumenes[i])*(V/T)
            alfas.append(alfa)
            
     #Última celda con método de diferencias por izquierda
        V = (volumenes[9]-volumenes[8])/1
        dV.append(V)
        T = (temperaturas[9]-temperaturas[8])/(1)
        dT.append(T)
        alfa = (1/volumenes[9])*(V/T)
        alfas.append(alfa)
        
        print("Los valores de alfa son:", alfas)
        
#Cálculo del error (desviación estándar)
        Error = np.std(alfas)
        print("El error global es:", Error)

#Gráfica V(T)
        plt.title("Gráfica Volumen vs. Temperatura")
        plt.scatter(volumenes,temperaturas,label='V(T)') 
        plt.xlabel("Temperatura (°C)")
        plt.ylabel("Volumen (cm³)")
        plt.legend()
        plt.savefig("V(T).jpg")
        plt.clf()
#Gráfica Alfa(T)

        plt.title("Alfa vs. Temperatura")
        plt.scatter(alfas,temperaturas,label='Alfa(T)') 
        plt.xlabel("Temperatura (°C)")
        plt.ylabel("Alfa (cm2/°C)")
        plt.legend()
        plt.savefig("Alfa(T).jpg")
        plt.clf()

#2.5 EXPANSION TERMICA OLIVINA Y GRAFITO 
#ExpansionTermicaMineral.leer_archivo("olivine_angel_2017.csv")
#ExpansionTermicaMineral.leer_archivo("graphite_mceligot_2016.csv")
 







