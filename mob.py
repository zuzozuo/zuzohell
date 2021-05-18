from entity import Entity
import random
import pygame
from CONSTS import *
class Mob(Entity):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.radius = 15
        self.hp = 0
        self.speed = 0
        self.weapon = 0
        self.type = 'Mob'
        self.can_attack = True
        self.bullet_break = pygame.time.get_ticks()
    

    def init(self):
        self.speed = random.random() * (SPEED_MAX - SPEED_MIN + 1) + SPEED_MIN
        self.velocity.x = 0
        self.velocity.y = self.speed

    def update(self):
        super().update()
        self.attack()

    def display(self, surface):        
        pygame.draw.circle(surface, YELLOW, (self.x, self.y) , self.radius, 0)
    #HANDLING EVENTS

    def attack(self):
        now = pygame.time.get_ticks()  #spawn delay
        if(now - self.last_update > 100):
            self.last_update = now
            self.spawn_bullet = True
    
    def cooldown(self): #wait for spawning group of bullets
        now = pygame.time.get_ticks()  #spawn delay
        if(now - self.bullet_break > 1000):
            self.bullet_break = now
            self.can_attack = True

    def check_border(self): 

        if self.y > MAP_HEIGHT - self.radius:
            self.is_dead = True

        if self.x < 0 - self.radius:
            self.is_dead = True

        if self.x > MAP_WIDTH + self.radius:
            self.is_dead = True
