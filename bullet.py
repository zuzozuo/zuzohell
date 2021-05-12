import pygame

from entity import Entity
from CONSTS import *


class Bullet(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 10
        self.hp = 0
        self.speed = BASIC_BULLET_SPEED
        self.power = 0
        self.is_dead = False
        self.velocity = pygame.Vector2(0,-4) #toedit

    def display(self, surface):
        pygame.draw.rect(surface, BLUE, pygame.Rect(self.x, self.y , self.radius , self.radius ))


    # HANDLING EVENTS
    def death(self):
        pass

    def cooldown(self):
        pass

    def check_border(self):
        if self.y > MAP_HEIGHT + self.radius:
            self.is_dead = True

            print("Dead")
        if self.y < 0:
            self.is_dead = True
            print("Dead")

        if self.x < 0 - self.radius:
            self.is_dead = True
            print("Dead")

        if self.x > MAP_WIDTH + self.radius:
            self.is_dead = True
            print("Dead")

    def collision(self):
        pass
