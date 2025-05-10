import time
import threading
from Entity import *;

class Monedas:
    def __init__(self, index):
        self.monedas = []
        self.index = index
        self.monedasCogidas = 0
        self.velociadMonedas = 2
        self.lock = threading.Lock()  # Usamos un Lock para evitar interferencias
        self.animacion_activa = False 
        self.ind = -1
        self.indx =0
    def crearMonedas(self):
        for i in range(self.index):
            self.monedas.append(Entity("C:/Users/ignac/Desktop/plataform-main/saltooptimized-main/carpetaSprite/moneda.png", 200 * i, 50 * i, 60, 60))

    def pintarMonedas(self, screen):
        for i in range(len(self.monedas) - 1 ):
            if self.monedas[i] is not None:
                self.monedas[i].pintar(screen)

    def elimMonedas(self, jugador):
        for i in range(len(self.monedas) - 1):
            if self.monedas[i] is not None:
                if (jugador.x <= self.monedas[i].x + self.monedas[i].ancho and 
                    jugador.x + self.monedas[i].ancho >= self.monedas[i].x):
                    if (jugador.y <= self.monedas[i].y + self.monedas[i].alto and 
                        jugador.y + jugador.alto >= self.monedas[i].y):
                        if self.monedas[i] is not None:
                            del self.monedas[i]
                            self.monedasCogidas += 1

    def moverMonedas(self, controles):
        for i in range(len(self.monedas) - 1):
            if controles.D:
                self.monedas[i].x -= self.velociadMonedas
            if controles.A:
                self.monedas[i].x += self.velociadMonedas

    def animacionMonedas(self):
        for i in range(33):
            time.sleep(0.1)
            for x in range(len(self.monedas)):
                 #self.monedas[x] = Entity("C:/Users/ignac/Desktop/plataform-main/saltooptimized-main/carpetaSprite/moneda" + str(i) +  ".png", 200 * x, 50 * x, 60, 60)
                self.monedas[x].imagen = pygame.image.load("C:/Users/ignac/Desktop/plataform-main/saltooptimized-main/carpetaSprite/moneda" + str(i) +  ".png")
        self.animacion_activa = False
    


               

        
            
            

    def iniciar_animacion(self):
        # Creamos el hilo para la animación
        if not self.animacion_activa:
            self.animacion_activa = True
            hilo = threading.Thread(target=self.animacionMonedas, daemon=True)
            hilo.start()


           
        
            

