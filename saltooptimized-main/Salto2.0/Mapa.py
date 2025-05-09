from Entity import *;
class Mapa:
    def __init__(self):
        self.mapaTexto = ("cccccccccccccccccccccccccccc\n"
                     "ccccccccccccccccccccccccccccccccc\n"
                     "cccccccccccccccccccccccccccccccccc\n"
                     "cccccccccccccccccccccccccccccccccc\n"
                     "cccccccccccccccccccccccccccccccccc\n"
                     "fffffffffffffffffccccccccccccccccc\n"
                     "fffffffffffffffffccccccccccccccccc\n"
                     "fffffffffffffffffcccccccccccccccccc\n"
                     "ffffffffffffffffffffffffffffffffff\n"
                     "ffffffffffffffffffffffffffffffffff\n"
                     "ffffffffffffffffffffffffffffffffff\n"
                     )
        
        self.matrizMapaTexto = [list(fila) for fila in self.mapaTexto.strip().splitlines()]
        self.index = 0
        self.matrizMapaImagenes = [[None for _ in fila] for fila in self.matrizMapaTexto]
    def recorriendoTexto(self):
        for fila_idx, fila in enumerate(self.matrizMapaTexto):
            for col_idx, caractrer in enumerate(fila):
                self.matrizMapaImagenes[fila_idx][col_idx] = Entity("C:/Users/ignacio/Desktop/saltooptimized-main/carpetaSprite/" + caractrer  + ".png",col_idx * 100, fila_idx * 100,100,100)
    def pintarMapa(self,screen):
        for i in range(len(self.matrizMapaImagenes) - 1):
            for x in range(len(self.matrizMapaImagenes[i]) - 1):
                self.matrizMapaImagenes[i][x].pintar(screen)