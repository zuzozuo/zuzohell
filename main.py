
import pygame
from CONSTS import *
import sys
sys.path.append('classes')
from pygame.locals import *
import util as game_util
from player import Player

#------------------------------------
score = 0 

#------entities lists-----------------
boss = []
mobs = []
bullets = []
#--------event lists---------------
input_keys = []
#-------------Init-------------------
pygame.init()
clock = pygame.time.Clock()

WINDOW_SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
MAP_SCREEN = pygame.Surface((MAP_WIDTH , MAP_HEIGHT))
#play_screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zuzohell") 
icon = pygame.image.load('img/411.png')
pygame.display.set_icon(icon)
#spawn player
player = Player((MAP_WIDTH + MAP_OFFSET)/2 , (MAP_WIDTH + MAP_OFFSET) * 0.98)
#------------Game Loop-----------------
running = True

while running:
    clock.tick(FPS)
    MAP_SCREEN.fill(WHITE)
    WINDOW_SCREEN.fill(BLACK)
    WINDOW_SCREEN.blit(MAP_SCREEN,(MAP_OFFSET, MAP_OFFSET))
    input_keys = []

    #EVENT HANDLING
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False

    player.move()  
    player.update_position()
    player.check_border()
    
    player.display(WINDOW_SCREEN, RED)    
    pygame.display.update()


#-----------------------------------------
pygame.quit()





