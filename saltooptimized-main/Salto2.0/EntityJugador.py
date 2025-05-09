
from Entity import *
from Controles import *
import time
class Jugador(Entity):
    def __init__(self, imagen,posX,posY,speed,transX,transY,fuerzaSalto,deceleracion):
        super().__init__(imagen,posX,posY,transX,transY)
        self.speed = speed


        
       
        self.ancho = transX
        self.alto = transY
        self.saltando = False
        self.choque = False
        self.suelo = posY + transY
        self.fuerzaSaltoInicial = fuerzaSalto
        self.fuerzaSalto = fuerzaSalto #20
        self.deceleracion = 0.3 #1
        self.choqueCabeza = False
        self.choquePie = False
        self.pisoPlataforma = 0
        self.enPlataforma = False
        self.graviti = 0.1
        self.gravedadInicial = 0.1


    def movimiento(self, controles):   
        if(controles.W == True):
           #self.y -= self.speed
           pass
        if(controles.A == True):
            self.x  -= self.speed

        if(controles.S == True):
            #self.y += self.speed
            pass

        if(controles.D == True):
            self.x += self.speed
        # espacio
        if(controles.SP == True):
            self.saltando = True


    
    def gravedad(self):
        #gravedad actuando sobre el muñeco
        self.y += self.graviti
        if(self.y + self.alto < self.suelo):
            self.graviti += self.deceleracion
        
        #si el muñeco esta en el suelo empuja con la misma fuerza que cae
        if (self.y + self.alto >= self.suelo or self.enPlataforma and self.choquePie ):
            
            self.graviti = self.gravedadInicial
            self.y -= self.graviti 
            self.saltando = False
            self.fuerzaSalto = self.fuerzaSaltoInicial

        #se le suma a graviti un poco de manera que graviti cada vez es mas  y es como si acelerara
    def salto(self): 
        #si presiona espacio se mueve hacia arriba con la fuerza de salto
        # a la cual se le va restando la gravedad y por eso cae.
        if(self.saltando):
            self.y -= self.fuerzaSalto

    def ColisionPlataforma(self):
        if(not self.choqueCabeza):
            self.salto()
        else:
           self.fuerzaSalto = 0
        #print(str(self.enPlataforma) + " " + str(self.choquePie))
        if(self.choquePie and self.enPlataforma):
            self.saltando = False
            self.graviti = self.gravedadInicial

        
            


        
    
    
    

        
        
               
        
        
        
      
        

                 



       
            
                        