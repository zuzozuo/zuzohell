import pygame
from CONSTS import *

class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2()

        self.m_bottom = 0
        self.m_top = 0
        self.m_left = 0
        self.m_right = 0

        self.spawn_bullet = False
        self.last_update = pygame.time.get_ticks()

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
        pass

    def hit(self):
        pass

    def collision(self):
        pass

    def check_border(self): #any entity border checkin
        pass

    def attack(self, is_player):
        if (is_player):
            now = pygame.time.get_ticks()  #spawn delay
            if(now - self.last_update > 60):
                self.last_update = now
                self.spawn_bullet = True
            print("He atacc")

    def update_position(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
