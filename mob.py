from entity import Entity
import random
import pygame
from CONSTS import *
class Mob(Entity, pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.radius = 30
        self.hp = 0
        self.speed = 0
        self.can_attack = True
        self.bullet_break = pygame.time.get_ticks()

        self.image = pygame.transform.scale(MOB_IMAGE.convert(), (2 * self.radius, 2 * self.radius))
        self.transColor = MOB_IMAGE.get_at((0,0))
        self.image.set_colorkey(self.transColor)
    

    def init(self):
        self.speed = random.random() * (SPEED_MAX - SPEED_MIN + 1) + SPEED_MIN
        self.velocity.x = 0
        self.velocity.y = self.speed

    def display(self, surface):
        #pygame.draw.rect(self.image, YELLOW, pygame.Rect(self.x/2, self.y/2, 60, 60))   
        #self.rect = self.image.get_rect()     
        pygame.draw.circle(surface, YELLOW, (self.x, self.y) , self.radius, 0)
        MAP_SCREEN.blit(self.image, (self.x-self.radius, self.y-self.radius))
    #HANDLING EVENTS

    def attack(self):
        now = pygame.time.get_ticks()  #spawn delay
        if(now - self.last_update > 200):
            self.last_update = now
            self.spawn_bullet = True
    
    def cooldown(self): #wait for spawning group of bullets
        now = pygame.time.get_ticks()  #spawn delay
        if(now - self.bullet_break > 1000):
            self.bullet_break = now
            self.can_attack = True

    def check_border(self): 

        if self.y > MAP_HEIGHT + self.radius:
            self.is_dead = True

        if self.x < 0 - self.radius:
            self.is_dead = True

        if self.x > MAP_WIDTH + self.radius:
            self.is_dead = True
