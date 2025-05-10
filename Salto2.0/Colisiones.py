
class Colisiones:
    def __init__(self, jugador,plataformas,screen):
        self.jugador = jugador
        self.plataformas = plataformas
        self.screen = screen
    def ColisionDetection(self):
        #if(self.jugador.y <= self.bloque.y + self.bloque.alto and self.jugador.y >= self.bloque.y + self.bloque.alto - 10):
           # print("chocando por debajo")
            borde = 20
            dentrodeobjeto = 4
            self.jugador.enPlataforma = False
            self.jugador.choquePie = False
            for i in range (len(self.plataformas.arrayPlataformas)):
                #choque con el bloque en x 
                if(self.jugador.y <= self.plataformas.arrayPlataformas[i].y + self.plataformas.arrayPlataformas[i].alto - 10 and self.jugador.y + self.jugador.alto >= self.plataformas.arrayPlataformas[i].y + 10):   
                    if(self.jugador.x  + self.jugador.ancho >= self.plataformas.arrayPlataformas[i].x + dentrodeobjeto and self.jugador.x + self.jugador.ancho <= self.plataformas.arrayPlataformas[i].x + borde):
                        self.jugador.x -= self.jugador.speed
                        
                    if(self.jugador.x <= self.plataformas.arrayPlataformas[i].x + self.plataformas.arrayPlataformas[i].ancho - dentrodeobjeto and self.jugador.x >= self.plataformas.arrayPlataformas[i].x + self.plataformas.arrayPlataformas[i].ancho - borde):
                        self.jugador.x += self.jugador.speed
                        
                
                #choque con el bloque en y
                if(self.jugador.x  + self.jugador.ancho >= self.plataformas.arrayPlataformas[i].x + dentrodeobjeto and self.jugador.x <= self.plataformas.arrayPlataformas[i].x + self.plataformas.arrayPlataformas[i].ancho - dentrodeobjeto):
                    self.jugador.enPlataforma = True
                    if(self.jugador.y <= self.plataformas.arrayPlataformas[i].y + self.plataformas.arrayPlataformas[i].alto - dentrodeobjeto and self.jugador.y >= self.plataformas.arrayPlataformas[i].y + self.plataformas.arrayPlataformas[i].alto - borde):
                        #chocando cabeza por debajo del bloque
                        self.jugador.y += self.jugador.speed 
                        self.jugador.choqueCabeza = True
                    else:
                        self.jugador.choqueCabeza = False
                    if(self.jugador.y + self.jugador.alto >= self.plataformas.arrayPlataformas[i].y + dentrodeobjeto + 20 and self.jugador.y + self.jugador.alto <= self.plataformas.arrayPlataformas[i].y  + borde + 20 and self.jugador.x  + self.jugador.ancho >= self.plataformas.arrayPlataformas[i].x + dentrodeobjeto and self.jugador.x <= self.plataformas.arrayPlataformas[i].x + self.plataformas.arrayPlataformas[i].ancho - dentrodeobjeto):
                            #chocando pies por encima del bloque
                        self.jugador.enPlataforma = True
                        self.jugador.choquePie = True
                        
                    
                    


