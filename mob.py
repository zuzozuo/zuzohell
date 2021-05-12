from entity import Entity
import random
import pygame
from CONSTS import *
class Mob(Entity):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.radius = 8
        self.hp = 0
        self.speed = 0
        self.weapon = 0
        self.is_dead = False
    

    def init(self):
        self.speed = random.random() * (SPEED_MAX - SPEED_MIN + 1) + SPEED_MIN
        self.velocity.x = 0
        self.velocity.y = self.speed

    def display(self, surface):
        pygame.draw.rect(surface, YELLOW, pygame.Rect(self.x, self.y , self.radius  , self.radius * 10 ))
    #HANDLING EVENTS

    def shoot(self):
        pass

    def death(self):
        pass
    
    def cooldown(self):
        pass

    def collision(self):
        pass
    def check_border(self): #TO DO - CHECKING ONLY BOTTOM LEFT AND RIGHT

        """ if self.y < 0:
            self.is_dead = True
            print("Dead mob")"""

        if self.x < 0 - self.radius:
            self.is_dead = True
            print("Dead mob")

        if self.x > MAP_WIDTH + self.radius:
            self.is_dead = True
            print("Dead mob")


