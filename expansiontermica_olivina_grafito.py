#2.5 EXPANSION TERMICA OLIVINA Y GRAFITO 

import expansiontermicamineral as exp

#Retorna: alfas, alfa promedio y error global de "olivine_angel_2017.csv"
#Muestra y guarda gráficas de Alfa(T) y V(T)
x = exp.ExpansionTermicaMineral.leer_archivo("olivine_angel_2017.csv")

#Retorna: alfas, alfa promedio y error global de "graphite_mceligot_2016.csv"
#Muestra y guarda gráficas de Alfa(T) y V(T)
y = exp.ExpansionTermicaMineral.leer_archivo("graphite_mceligot_2016.csv")
 
#print(x)
#print(y)