import pygame

class Ship():
    def __init__(self, screen):
        self.screen = screen
        # carrega imagem da nave
        self.image = pygame.image.load('imagens/nave_game.bmp') 
        # obtem o retângulo da nave
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect()
        self.imagemissile = pygame.image.load('imagens/missile.bmp')
        self.rectmissile = self.imagemissile.get_rect()
	# inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom    
        self.rectmissile.bottom = self.rect.bottom
        self.vida = 15

    # Desenha a espaçonave em sua posição atual
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def blitmemissile(self):
        self.screen.blit(self.imagemissile, self.rect)

    def moveMissile(self):
        while self.rectmissile.bottom > 0:
            self.rectmissile.bottom -= 30
