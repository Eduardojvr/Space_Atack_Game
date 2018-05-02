from settings import Settings
from ship import Ship
import pygame
import sys

def run_game():
    tela1 = Settings()
    screen = pygame.display.set_mode((tela1.altura, tela1.largura))
    background = Settings()
    pygame.display.set_caption("Space War")
    nave = Ship(screen)
    #pygame.mouse.set_visible(0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    nave.rect.centerx +=20
                elif event.key == pygame.K_LEFT:
                    nave.rect.centerx -=20
                elif event.key == pygame.K_UP:
                    nave.rect.bottom -=20
                elif event.key == pygame.K_DOWN:
                    nave.rect.bottom +=20

        screen.fill(tela1.bg_color)
        screen.blit(background.bg_image, (0,0))
        nave.blitme()        
        pygame.display.flip()
        
        
################################ Main ################################ 
run_game()

