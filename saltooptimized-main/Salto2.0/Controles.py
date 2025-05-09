import pygame
class Controles:
    def __init__(self):
        self.W = False
        self.A = False
        self.D = False
        self.S = False
        self.SP = False
        self.keys = ""
    def KeyDetection(self):
        self.keys = pygame.key.get_pressed()
        if self.keys[pygame.K_a]:
            self.A = True
        if self.keys[pygame.K_d]:
            self.D = True
        if self.keys[pygame.K_w]:
            self.W = True
        if self.keys[pygame.K_s]:
            self.S = True
        if self.keys[pygame.K_SPACE]:
            self.SP = True
        
        #teclas liberadas
        if not self.keys[pygame.K_a]:
            self.A = False
        if not self.keys[pygame.K_d]:
            self.D = False
        if not self.keys[pygame.K_w]:
            self.W = False
        if not self.keys[pygame.K_s]:
            self.S = False
            
        if not self.keys[pygame.K_SPACE]:
            self.SP = False
             