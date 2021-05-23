import pygame
import pygame.mixer

pygame.mixer.init()

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1008

MAP_HEIGHT = 720
MAP_WIDTH = 672
WINDOW_OFFSET =  WINDOW_WIDTH - MAP_WIDTH

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
BOSS_IMAGE = pygame.image.load('img/boss.png')

MAP_SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))
#MAP_SCREEN = pygame.surface.Surface((MAP_WIDTH, MAP_HEIGHT))
WINDOW_SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

#GAME STATES

GAME_START = 1
GAME_PLAYING = 2
GAME_OVER = 3

#
MOBS_NUMBER = 3
MIN_BOSS_BULLETS_NUMBER = 10
MAX_BOSS_BULLETS_NUMBER = 20
#SOUNDS
FEAR_SOUND = pygame.mixer.Sound('Sounds/projekt.mp3')
LOSE_SOUND = pygame.mixer.Sound('Sounds/youlose2_sound.mp3')
BOSS_DEATH_SOUND = pygame.mixer.Sound('Sounds/dead_boss.mp3')
BOSS_APPEARS_SOUND = pygame.mixer.Sound('Sounds/weewee_sound.mp3')
PLAYER_BULLET_SOUND = pygame.mixer.Sound('Sounds/shoot1_sound.mp3')
PLAYER_DEATH_SOUND = pygame.mixer.Sound('Sounds/youlose2_sound.mp3')
GAME_OVER_SOUND = pygame.mixer.Sound('Sounds/youlose1_sound.mp3')

PLAYER_BOSS_DAMAGE = 0.5
PLAYER_MOB_DAMAGE=  0.75
MOB_PLAYER_DAMAGE = 0.4
BOSS_PLAYER_DAMAGE = 0.9

#FONTS

INFO_FONT_SIZE = 24
START_FONT_SIZE = 50


PLAYER_MAX_HP = 10
BOSS_MAX_HP = 10

#HEALTH BARS

HEALTH_BAR_WIDTH = 100
HEALTH_BAR_HEIGHT = 20



