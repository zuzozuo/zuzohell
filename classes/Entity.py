class Entity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.position = 0
        self.velocity = 0
        self.radius = 0

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

    def display(): #any entity display
        pass
    
    #handling events
    def death():
        pass

    def hit():
        pass

    def collision():
        pass
