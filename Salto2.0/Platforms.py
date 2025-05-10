import pygame
from Entity import *;
class CrearPlataformas:
    def __init__(self,index):
        self.arrayPlataformas = []
        self.index = index
        self.velocidadPlataformas = 2
    def crearArrayPlataformas(self):
        for i in range(self.index):
            self.arrayPlataformas.append(Entity("C:/Users/ignac/Desktop/plataform-main/saltooptimized-main/carpetaSprite/s.png",200 * i,100 * i,60,200))
    def pintarP(self,screen):
        for i in range(len(self.arrayPlataformas) - 1):
            self.arrayPlataformas[i].pintar(screen)
    def moverPlataformas(self, controles):
        if controles.D:
            for i in range(len(self.arrayPlataformas) - 1):
                self.arrayPlataformas[i].x -= self.velocidadPlataformas
        if controles.A:
            for i in range(len(self.arrayPlataformas) - 1):
                self.arrayPlataformas[i].x += self.velocidadPlataformas
        