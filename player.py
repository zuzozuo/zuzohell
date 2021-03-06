from entity import Entity
import pygame
from CONSTS import *
import pygame.mixer


class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = PLAYER_RADIUS
        self.display_radius = PLAYER_RADIUS + 5
        self.hp = PLAYER_MAX_HP
        self.score = 0
        self.speed = PLAYER_SPEED
        self.fire = False
        self.x = x
        self.y = y
        self.is_player = True
        self.kill_count = 0

        self.image = pygame.transform.scale(PLAYER_IMAGE.convert(), (2 * self.display_radius, 2 * self.display_radius))
        self.transColor = PLAYER_IMAGE.get_at((0,0))
        self.image.set_colorkey(self.transColor)
    
    def update(self):
        super().update()
        if self.hp < 0:
            self.hp = 0

    def death(self):
        super().death()
        self.is_dead == True
        PLAYER_DEATH_SOUND.play()

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
        #pygame.draw.circle(surface, WHITE, (self.x, self.y) , self.radius, 0)
        WINDOW_SCREEN.blit(self.image, (self.x-self.radius, self.y-self.radius))

    def cooldown(self):
        pass

    def attack(self):
        now = pygame.time.get_ticks()  #bullet spawn delay
        if(now - self.last_update > 100):
            self.last_update = now
            self.spawn_bullet = True
    
    def update_score(self, count):
        self.score += count

    def update_hp(self, count,sound):
        super().update_hp(count)
        if count < 0 and sound:
            PLAYER_HURT_SOUND.play()

    def update_kill_count(self):
        self.kill_count +=1

