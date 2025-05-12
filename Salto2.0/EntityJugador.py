
from Entity import *
from Controles import *
import threading
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
        self.shoot = False
        self.balas = []

    def imprimirXY(self):
        print("x : " + str(self.x) + " y : " + str(self.y))
    def movimiento(self, controles, mapa):   
        
        if(controles.W == True):
           #self.y -= self.speed
           pass
        if(controles.A == True):
            if(mapa.mapaNoseMueve and self.x > 0):
                self.x -= self.speed

        if(controles.S == True):
            #self.y += self.speed
            pass

        if(controles.D == True):
            if(self.x <= 400):
                self.x +=  self.speed
        
        # espacio
        if(controles.SP == True):
            self.saltando = True
        if(controles.K == True):
            self.shoot = True


    
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
    def disparo(self):
        if(self.shoot):
            self.balas.append( Entity("C:/Users/ignac/Desktop/plataform-main/saltooptimized-main/carpetaSprite/disparo.png", self.x + self.ancho,self.y + self.alto - self.alto/2 , 16,16) )
            self.shoot = False
    def moverDisparo(self):
            if(len(self.balas) > 0):
                for i in range(len(self.balas)):
                    self.balas[i]. x += 10

    def dibujarDisparo(self,screen):
         if(len(self.balas) > 0):
                for i in range(len(self.balas) ):
                    self.balas[i].pintar(screen)
                    
    
    def hilodisparo(self):
        pass
        


        
    
    
    

        
        
               
        
        
        
      
        

                 



       
            
                        