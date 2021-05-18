from entities import *
from bullet import Bullet
from mob import Mob
from CONSTS import *
import random
import pygame

def init_game():
    pass


def reset_game():
    pass

def add_mob():
    mob = Mob(random.randint(0,MAP_WIDTH), WORLD_CEILING)
    mob.init()
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


def loop_over(objects, surface):
    for ent in objects:
        ent.update()
        if ent.is_dead:
            objects.remove(ent)
        ent.display(surface)
