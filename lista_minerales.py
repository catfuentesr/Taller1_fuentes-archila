#2.3 LISTA MINERALES Separar 

import mineral as min

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
        minerales.append(min.Mineral(nombre, dureza, rompimiento_por_fractura, color, composicion, lustre, specific_gravity, sistema_cristalino)) #Agrega datos a la matriz

#Escribir numero de minerales silicatos
def cantidad_minerales_silicatos(minerales):
    contador = 0
    for i in range(0,len(minerales)):
        if min.Mineral.silicato(minerales[i]) == True:
            contador += 1
    return contador

#Calcular la densidad promedio 
def calcular_densidad_promedio(minerales):
    suma_densidades = 0
    for i in range(0,len(minerales)):
        suma_densidades += min.Mineral.densidad(minerales[i])
    return suma_densidades / len(minerales)
        
