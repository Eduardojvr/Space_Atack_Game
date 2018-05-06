import pygame

class Trap():
    def __init__(self, screen, posx):
        self.screen = screen
        # carrega imagem da nave
        self.image = pygame.image.load('imagens/trap.bmp') 
        # obtem o retângulo da imagem
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect()
        # inicia cada nova trap na parte inferior central da tela
        self.rect.centerx = posx
        
        # self.rect.bottom = self.screen_rect.bottom    

    # Desenha a trap em sua posição atual
    def blitme(self):
        self.screen.blit(self.image, self.rect)