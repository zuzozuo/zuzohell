
import pygame
import pygame.freetype 

from CONSTS import *
from player import Player
from entities import bullets
from helpers import *
# ------------------------------------
score = 0
mobs_to_spawn = 5 #TO DO, number of mobs for each level
# -------------Init-------------------
pygame.init()
GAME_FONT = pygame.freetype.Font("fonts/slkscr.ttf", 24)
clock = pygame.time.Clock()

pygame.display.set_caption("Zuzohell")
icon = pygame.image.load('img/411.png')
pygame.display.set_icon(icon)
# spawn player

player = Player(MAP_WIDTH / 2, MAP_HEIGHT * 0.98)
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

    if player.spawn_bullet == True:
        add_bullets(player.x, player.y, 0, MAP_SCREEN)
        player.spawn_bullet = False

    if(len(mobs) < 4):
        mobs_to_spawn = 1
    
    if mobs_to_spawn > 0 :
        add_mob()
        mobs_to_spawn -=  1

    
    for i in range(0, len(mobs)):
        if(mobs[i].is_dead == True):            
            continue 

        mobs[i].cooldown()

        if(mobs[i].can_attack == True):
            mobs[i].attack()

            if(mobs[i].spawn_bullet == True):
                add_mob_bullets(mobs[i].x, mobs[i].y, 0, MAP_SCREEN)    
                mobs[i].spawn_bullet = False    
            mobs[i].can_attack = False

        for j in range(0, len(bullets)):
            if(bullets[j].is_collision(mobs[i]) == True):    
                player.score += 1
                mobs[i].death()
                bullets[j].death()
            

        if(player.is_collision(mobs[i]) == True):
            player.death()
    
    for i in range(0, len(mob_bullets)):
        if(player.is_collision(mob_bullets[i])):
            mob_bullets[i].is_dead = True
            player.hp -= 1

        if player.hp == 0: 
            player.is_dead = True
    
    
    if(player.is_dead == True):        
        running = False
        print("Przegrana!!")
                    
    
    loop_over(bullets, MAP_SCREEN)
    loop_over(mobs, MAP_SCREEN)
    loop_over(mob_bullets, MAP_SCREEN)
    
    player.move()
    player.update_position()
    player.check_border()

    player.display(MAP_SCREEN)
    GAME_FONT.render_to(MAP_SCREEN, (0, MAP_HEIGHT - 58), "Your score: " + str(player.score), (0, 0, 0))
    GAME_FONT.render_to(MAP_SCREEN, (0, MAP_HEIGHT - 24), "Your hp: " + str(player.hp), (0, 0, 0))
    pygame.display.update()
    pygame.display.flip()

# -----------------------------------------

pygame.quit()
