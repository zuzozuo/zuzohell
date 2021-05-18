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
        self.is_player = True

        self.image = pygame.transform.scale(PLAYER_IMAGE.convert(), (2 * self.radius, 2 * self.radius))
        self.transColor = PLAYER_IMAGE.get_at((0,0))
        self.image.set_colorkey(self.transColor)
    

    def bonus(self):  # gain bonus after collecting items
        pass

    def update(self):
        pass

    # MOVING
    def move(self):
        self.velocity = pygame.Vector2(0, 0)

        keystate = pygame.key.get_pressed()

        if keystate[pygame.K_SPACE]:
            self.attack()

        if keystate[pygame.K_LEFT]:
            self.velocity.x = -self.speed
        if keystate[pygame.K_RIGHT]:
            self.velocity.x = self.speed
        if keystate[pygame.K_UP]:
            self.velocity.y = -self.speed
        if keystate[pygame.K_DOWN]:
            self.velocity.y = self.speed

    # check border behaviour
    def check_border(self):
        # LEFT
        if self.x < self.radius:
            self.x = self.radius

            # RIGHT
        if self.x > MAP_WIDTH - self.radius:
            self.x = MAP_WIDTH - self.radius

            # UP
        if self.y < self.radius:
            self.y = self.radius

        # DOWN
        if self.y > MAP_HEIGHT - self.radius:
            self.y = MAP_HEIGHT - self.radius

            # HANDLING EVENTS

    def display(self, surface):
        #pygame.draw.rect(surface, RED,
        #                 pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2))
        #pygame.draw.circle(surface, RED, (self.x, self.y) , self.radius, 0)
        pygame.draw.circle(surface, YELLOW, (self.x, self.y) , self.radius, 0)
        MAP_SCREEN.blit(self.image, (self.x-self.radius, self.y-self.radius))

    def cooldown(self):
        pass

    def attack(self):
        now = pygame.time.get_ticks()  #bullet spawn delay
        if(now - self.last_update > 70):
            self.last_update = now
            self.spawn_bullet = True

