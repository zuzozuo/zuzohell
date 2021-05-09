
import pygame

from CONSTS import *
from player import Player
from entities import bullets
from util import loop_over, add_bullets
# ------------------------------------
score = 0

# -------------Init-------------------
pygame.init()
clock = pygame.time.Clock()

MAP_SCREEN = pygame.display.set_mode((MAP_WIDTH, MAP_HEIGHT))

pygame.display.set_caption("Zuzohell")
icon = pygame.image.load('img/411.png')
pygame.display.set_icon(icon)
# spawn player

player = Player(MAP_WIDTH / 2, MAP_WIDTH * 0.98)
# ------------Game Loop-----------------
running = True

while running:
    clock.tick(FPS)
    MAP_SCREEN.fill(WHITE)

    # EVENT HANDLING
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    #loop_over(bullets)
    if player.spawn_bullet == True:
        add_bullets(player.x, player.y, 0, MAP_SCREEN)
        player.spawn_bullet = False
    
    loop_over(bullets, MAP_SCREEN)
    
    player.move()
    player.update_position()
    player.check_border()

    player.display(MAP_SCREEN)
    pygame.display.update()

# -----------------------------------------
pygame.quit()
