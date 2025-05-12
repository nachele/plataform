 
from Ventana import *;
from Entity import *;
from EntityJugador import *;
from Controles import *;
from Colisiones import *;
from Platforms import *;
from Monedas import *;
from Mapa import *;
from FpsCounter import *;
pygame.init()
pygame.font.init()

#creando la ventana 
screen = Ventana(800,800)
jugador = Jugador("C:/Users/ignac/Desktop/plataform-main/saltooptimized-main/carpetaSprite/fan.png",400,550,4,50,50,15,0.5)
plataformas = CrearPlataformas(5)
plataformas.crearArrayPlataformas()
colisiones = Colisiones(jugador,plataformas,screen)
monedas = Monedas(5)
monedas.crearMonedas()
mapa = Mapa()
mapa.recorriendoTexto()
bala = Entity("C:/Users/ignac/Desktop/plataform-main/saltooptimized-main/carpetaSprite/disparo.png", 450, 550, 16,16)


controles = Controles()
running = True
clock = pygame.time.Clock()
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.screen.fill("white")
    
    
    
    mapa.pintarMapa(screen.screen)
    controles.KeyDetection()
    
    
    jugador.movimiento(controles,mapa)
    mapa.moverMapa(controles,jugador)
    plataformas.moverPlataformas(controles,mapa,jugador)
    plataformas.pintarP(screen.screen)
    colisiones.ColisionDetection()
    jugador.ColisionPlataforma()
    jugador.gravedad()
    
    
    monedas.pintarMonedas(screen.screen)
    monedas.moverMonedas(controles,mapa,jugador)
    monedas.elimMonedas(jugador)
    monedas.iniciar_animacion()
    jugador.disparo()
    jugador.moverDisparo()
    jugador.dibujarDisparo(screen.screen)
    jugador.pintar(screen.screen)
   
    

    
    
    ContadorFps(clock, screen.screen, font)
    
    
    pygame.display.flip()
    # fill the screen with a color to wipe away anything from last frame
    clock.tick(60) # limits FPS to 60

pygame.quit()