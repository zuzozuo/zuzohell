from entities import *
from bullet import Bullet


def init_game(self):
    pass


def reset_game(self):
    pass


def add_bullets(x, y, angle, surface):
    bullet = Bullet(x, y)
    bullets.append(bullet)


def loop_over(objects, surface):
    for ent in objects:
        ent.update()
        ent.display(surface)
        if ent.is_dead:
            objects.remove(ent)
