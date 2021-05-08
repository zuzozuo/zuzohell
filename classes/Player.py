from entity import Entity
import pygame
from CONSTS import *
class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 30
        self.hp = 0
        self.speed = 3
        self.weapon = 0
        self.fire = False
        self.x = x
        self.y = y

    
    def bonus(): #gain bonus after collecting items
        pass    

    def update():
        pass

    #MOVING
    def move(self):
        self.velocity = pygame.Vector2(0, 0)
        
        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        if keystate[pygame.K_RIGHT]:
            self.velocity.x = self.speed
        if keystate[pygame.K_UP]:
            self.velocity.y = -self.speed
        if keystate[pygame.K_DOWN]:
            self.velocity.y = self.speed

    #check border behaviour
    def check_border(self):
        #LEFT
        if (self.x < self.radius + MAP_OFFSET):
            self.x = self.radius + MAP_OFFSET
        
        #RIGHT
        if (self.x > MAP_WIDTH - self.radius + MAP_OFFSET):
            self.x = MAP_WIDTH  - self.radius + MAP_OFFSET

        #UP
        if (self.y < self.radius + MAP_OFFSET):
            self.y = self.radius + MAP_OFFSET

        #DOWN
        if (self.y > MAP_HEIGHT - self.radius + MAP_OFFSET):
            self.y = MAP_HEIGHT - self.radius + MAP_OFFSET

    #HANDLING EVENTS
    def shoot():
        pass

    def death():
        pass

    def display(self, surface, color): 
        pygame.draw.rect(surface, color, pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius * 2, self.radius * 2))
    
    def cooldown():
        pass

    def collision():
        pass


