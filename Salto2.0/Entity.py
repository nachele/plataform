import pygame
class Entity:
    def __init__(self,imagen,posX, posY, transX, transY):
        self.x = posX
        self.y = posY
        self.transX = transX
        self.transY = transY
        self.ancho = transX
        self.alto = transY
        self.imagen = pygame.transform.scale(pygame.image.load(imagen).convert_alpha(), (transX,transY))
       #pygame.image.load(imagen).convert_alpha()
    def pintar(self,screen):
        screen.blit(self.imagen,(self.x,self.y))
    def cuadroColision(self,screen):
        self.rect = self.imagen.get_rect(topleft = (self.x, self.y))
        borde_color = (255,0,0)
        borde_grosor = 5
        pygame.draw.rect(screen,borde_color,self.rect,borde_grosor)
