import pygame

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

    def attack(self, is_player):
        if (is_player):
            #add_bullets(self.x, self.y, 0, is_player, surface)

            print("He atacc")

    def update_position(self):
        self.x += self.velocity.x
        self.y += self.velocity.y
