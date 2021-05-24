import pygame
import pygame.freetype 
from CONSTS import *
from player import Player
from entities import *
from boss import Boss
from helpers import *
# ------------------------------------
print(pygame.font.get_fonts())
mobs_to_spawn = random.randint(MIN_MOBS_NUMBER, MAX_MOB_NUMBER) 
INIT_MOBS_NUMBER = mobs_to_spawn #need to remeber this value
mobs_to_kill = random.randint(MIN_NUMBER_TO_KILL, MAX_NUMBER_TO_KILL)
boss_phase = False
boss_wait = False
boss_counter = 0
# -------------Init-------------------
game_state = GAME_START
pygame.init()
TITLE_FONT = pygame.freetype.Font("fonts/slkscr.ttf", 30)
GAME_FONT = pygame.freetype.Font("fonts/slkscr.ttf", 24)
INFO_FONT = pygame.freetype.Font("fonts/slkscr.ttf", 12)

clock = pygame.time.Clock()

pygame.display.set_caption("Zuzohell")
icon = pygame.image.load('img/411.png')
pygame.display.set_icon(icon)
pygame.mixer.set_num_channels(100)
pygame.mixer.set_reserved(0)
pygame.mixer.set_reserved(1)
pygame.mixer.set_reserved(2)
pygame.mixer.set_reserved(3)
pygame.mixer.Sound.set_volume(BACKGROUND_MUSIC, 0.3)
pygame.mixer.Sound.set_volume(PLAYER_DEATH_SOUND, 1.2)
pygame.mixer.Sound.set_volume(PLAYER_HURT_SOUND, 0.3)
pygame.mixer.Sound.set_volume(BOSS_DEATH_SOUND, 0.5)
pygame.mixer.Sound.set_volume(BOSS_APPEARS_SOUND, 0.5)
pygame.mixer.Sound.set_volume(PLAYER_BULLET_SOUND, 0.1)
pygame.mixer.Sound.set_volume(GAME_WIN_SOUND, 0.3)
pygame.mixer.Sound.set_volume(GAME_WIN_MUSIC, 0.2)


play_music = True
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
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , 60), "THE ZUZOHELL GAME ", (0, 0, 0))
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , 120), "HOW TO PLAY?: ", (0, 0, 0))
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10  , 150), "SPACE - FIRE ", (0, 0, 0))
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10  , 180), "USE ARROW KEYS TO MOVE CHEEMS ", (0, 0, 0))
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , 210), "YOU WIN IF YOU KILL 3 BIG CATS  ", (0, 0, 0))
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , 240), "YOU LOSE IF TOUCH BIG CAT", (0, 0, 0))
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , 270), "OR YOU LOSE WHOLE HP  ", (0, 0, 0))

    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/2), "PREMSS AMNY KEY TO STAMRMT :)", (0, 0, 0))
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT - 30), "AUTHOR: ZUZOZUO", (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            game_state = GAME_PLAYING
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(WINDOW_SCREEN, BLACK, pygame.Rect(WINDOW_WIDTH - WINDOW_OFFSET, 0 , WINDOW_WIDTH - MAP_WIDTH , WINDOW_HEIGHT))
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
            PLAYER_HURT_SOUND.play()
        
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
    player.display(WINDOW_SCREEN)

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
            player.update_kill_count()
            
            if(boss_counter == BOSS_NUMBER):
                game_state = GAME_WIN

    if player.is_dead:
        game_state = GAME_OVER
    
    loop_over(boss_bullets, WINDOW_SCREEN)
    
    pygame.draw.rect(WINDOW_SCREEN, BLACK, pygame.Rect(WINDOW_WIDTH - WINDOW_OFFSET, 0 , WINDOW_WIDTH - MAP_WIDTH , WINDOW_HEIGHT))
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
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/2, 60), "GAME OVER :(", (0, 0, 0))
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , 120), "LOMSER!!! ;(  ", (0, 0, 0))
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , 150), "PREMSS SPACE TO QUIMT!", (0, 0, 0))

    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10  , MAP_HEIGHT/4), "CREDITS:  ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10  , MAP_HEIGHT/4 + 30), "MUSIC ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 3), "BACKGROUND MUSIC: \"Monkeys Spinning Monkeys\" by KevinMacLeod", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 4), "MENU MUSIC: \"Fluffing a Duck\" by KevinMacLeod", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 5), "SHORT SOUNDS: Made by Me (Zuzozuo) and my Cousin (Maciej Chowan) ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 7), "IMAGES: ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 8), "Every image was found on open source sites", (0, 0, 0))

    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 9), "DISCLAIMER: I hereby declare that I do not own the rights to this music). ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 10), " or images (except sounds I made with my cousin). ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 11), "All rights belong to the owners and creators. ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 12), "No Copyright Infringement Intended. ", (0, 0, 0))
    

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
        if event.type == pygame.QUIT:
            running = False
            
    pygame.draw.rect(WINDOW_SCREEN, BLACK, pygame.Rect(WINDOW_WIDTH - WINDOW_OFFSET, 0 , WINDOW_WIDTH - MAP_WIDTH , WINDOW_HEIGHT))
    pygame.display.update()
    pygame.display.flip()

#-----------------------------------------------------------------------
def game_win_screen():
    global GAME_FONT
    global running

    WINDOW_SCREEN.fill(WHITE)
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10, 20), "WIMNER!!!!", (0, 0, 0))
    GAME_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10, 20 + INFO_FONT_SIZE), "Your score: " + str(round(player.score, 2)), (0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = False
        if event.type == pygame.QUIT:
            running = False
    
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10  , MAP_HEIGHT/4), "CREDITS:  ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10  , MAP_HEIGHT/4 + 30), "MUSIC ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 3), "BACKGROUND MUSIC: \"Monkeys Spinning Monkeys\" by KevinMacLeod", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 4), "MENU MUSIC: \"Fluffing a Duck\" by KevinMacLeod", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 5), "SHORT SOUNDS: Made by Me (Zuzozuo) and my Cousin (Maciej Chowan) ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 7), "IMAGES: ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 8), "Every image was found on open source sites", (0, 0, 0))

    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 9), "DISCLAIMER: I hereby declare that I do not own the rights to this music). ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 10), " or images (except sounds I made with my cousin). ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 11), "All rights belong to the owners and creators. ", (0, 0, 0))
    INFO_FONT.render_to(WINDOW_SCREEN, (MAP_WIDTH/10 , MAP_HEIGHT/4 + 30 * 12), "No Copyright Infringement Intended. ", (0, 0, 0))

    pygame.draw.rect(WINDOW_SCREEN, BLACK, pygame.Rect(WINDOW_WIDTH - WINDOW_OFFSET, 0 , WINDOW_WIDTH - MAP_WIDTH , WINDOW_HEIGHT))
    pygame.display.update()
    pygame.display.flip()

# --------------------------------Game Loop------------------------------------------------------

while running:
    if game_state == GAME_START: 
        start_screen()

        if play_music:
            pygame.mixer.Channel(0).play(MENU_MUSIC, -1)
            pygame.mixer.Sound.set_volume(MENU_MUSIC, 0.1)
            play_music = False

    elif game_state == GAME_PLAYING:
        play()

        if pygame.mixer.Channel(0).get_busy() == True:
            pygame.mixer.Channel(0).stop()
            play_music = True

        if play_music:
            pygame.mixer.Channel(1).play(BACKGROUND_MUSIC, -1)
            play_music = False
    
    elif game_state == GAME_OVER:
        game_over_screen()

        if pygame.mixer.Channel(1).get_busy() == True:
            pygame.mixer.Channel(1).stop()
            play_music = True

        if play_music:
            pygame.mixer.Channel(2).play(GAME_OVER_MUSIC, -1)
            pygame.mixer.Sound.set_volume(GAME_OVER_MUSIC, 0.05)
            play_music = False

    elif game_state == GAME_WIN:
        game_win_screen()

        if pygame.mixer.Channel(1).get_busy() == True:
            pygame.mixer.Channel(1).stop()
            
            play_music = True

        if play_music:
            pygame.mixer.Channel(3).play(GAME_WIN_SOUND, 0)
            pygame.mixer.Channel(4).play(GAME_WIN_MUSIC, -1)
            play_music = False
        
pygame.quit()
