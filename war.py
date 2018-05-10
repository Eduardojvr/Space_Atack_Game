from settings import Settings
from ship import Ship
import pygame
import sys
from trap import Trap
from time import clock
from random import randint

def run_game():
    tela1 = Settings()
    screen = pygame.display.set_mode((tela1.altura, tela1.largura))
    background = Settings()
    pygame.display.set_caption("Space War")
    nave = Ship(screen)
    #pygame.mouse.set_visible(0)
    trap = [Trap(screen,randint(0,1200)), Trap(screen,randint(0,1200)), Trap(screen,randint(0,1200))]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    nave.rect.centerx +=30
                elif event.key == pygame.K_LEFT:
                    nave.rect.centerx -=30
                elif event.key == pygame.K_UP:
                    nave.rect.bottom -=30
                elif event.key == pygame.K_DOWN:
                    nave.rect.bottom +=30
                elif event.key == pygame.K_SPACE:
                    nave.moveMissile()


        for i in trap:
            i.rect.bottom += 30
            if (i.rect.colliderect(nave.rect)):
                nave.vida = nave.vida-1
                if (nave.vida < 1):
                    background.bg_image = pygame.image.load('imagens/gameover.bmp')
                
        screen.fill(tela1.bg_color)
        screen.blit(background.bg_image, (0,0))
        nave.blitme()
        nave.blitmemissile()

        for i in trap:
            i.blitme()

        for i in trap:
            if i.rect.centery > Settings().altura:
                i.rect.centery = 0
                i.rect.centerx = randint(0,1200)
                i.rect.centery = randint(0,200)           
                 
        pygame.display.flip()
        
################################ Main ################################ 
run_game()

