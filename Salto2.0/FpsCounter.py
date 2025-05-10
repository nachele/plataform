import pygame
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 24)
def ContadorFps(clock,screen,font):
    fps = clock.get_fps()
    fps_text = font.render(f"FPS:{fps:.2f}", True,(255,255,255))
    screen.blit(fps_text,(700,10))
