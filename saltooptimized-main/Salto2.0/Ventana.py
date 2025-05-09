import pygame
class Ventana:
    def __init__(self,anchoVentana,altoVentana):
        self.ancho = anchoVentana
        self.alto = altoVentana
        self.screen = pygame.display.set_mode((anchoVentana, altoVentana))

