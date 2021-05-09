from entities import *
from bullet import Bullet


def init_game(self):
    pass


def reset_game(self):
    pass


def add_bullets(x, y, angle, is_player, surface):
    bullet = Bullet(x, y, surface)
    bullet.spawn_bullet()
    bullets.append(bullet)


def loop_over(objects):
    for ent in objects:
        ent.update()
        if ent.is_dead:
            objects.remove(ent)
