from entities import *
from bullet import Bullet
from mob import Mob
from CONSTS import *
import math
import random
import pygame
import pygame.mixer
import pygame.freetype

def init_game():
    pass

def reset_game():
    pass

def add_mob():
    mob = Mob(random.randint(0,int(MAP_WIDTH/30)) * 30, WORLD_CEILING - 30)
    mob.init()
    FEAR_SOUND.play()
    mobs.append(mob)

def add_bullets(x, y, angle, surface):
    bullet = Bullet(x, y)
    bullets.append(bullet)


def add_mob_bullets(x,y, angle, surface):

    angle = random.random() - 0.5
    bullet = Bullet(x, y)
    bullet.velocity = pygame.Vector2(0, BASIC_BULLET_SPEED).rotate_rad(angle)
    bullet.color = IDK_COLOR
    mob_bullets.append(bullet)

def add_boss_bullets(x, y, radius):
    step = 2 * math.pi / BOSS_BULLETS_NUMBER
    for i in range(0, BOSS_BULLETS_NUMBER):
        x_spawn = x + math.sin(step * i) * radius
        y_spawn = y + math.cos(step * i) * radius
        #angle = random.random() - 0.5
        bullet = Bullet(x_spawn, y_spawn)
        bullet.velocity = pygame.Vector2(0,0)
        bullet.velocity = pygame.Vector2(0, BASIC_BULLET_SPEED).rotate_rad(-1 * step * i )
        #bullet.velocity = pygame.Vector2(0, BASIC_BULLET_SPEED).rotate_rad(angle)
        bullet.color = RED
        boss_bullets.append(bullet)

def loop_over(objects, surface):
    for ent in objects:
        ent.update()
        if ent.is_dead:
            objects.remove(ent)
        ent.display(surface)


