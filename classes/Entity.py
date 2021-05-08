import pygame
class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(0, 0)
        self.acceleration = pygame.Vector2()

        self.m_bottom = 0
        self.m_top = 0
        self.m_left = 0
        self.m_right = 0


    def init(): # any entity init
        pass

    def update(): #update done on every object
        pass

    def check_border(): #check border behaviour
        pass

    def cooldown(): #any entity cooldown
        pass

    def display(self, surface, color): #any entity display
        pass
    
    #handling events
    def death():
        pass

    def hit():
        pass

    def collision():
        pass

    def update_position(self):
        self.x +=self.velocity.x
        self.y += self.velocity.y 