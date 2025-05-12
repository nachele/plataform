from Entity import *;
class Mapa:
    def __init__(self):
        #es la forma del mapa en formato texto cada caracter representa una imagen del mapa 
        #c = cielo
        #f = suelo
        self.mapaTexto = ("ccccccccccccccccccccccccccccccccccccccccccccccccccc\n"
                     "ccccccccccccccccccccccccccccccccccccccccccccccccccccc\n"
                     "ccccccccccccccccccccccccccccccccccccccccccccccccccccc\n"
                     "ccccccccccccccccccccccccccccccccccccccccccccccccccccc\n"
                     "cccccccccccccccccccccccccccccccccccccccccccccccccccc\n"
                     "ccccccccccccccccccccccccccccccccccccccccccccccccccccc\n"
                     "fffffffffffffffffffffffffffffffffffffffffffffffffffff\n"
                     "fffffffffffffffffffffffffffffffffffffffffffffffffffff\n"
                     "fffffffffffffffffffffffffffffffffffffffffffffffffffff\n"
                     "fffffffffffffffffffffffffffffffffffffffffffffffffffff\n"
                     "fffffffffffffffffffffffffffffffffffffffffffffffffffff\n"
                     )
        
        self.matrizMapaTexto = [list(fila) for fila in self.mapaTexto.strip().splitlines()]
        self.index = 0
        self.matrizMapaImagenes = [[None for _ in fila] for fila in self.matrizMapaTexto]
        self.velocidadMapa = 2
        self.mapaNoseMueve = False
        #recorre todos los caracteres de mapatexto y segun que caracter encuentre introduce una imagen en matriz imagenes con la posicion que tendra en la pantalla
    def recorriendoTexto(self):
        for fila_idx, fila in enumerate(self.matrizMapaTexto):
            for col_idx, caractrer in enumerate(fila):
                self.matrizMapaImagenes[fila_idx][col_idx] = Entity("C:/Users/ignac/Desktop/plataform-main/saltooptimized-main/carpetaSprite/" + caractrer  + ".png",col_idx * 100, fila_idx * 100,100,100)
        #repinta todas las imagenes en la pantalla
    def pintarMapa(self,screen):
        for i in range(len(self.matrizMapaImagenes) - 1):
            for x in range(len(self.matrizMapaImagenes[i]) - 1):
                self.matrizMapaImagenes[i][x].pintar(screen)
        #si el mersonaje se mueve el mapa se mueve en la direccion opuesta para que de la sensacion de movimiento 
    def moverMapa(self, controles, jugador):
            if(self.matrizMapaImagenes[0][0].x >= 0):
                #hacer true para que el mapa no se mueva cuando pasa el principio
                self.mapaNoseMueve = True
            else:
                
                self.mapaNoseMueve = False

            for i in range(len(self.matrizMapaImagenes) - 1):
                for x in range(len(self.matrizMapaImagenes[i]) - 1):
                    if(controles.A and self.mapaNoseMueve == False):
                        self.matrizMapaImagenes[i][x].x += self.velocidadMapa
                    if(controles.D and jugador.x >= 400):
                        self.matrizMapaImagenes[i][x].x -= self.velocidadMapa
                        self.mapaNoseMueve = False
