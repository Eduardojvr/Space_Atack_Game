import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Space War")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(":)")
    pygame.display.flip()
    run_game()

# main
run_game()

