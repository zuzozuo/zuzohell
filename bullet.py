import pygame
import pygame.mixer
from entity import Entity
from CONSTS import *
from entities import *

class Bullet(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 6
        self.color = BLUE
        self.velocity = pygame.Vector2(0,-4) 

        self.image = None
        self.transColor = None

    def display(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y) , self.radius, 0)
        #WINDOW_SCREEN.blit(self.image, (self.x-self.radius, self.y-self.radius))
    # HANDLING EVENTS

    def check_border(self):
        if self.y > MAP_HEIGHT + self.radius:
            self.is_dead = True
            
        if self.y < 0:
            self.is_dead = True

        if self.x < 0 - self.radius:
            self.is_dead = True

        if self.x > MAP_WIDTH + self.radius:
            self.is_dead = True
