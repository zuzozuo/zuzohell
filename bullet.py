import pygame

from entity import Entity
from CONSTS import *


class Bullet(Entity):
    def __init__(self, x, y):
        super.__init__(x, y)
        self.radius = 4
        self.hp = 0
        self.speed = BASIC_BULLET_SPEED
        self.power = 0
        self.is_dead = False

    def spawn_bullet(self):
        self.y = self.y + 10  # liczba taka losowa o narazie

    def display(self, surface):
        pygame.draw.rect(surface, BLUE,
                         pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2))

    # HANDLING EVENTS
    def death(self):
        pass

    def cooldown(self):
        pass

    def update_position(self):
        self.velocity.y = 0
        self.velocity.y = 2

    def check_border(self):
        if self.y > MAP_HEIGHT + self.radius:
            self.is_dead = True
        if self.y < 0:
            self.is_dead = True

        if self.x < 0 - self.radius:
            self.is_dead = True

        if self.x > MAP_WIDTH + self.radius:
            self.is_dead = True
        pass

    def collision(self):
        pass
