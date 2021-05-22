from entity import Entity
from CONSTS import *

class Boss(Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.radius = 60
        self.hp = 0
        self.speed = 0
        self.weapon = 0

        self.image = pygame.transform.scale(BOSS_IMAGE.convert(), (2 * self.radius, 2 * self.radius))
        self.transColor = BOSS_IMAGE.get_at((0,0))
        self.image.set_colorkey(self.transColor)

    # HANDLING EVENTS
    def check_border(self):
        # LEFT
        if self.x < self.radius:
            self.x = self.radius

            # RIGHT
        if self.x > MAP_WIDTH - self.radius:
            self.x = MAP_WIDTH - self.radius

        # DOWN
        #if self.y > MAP_HEIGHT - self.radius:
        #    self.y = MAP_HEIGHT - self.radius

    def attack(self):
        pass

    def death(self):
        pass

    def display(self, surface):
        pygame.draw.circle(surface, YELLOW, (self.x, self.y) , self.radius, 0)
        MAP_SCREEN.blit(self.image, (self.x-self.radius, self.y-self.radius))

    def cooldown(self):
        pass

    def collision(self):
        pass
