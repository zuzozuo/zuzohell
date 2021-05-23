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

def add_boss_bullets(x, y, radius, sequence_number, bullets_number):

    step = 2 * math.pi / bullets_number #calculate radians

    if sequence_number == 0:
        for i in range(0, bullets_number):
            x_spawn = x + math.sin(step * i) * radius
            y_spawn = y + math.cos(step * i) * radius
            bullet = Bullet(x_spawn, y_spawn)
            bullet.velocity = pygame.Vector2(0,0)
            bullet.velocity = pygame.Vector2(0, BASIC_BULLET_SPEED).rotate_rad(-1 * step * i )
            bullet.color = RED
            boss_bullets.append(bullet)

    elif sequence_number == 1:
        for i in range(0, bullets_number):
            x_spawn = x + math.sin(step * i) * radius
            y_spawn = y + math.cos(step * i) * radius
            angle = random.random() - 0.5
            bullet = Bullet(x_spawn, y_spawn)
            bullet.velocity = pygame.Vector2(0,0)
            #bullet.velocity = pygame.Vector2(0, BASIC_BULLET_SPEED).rotate_rad(-1 * step * i )
            bullet.velocity = pygame.Vector2(0, BASIC_BULLET_SPEED).rotate_rad(angle)
            bullet.color = RED
            boss_bullets.append(bullet)

    elif sequence_number == 2:
        for i in range(0, bullets_number):
            x_spawn = x + math.sin(step * i) * radius
            y_spawn = y + math.cos(step * i) * radius
            bullet = Bullet(x_spawn, y_spawn)
            bullet.velocity = pygame.Vector2(0,0)
            bullet.velocity = pygame.Vector2(0, random.randint(2,5)).rotate_rad(1 * step * i )
            bullet.color = RED
            boss_bullets.append(bullet)
    elif sequence_number == 3:
        for i in range(0, bullets_number):
            x_spawn = x + math.sin(step * i) * radius
            y_spawn = y + math.cos(step * i) * radius
            bullet = Bullet(x_spawn, y_spawn)
            bullet.velocity = pygame.Vector2(0,0)
            bullet.velocity = pygame.Vector2(0, random.randint(2,4)).rotate_rad(-1 * step * i )
            bullet.radius = random.randint(6, 10)
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


