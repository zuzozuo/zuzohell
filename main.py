
import pygame
from pygame.locals import *
import util as game_util

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
player = []
boss = []
mobs = []
bullets = []

#-------------Init-------------------
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zuzohell") 
icon = pygame.image.load('img/411.png')
pygame.display.set_icon(icon)

#------------Game Loop-----------------
running = True

while running:
    clock.tick(FPS)

    screen.fill(WHITE)

    #EVENT HANDLING
    for event in pygame.event.get():
        #check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Wow")
    
    pygame.display.update()


#-----------------------------------------
pygame.quit()





