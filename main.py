# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
def main():
    pygame.init()
    obj = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
   
    screen.fill((0, 0, 0), rect=None, special_flags=0) 
    pygame.display.flip()
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
            dt = dt - obj.tick(60)       
        player.draw(screen)


if __name__ == "__main__":
      main()  s