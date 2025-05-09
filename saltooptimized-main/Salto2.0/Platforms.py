import pygame
from Entity import *;
class CrearPlataformas:
    def __init__(self,index):
        self.arrayPlataformas = []
        self.index = index
    def crearArrayPlataformas(self):
        for i in range(self.index):
            self.arrayPlataformas.append(Entity("C:/Users/ignacio/Desktop/saltooptimized-main/carpetaSprite/s.png",200 * i,100 * i,60,200))
    def pintarP(self,screen):
        for i in range(len(self.arrayPlataformas)):
            self.arrayPlataformas[i].pintar(screen)