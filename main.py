
import pygame
import sys
sys.path.append('classes')
from pygame.locals import *
import util as game_util
from player import Player


#------CONSTS-------------------------
WINDOW_HEIGHT = 640
WINDOW_WIDTH = 480
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
FPS = 60
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
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zuzohell") 
icon = pygame.image.load('img/411.png')
pygame.display.set_icon(icon)
#spawn player
player = Player(WINDOW_WIDTH/2, WINDOW_HEIGHT * 0.9)
#------------Game Loop-----------------
running = True

while running:
    clock.tick(FPS)
    screen.fill(WHITE)

    input_keys = []

    #EVENT HANDLING
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False

        player.move()

    player.update_position()
    
    player.display(screen, RED)    
    pygame.display.update()


#-----------------------------------------
pygame.quit()





