import pygame
import pygame.mixer

pygame.mixer.init()

WINDOW_HEIGHT = 720
WINDOW_WIDTH = 1008
WINDOW_SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
MAP_HEIGHT = 720
MAP_WIDTH = 672
WINDOW_OFFSET = WINDOW_WIDTH - MAP_WIDTH
WORLD_CEILING =  -30
FPS = 60

#COLORS
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
IDK_COLOR = (100, 23, 50)

#GAME PROPERTIES
MIN_BULLET_SPEED = 2.5
MAX_BULLET_SPEED = 4.5

DEFAULT_BULLET_RADIUS = 7
PLAYER_RADIUS = 30
BOSS_RADIUS = 60
MOB_RADIUS = 25

#later it will depend on difficulty level
SPAWN_TIME_MIN =  20
SPAWN_TIME_MAX = 100

SPEED_MIN = 0.5
SPEED_MAX = 1

MIN_NUMBER_TO_KILL = 1 #HOW MANY SHOULD YOU KILL TO MAKE THE BOSS APPEAR
MAX_NUMBER_TO_KILL = 3

MIN_MOBS_NUMBER = 1 #HOW MANY MOBS AT ONE TIME CAN BE SUMMONED
MAX_MOB_NUMBER = 3

MIN_BOSS_BULLETS_NUMBER = 15
MAX_BOSS_BULLETS_NUMBER = 25

#HOW MANY BOSSES
BOSS_NUMBER = 1

PLAYER_MAX_HP = 10
BOSS_MAX_HP = 10

#SCORES
KILL_MOB_SCORE = 1
KILL_BOSS_SCORE = 2
HIT_MOB_SCORE = 0.45
HIT_BOSS_SCORE = 0.15

PLAYER_BOSS_DAMAGE = 0.15
PLAYER_MOB_DAMAGE=  0.70
MOB_PLAYER_DAMAGE = 0.4
BOSS_PLAYER_DAMAGE = 0.75
MOB_PLAYER_COLLISION_DAMAGE = 0.00000000062

#GAME STATES
GAME_START = 1
GAME_PLAYING = 2
GAME_OVER = 3
GAME_WIN = 4

#IMAGES

PLAYER_IMAGE = pygame.image.load('img/player.png')
BULLET_PLAYER_IMAGE = pygame.image.load('img/player_bullet.png')
BULLET_IMAGE_BLUE = pygame.image.load('img/bullet3.png')
BULLET_IMAGE_ORANGE = pygame.image.load('img/bullet5.png')
BULLET_IMAGE_GREEN = pygame.image.load('img/bullet4.png')
MOB_IMAGE = pygame.image.load('img/mob2.png')
BOSS_IMAGE = pygame.image.load('img/boss.png')
ALL_BULLETS = [BULLET_IMAGE_BLUE, BULLET_IMAGE_GREEN, BULLET_IMAGE_ORANGE]

#SOUNDS
FEAR_SOUND = pygame.mixer.Sound('Sounds/projekt.mp3')
LOSE_SOUND = pygame.mixer.Sound('Sounds/youlose2_sound.mp3')
BOSS_DEATH_SOUND = pygame.mixer.Sound('Sounds/dead_boss.mp3')
BOSS_APPEARS_SOUND = pygame.mixer.Sound('Sounds/weewee_sound.mp3')
PLAYER_BULLET_SOUND = pygame.mixer.Sound('Sounds/shoot1_sound.mp3')
PLAYER_DEATH_SOUND = pygame.mixer.Sound('Sounds/youlose2_sound.mp3')
GAME_OVER_SOUND = pygame.mixer.Sound('Sounds/youlose1_sound.mp3')
GAME_WIN_SOUND = pygame.mixer.Sound('Sounds/win_sound.wav')
GAME_WIN_MUSIC = pygame.mixer.Sound('Sounds/game_win_music_2.mp3')
PLAYER_HURT_SOUND = pygame.mixer.Sound('Sounds/gethurt_sound.mp3')
BACKGROUND_MUSIC = pygame.mixer.Sound('Sounds/background_music_2.mp3')
MENU_MUSIC = pygame.mixer.Sound('Sounds/menu_music_2.mp3')
GAME_OVER_MUSIC = pygame.mixer.Sound('Sounds/game_over_music_2.mp3')

#FONTS
INFO_FONT_SIZE = 24
START_FONT_SIZE = 50





