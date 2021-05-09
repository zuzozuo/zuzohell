from entity import Entity
class Mob(Entity):
    def __init__(self, x, y):
        super.__init__(x,y)
        self.radius = 0
        self.hp = 0
        self.speed = 0
        self.weapon = 0
    

    def update(self):
        pass
    #HANDLING EVENTS

    def shoot(self):
        pass

    def death(self):
        pass

    def display(self):
        pass
    
    def cooldown(self):
        pass


    def collision(self):
        pass


