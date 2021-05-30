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
    bullet = Bullet(x, y, DEFAULT_BULLET_RADIUS, BULLET_PLAYER_IMAGE)
    bullets.append(bullet)


def add_mob_bullets(x,y):

    angle = random.random() - 0.5
    bullet = Bullet(x, y, DEFAULT_BULLET_RADIUS, BULLET_IMAGE_BLUE)
    velocity_y = random.random() * (MAX_BULLET_SPEED - MIN_BULLET_SPEED + 1) + MIN_BULLET_SPEED
    bullet.velocity = pygame.Vector2(0, velocity_y).rotate_rad(angle)
    bullet.color = IDK_COLOR
    mob_bullets.append(bullet)

def add_boss_bullets(x, y, radius, sequence_number, bullets_number):

    step = 2 * math.pi / bullets_number #calculate radians

    for i in range(0, bullets_number):
        x_spawn = x + math.sin(step * i) * radius
        y_spawn = y + math.cos(step * i) * radius
        velocity = pygame.Vector2(0,0)
        radius = DEFAULT_BULLET_RADIUS  
        img = ALL_BULLETS[random.randint(1,len(ALL_BULLETS)-1)]      

        if sequence_number == 0:
            velocity = pygame.Vector2(0, MIN_BULLET_SPEED).rotate_rad(-1 * step * i )

        if sequence_number == 1:
            speed = random.random() * (MAX_BULLET_SPEED - MIN_BULLET_SPEED + 1) + MIN_BULLET_SPEED
            sign = random_sign()
            #angle = random.random() - 0.5
            radius = random.randint(6, 10)
            velocity = pygame.Vector2(0, speed).rotate_rad(sign * step * i )

        if sequence_number == 2:
            velocity = pygame.Vector2(0, random.randint(2,5)).rotate_rad(1 * step * i )

        if sequence_number == 3:
            velocity = pygame.Vector2(0, random.randint(2,4)).rotate_rad(-1 * step * i )
            radius = random.randint(6, 10)
        
        bullet = Bullet(x_spawn, y_spawn, radius, img)
        bullet.velocity = velocity
        bullet.radius = radius
        bullet.color = RED        
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

def random_sign():
    if random.random() < 0.5:
        return 1
    else:
        return -1



