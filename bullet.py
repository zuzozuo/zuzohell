import pygame
import pygame.mixer
from entity import Entity
from CONSTS import *
from entities import *

class Bullet(Entity):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.radius = r
        self.display_radius = self.radius * 2 + 2
        self.color = BLUE
        self.velocity = pygame.Vector2(0,-4) 
        self.image = pygame.transform.scale(BULLET_IMAGE_BLUE.convert(), (self.display_radius,  self.display_radius))
        self.transColor = BULLET_IMAGE_BLUE.get_at((0,0))
        self.image.set_colorkey(self.transColor)

    def display(self, surface):
        #pygame.draw.circle(surface, self.color, (self.x, self.y) , self.radius, 0)
        WINDOW_SCREEN.blit(self.image, (self.x-self.radius, self.y-self.radius))
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
