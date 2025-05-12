import pygame
#detecta para detectar la pulsacion y suelte de las teclas w,a,s,d
class Controles:
    #propiedades 
    def __init__(self):
        self.W = False
        self.A = False
        self.D = False
        self.S = False
        self.SP = False
        self.K = False
        self.keys = ""
    #metodos

    #si la tecla w,a,s,d es presionada se vuelve true la propiedad correspondiente por ejemplo: si a presionada entonces self.A = True 
    #si la tecla w,a,s,d es soltada se vuelve false la propiedad correspondiente por ejemplo: si a es soltada entonces self.A = False
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
        if self.keys[pygame.K_k]:
            self.K = True
    
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
        if not self.keys[pygame.K_k]:
            self.K = False
             