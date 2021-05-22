import pygame
WINDOW_HEIGHT = 792
WINDOW_WIDTH = 1008

MAP_HEIGHT = 720
MAP_WIDTH = 672
MAP_OFFSET = 24

WORLD_CEILING =  -30

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
IDK_COLOR = (100, 23, 50)
FPS = 60

BASIC_BULLET_SPEED = 2
SLOWDOWN = 0.2

#later it will depend on difficulty level
SPAWN_TIME_MIN =  20
SPAWN_TIME_MAX = 100

SPEED_MIN = 0.3
SPEED_MAX = 1

#IMAGES

PLAYER_IMAGE = pygame.image.load('img/player.png')
MOB_IMAGE = pygame.image.load('img/mob5.png')

MAP_SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))

#GAME STATES

GAME_START = 1
GAME_PLAYING = 2
GAME_OVER = 3