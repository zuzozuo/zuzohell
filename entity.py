import pygame
import math
from entities import *
from CONSTS import *

class Entity:
    def __init__(self, x, y):
        self.x = x #center coords
        self.y = y #center coords
        self.radius = 0


        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2()

        self.m_bottom = 0
        self.m_top = 0
        self.m_left = 0
        self.m_right = 0

        self.spawn_bullet = False
        self.last_update = pygame.time.get_ticks()
        self.is_player = False
        self.is_dead = False

    def init(self):  # any entity init
        pass

    def update(self):  # update done on every object
        self.update_position()
        self.check_border()

    def cooldown(self):  # any entity cooldown
        pass

    def display(self, surface):  # any entity display
        pass

    # handling events
    def death(self):
        self.is_dead = True

    def hit(self):
        pass

    def check_border(self): #any entity border checkin
        pass

    def attack(self):
        pass
    
    def is_collision(self, obj):
        #calculationg distance vector
        dist_vec = math.sqrt((self.x - obj.x)** 2  + ((self.y - obj.y)** 2 ))
        return dist_vec <= obj.radius + self.radius

    def update_position(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
