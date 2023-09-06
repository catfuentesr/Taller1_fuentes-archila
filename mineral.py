#2.1 CLASE MINERAL

import matplotlib.pyplot as plt
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

#Saber si el mineral es silicato
    def silicato(self):
        if 'Si' in self.composicion and 'O' in self.composicion:
            return True
        else:
            return False
        
#Calcular la densidad del material
    def densidad(self):
        densidad_agua = 1000
        densidad_material = self.specific_gravity * densidad_agua
        return densidad_material 
    
#Visualizar el color del material deseado
    def color_graficado(nombre_mineral, minerales): #como van a meterle el mineral? por el nombre?
        for i in range(0,len(minerales)):
            if nombre_mineral == minerales[i].nombre:
                color_hex = minerales[i].color

        fig, ax = plt.subplots()
        ax.set_axis_off()
        fig.patch.set_facecolor(color_hex)
        plt.show()

#Imprimir dureza, tipo de rompimiento y el sistema de organización de átomos
    def caracteristicas(self):
        print("Dureza:", self.dureza)
        if self.rompimiento_por_fractura == True: 
            print("Tipo de rompimiento: Fractura")
        else:
            print("Tipo de rompimiento: Escisión")
        print("Sistema de organización de átomos:", self.sistema_cristalino)



#PREGUNTAR COLORR
#PREGUNTAR ERROR
