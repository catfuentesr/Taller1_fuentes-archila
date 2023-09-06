#2.4 EXPANSIÓN TÉRMICA MINERALES

import matplotlib.pyplot as plt
import numpy as np
import mineral as min 

#Crear clase que hereda a la clase Mineral 
class ExpansionTermicaMineral(min.Mineral):
    
#Almacenar datos en dos listas diferentes
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
        
    #Promedio de afas
        alfa_promedio = np.min(alfas)      
        
#Cálculo del error (desviación estándar)
        Error = np.std(alfas)

#Gráfica V(T)
        plt.title("Gráfica Volumen vs. Temperatura")
        plt.scatter(volumenes,temperaturas,label='V(T)') 
        plt.xlabel("Temperatura (°C)")
        plt.ylabel("Volumen (cm³)")
        plt.legend()
        plt.savefig("V(T).jpg")
        plt.show()
        plt.clf()

#Gráfica Alfa(T)

        plt.title("Alfa vs. Temperatura")
        plt.scatter(alfas,temperaturas,label='Alfa(T)') 
        plt.xlabel("Temperatura (°C)")
        plt.ylabel("Alfa (cm2/°C)")
        plt.legend()
        plt.savefig("Alfa(T).jpg")
        plt.show()
        plt.clf()

        return alfas, alfa_promedio, Error
    

