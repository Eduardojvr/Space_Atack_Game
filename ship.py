import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        # carrega imagem da nave
        self.image = pygame.image.load('imagens/nave_game.bmp') 
        # obtem o retângulo da nave
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect()
        # inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom    

    # Desenha a espaçonave em sua posição atual
    def blitme(self):
        self.screen.blit(self.image, self.rect)


