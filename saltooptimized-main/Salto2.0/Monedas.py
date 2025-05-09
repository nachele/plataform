
from Entity import *;
class Monedas:
    def __init__(self, index):
       
        self.monedas = []
        self.index = index
        self.monedasCogidas = 0
    def crearMonedas(self):
        for i in range(self.index):
            self.monedas.append(Entity("C:/Users/ignacio/Documents/_/saltooptimized-main/carpetaSprite/moneda.png", 200 * i, 50 * i,60,60))
    def pintarMonedas(self,screen):
        for i in range(len(self.monedas) - 1):
            if(self.monedas[i] != None):
                self.monedas[i].pintar(screen)
    def elimMonedas(self, jugador):
        for i in range(len(self.monedas) - 1):
            if(self.monedas[i] != None):

                if(jugador.x <= self.monedas[i].x + self.monedas[i].ancho and jugador.x + self.monedas[i].ancho >= self.monedas[i].x):
                    if(jugador.y <= self.monedas[i].y + self.monedas[i].alto and jugador.y + jugador.alto >= self.monedas[i].y):
                        #si colision con monedas desaparece del array
                        if(self.monedas[i] != None):
                            del self.monedas[i]
                            self.monedasCogidas += 1
        
            

