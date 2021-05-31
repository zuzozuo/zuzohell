import pygame
import math
from entities import *
from CONSTS import *
import pygame.mixer

class Entity:
    def __init__(self, x, y):
        self.x = x #center coords
        self.y = y #center coords
        self.radius = 0
        self.hp = 0
        self.velocity = pygame.Vector2(0, 0)

        self.spawn_bullet = False
        self.last_update = pygame.time.get_ticks()
        self.is_player = False
        self.is_boss = False
        self.is_dead = False

    def update(self):  # update done on every object
        self.update_position()
        self.check_border()

    def cooldown(self):  # any entity cooldown
        pass

    def display(self, surface):  # any entity display
        pass

    def check_border(self):
        pass

    # handling events
    def death(self):
        self.is_dead = True
    
    def is_collision(self, obj):
        #calculationg distance vector
        dist_vec = math.sqrt((self.x - obj.x)** 2  + ((self.y - obj.y)** 2 ))
        return dist_vec <= obj.radius + self.radius

    def update_position(self):
        self.x += self.velocity.x
        self.y += self.velocity.y

    def update_hp(self, count):
        self.hp += count
