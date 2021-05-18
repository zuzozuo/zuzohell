import pygame

from entity import Entity
from CONSTS import *
from entities import *

class Bullet(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 6
        self.hp = 0
        self.speed = BASIC_BULLET_SPEED
        self.power = 0
        self.velocity = pygame.Vector2(0,-4) #toedit
        self.type = 'Bullet'

    def display(self, surface):
        pygame.draw.circle(surface, BLUE, (self.x, self.y) , self.radius, 0)

    # HANDLING EVENTS

    def cooldown(self):
        pass

    def check_border(self):
        if self.y > MAP_HEIGHT + self.radius:
            self.is_dead = True
        if self.y < 0:
            self.is_dead = True

        if self.x < 0 - self.radius:
            self.is_dead = True

        if self.x > MAP_WIDTH + self.radius:
            self.is_dead = True
