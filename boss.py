from entity import Entity
from CONSTS import *

class Boss(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 60
        self.hp = 10
        self.speed = 0
        self.weapon = 0
        self.can_attack = True
        self.bullet_break = pygame.time.get_ticks()

        self.image = pygame.transform.scale(BOSS_IMAGE.convert(), (2 * self.radius, 2 * self.radius))
        self.transColor = BOSS_IMAGE.get_at((0,0))
        self.image.set_colorkey(self.transColor)

    def update(self):
        super().update()
        self.attack()

    def check_border(self):
        # LEFT
        if self.x <= self.radius + 10:
            self.velocity.x = 1
        # RIGHT
        if self.x >= MAP_WIDTH - self.radius:
            self.velocity.x = (-1)
        # DOWN
        if self.y >= MAP_HEIGHT/3 - self.radius:
            self.velocity.y = (-1)
            if(self.velocity.x == 0):
                self.velocity.x = 1
        # UP - firstly check if is on board 
        if (self.is_on_board()):
            if(self.y <= self.radius):
                self.velocity.y = 1

    def is_on_board(self):
        if self.y < self.radius + 10:
            return True

    def death(self):
        super().death()
        BOSS_DEATH_SOUND.play()        

    def display(self, surface):
        pygame.draw.circle(surface, YELLOW, (self.x, self.y) , self.radius, 0)
        MAP_SCREEN.blit(self.image, (self.x-self.radius, self.y-self.radius))

    def cooldown(self):
        now = pygame.time.get_ticks()  #spawn delay
        if(now - self.bullet_break > 1000):
            self.bullet_break = now
            self.can_attack = True
    
    def attack(self):
        now = pygame.time.get_ticks()  #spawn delay
        if(now - self.last_update > 200):
            self.last_update = now
            self.spawn_bullet = True

