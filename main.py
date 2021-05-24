import pygame
import pygame.freetype 
from CONSTS import *
from player import Player
from entities import *
from boss import Boss
from helpers import *
# ------------------------------------
mobs_to_spawn = random.randint(MIN_MOBS_NUMBER, MAX_MOB_NUMBER) 
INIT_MOBS_NUMBER = mobs_to_spawn #need to remeber this value
mobs_to_kill = random.randint(MIN_NUMBER_TO_KILL, MAX_NUMBER_TO_KILL)
boss_phase = False
boss_wait = False
boss_counter = 0
# -------------Init-------------------
game_state = GAME_START
pygame.init()
GAME_FONT = pygame.freetype.Font("fonts/slkscr.ttf", 24)
clock = pygame.time.Clock()

pygame.display.set_caption("Zuzohell")
icon = pygame.image.load('img/411.png')
pygame.display.set_icon(icon)

# spawn player
player = Player(MAP_WIDTH / 2, MAP_HEIGHT * 0.98)
running = True       

#------------------------------------------------------------------------------------------------
def start_screen():

    global GAME_FONT
    global game_state
    global running
    global boss
    global boss_phase

    WINDOW_SCREEN.fill(WHITE)
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/2 - 200 , MAP_HEIGHT/2), "PREMSS AMNY KEY TO STAMRMT :)", (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game_state = GAME_PLAYING
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(MAP_SCREEN, BLACK, pygame.Rect(WINDOW_WIDTH - WINDOW_OFFSET, 0 , WINDOW_WIDTH - MAP_WIDTH , WINDOW_HEIGHT))
    pygame.display.update()
    pygame.display.flip()
#-----------------------------------------------------------------------------------------------
def play():

    global running
    global clock
    global game_state
    global mobs_to_spawn
    global mobs_to_kill
    global boss_phase
    global boss_wait
    global boss
    global boss_counter 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(FPS)
    WINDOW_SCREEN.fill(WHITE)    

    if player.spawn_bullet == True:
        add_bullets(player.x, player.y)
        PLAYER_BULLET_SOUND.play()
        player.spawn_bullet = False

    if(len(mobs) < INIT_MOBS_NUMBER and not boss_phase):
        mobs_to_spawn = INIT_MOBS_NUMBER
    
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
                add_mob_bullets(mobs[i].x + mobs[i].radius, mobs[i].y + mobs[i].radius)    
                mobs[i].spawn_bullet = False    
            mobs[i].can_attack = False

        for j in range(0, len(bullets)):
            if(bullets[j].is_collision(mobs[i]) == True):
                mobs[i].update_hp(-PLAYER_MOB_DAMAGE)
                player.update_score(HIT_MOB_SCORE)    

                if(mobs[i].hp <= 0):
                    mobs[i].death()
                    player.update_score(KILL_MOB_SCORE)
                    player.update_kill_count()
                bullets[j].death()
            
        if(player.is_collision(mobs[i]) == True):
            player.update_hp(-MOB_PLAYER_COLLISION_DAMAGE)
        
    for i in range(0, len(boss_bullets)):
        if(player.is_collision(boss_bullets[i]) == True):
            player.update_hp(-BOSS_PLAYER_DAMAGE)
            boss_bullets[i].death()
    
    #####WAITING FOR BOSS###############

    if(boss is None):
        if ((player.kill_count % mobs_to_kill == 0 and player.score > 0) or boss_phase) :
            mobs_to_spawn = 0   
            boss_phase = True
        if(not mobs and not mob_bullets):
            boss = Boss(MAP_WIDTH/2, 0 - 60) #start boss position TODO
            boss.init()
            BOSS_APPEARS_SOUND.play()
    ######################################
    for i in range(0, len(mob_bullets)):
        if(player.is_collision(mob_bullets[i])):
            mob_bullets[i].is_dead = True
            player.update_hp(-MOB_PLAYER_DAMAGE)
    
    if player.hp <= 0: 
        player.death()
        
    loop_over(bullets, WINDOW_SCREEN)
    loop_over(mobs, WINDOW_SCREEN)
    loop_over(mob_bullets, WINDOW_SCREEN)
    
    player.move()
    player.update()
    player.display(MAP_SCREEN)

    if(boss_phase and not (boss is None)):
        boss.cooldown()

        if(boss.can_attack == True):
            boss.attack()

            if(boss.spawn_bullet == True):
                print(boss.attack_type)
                add_boss_bullets(boss.x, boss.y, boss.radius, boss.attack_type, boss.bullet_number)   
                boss.spawn_bullet = False    
            boss.can_attack = False

            print(boss_bullets)

        if(player.is_collision(boss) == True):
            player.death()

        for i in range(0, len(bullets)):
            if(boss.is_collision(bullets[i]) == True):
                boss.update_hp(-PLAYER_BOSS_DAMAGE)
                player.update_score(HIT_BOSS_SCORE)
                bullets[i].death()
    
        if boss.hp <= 0:
            boss.death()
            boss_counter +=1


        boss.update()
        boss.display(WINDOW_SCREEN)

        if(boss.is_dead):
            boss_phase = False
            boss = None
            player.update_score(KILL_BOSS_SCORE)
            player.update_kill_count
            
            if(boss_counter == BOSS_NUMBER):
                game_state = GAME_WIN

    if player.is_dead:
        game_state = GAME_OVER
    
    loop_over(boss_bullets, WINDOW_SCREEN)
    
    pygame.draw.rect(MAP_SCREEN, BLACK, pygame.Rect(WINDOW_WIDTH - WINDOW_OFFSET, 0 , WINDOW_WIDTH - MAP_WIDTH , WINDOW_HEIGHT))
    GAME_FONT.render_to(WINDOW_SCREEN, (WINDOW_WIDTH - WINDOW_OFFSET, INFO_FONT_SIZE), "Your score: " + str(round(player.score, 2)), (255, 255, 255))
    GAME_FONT.render_to(WINDOW_SCREEN, (WINDOW_WIDTH - WINDOW_OFFSET, INFO_FONT_SIZE * 2), "Your hp: " + str(points_to_percent(player.hp, PLAYER_MAX_HP)) + "%", (255, 255, 255))
    if(not(boss is None)):        
        GAME_FONT.render_to(WINDOW_SCREEN, (WINDOW_WIDTH - WINDOW_OFFSET, INFO_FONT_SIZE * 3), "Boss hp: " + str(points_to_percent(boss.hp, BOSS_MAX_HP)) + "%", (255, 255, 255))
    pygame.display.update()
    pygame.display.flip()
#-----------------------------------------
def game_over_screen():
    global GAME_FONT
    global running

    WINDOW_SCREEN.fill(WHITE)
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/2, MAP_HEIGHT/2), "LOMSER :(", (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.rect(MAP_SCREEN, BLACK, pygame.Rect(WINDOW_WIDTH - WINDOW_OFFSET, 0 , WINDOW_WIDTH - MAP_WIDTH , WINDOW_HEIGHT))
    pygame.display.update()
    pygame.display.flip()

#-----------------------------------------------------------------------
def game_win_screen():
    global GAME_FONT
    global running

    WINDOW_SCREEN.fill(WHITE)
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/2, MAP_HEIGHT/2), "WIMNER!!!!", (0, 0, 0))
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/2, MAP_HEIGHT/2 + INFO_FONT_SIZE), "Your score: " + str(player.score), (0, 0, 0))
    GAME_WIN_SOUND.play()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.rect(MAP_SCREEN, BLACK, pygame.Rect(WINDOW_WIDTH - WINDOW_OFFSET, 0 , WINDOW_WIDTH - MAP_WIDTH , WINDOW_HEIGHT))
    pygame.display.update()
    pygame.display.flip()

# --------------------------------Game Loop------------------------------------------------------
while running:

    if game_state == GAME_START: 
        start_screen()

    elif game_state == GAME_PLAYING:
        play()        
    
    elif game_state == GAME_OVER:
        game_over_screen()
    
    elif game_state == GAME_WIN:
        game_win_screen()

pygame.quit()
