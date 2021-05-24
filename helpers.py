from entities import *
from bullet import Bullet
from mob import Mob
from CONSTS import *
import math
import random
import pygame
import pygame.mixer
import pygame.freetype

def sound_init():
    pygame.mixer.set_num_channels(100)
    pygame.mixer.set_reserved(0)
    pygame.mixer.set_reserved(1)
    pygame.mixer.set_reserved(2)
    pygame.mixer.set_reserved(3)
    pygame.mixer.Sound.set_volume(BACKGROUND_MUSIC, 0.3)
    pygame.mixer.Sound.set_volume(PLAYER_DEATH_SOUND, 1.2)
    pygame.mixer.Sound.set_volume(PLAYER_HURT_SOUND, 0.3)
    pygame.mixer.Sound.set_volume(BOSS_DEATH_SOUND, 0.5)
    pygame.mixer.Sound.set_volume(BOSS_APPEARS_SOUND, 0.5)
    pygame.mixer.Sound.set_volume(PLAYER_BULLET_SOUND, 0.1)
    pygame.mixer.Sound.set_volume(GAME_WIN_SOUND, 0.3)
    pygame.mixer.Sound.set_volume(GAME_WIN_MUSIC, 0.2)

def add_mob():
    mob = Mob(random.randint(0,int(MAP_WIDTH/30)) * 30, WORLD_CEILING - 30)
    mob.init()
    mobs.append(mob)

def add_bullets(x, y):
    bullet = Bullet(x, y)
    bullet.image = pygame.transform.scale(BULLET_PLAYER_IMAGE.convert(), (2 * bullet.radius, 2 * bullet.radius))
    bullet.transColor = BULLET_PLAYER_IMAGE.get_at((0,0))
    bullet.image.set_colorkey(bullet.transColor)
    bullets.append(bullet)


def add_mob_bullets(x,y):

    angle = random.random() - 0.5
    bullet = Bullet(x, y)
    velocity_y = random.random() * (MAX_BULLET_SPEED - MIN_BULLET_SPEED + 1) + MIN_BULLET_SPEED
    bullet.velocity = pygame.Vector2(0, velocity_y).rotate_rad(angle)
    bullet.color = IDK_COLOR
    mob_bullets.append(bullet)

def add_boss_bullets(x, y, radius, sequence_number, bullets_number):

    step = 2 * math.pi / bullets_number #calculate radians

    for i in range(0, bullets_number):
        x_spawn = x + math.sin(step * i) * radius
        y_spawn = y + math.cos(step * i) * radius
        bullet = Bullet(x_spawn, y_spawn)
        bullet.color = RED

        if sequence_number == 0:
            bullet.velocity = pygame.Vector2(0, MIN_BULLET_SPEED).rotate_rad(-1 * step * i )

        if sequence_number == 1:
            angle = random.random() - 0.5
            bullet.velocity = pygame.Vector2(0,0)
            bullet.velocity = pygame.Vector2(0, MIN_BULLET_SPEED).rotate_rad(angle)

        if sequence_number == 2:
            bullet.velocity = pygame.Vector2(0, random.randint(2,5)).rotate_rad(1 * step * i )

        if sequence_number == 3:
            bullet.velocity = pygame.Vector2(0, random.randint(2,4)).rotate_rad(-1 * step * i )
            bullet.radius = random.randint(6, 10)
        
        boss_bullets.append(bullet)


def points_to_percent(hp, max_hp):
    percent = round((hp / max_hp) * 100, 2)
    if(percent < 0):
        return 0
    return percent

def loop_over(objects, surface):
    for ent in objects:
        ent.update()
        if ent.is_dead:
            objects.remove(ent)
        ent.display(surface)


