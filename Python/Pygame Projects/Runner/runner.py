import pygame
from sys import exit

def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time #subtract starttime from game duration so that score is zero
    score_surf = score_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
game_active = False
start_time = 0 # to enable a fresh restart after game over.

#textures & text
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
score_font = pygame.font.Font('font/pincher.otf', 50)
# score_surf = score_font.render('My game', False, (64, 64, 64)) #RGB 646464
# score_rect = score_surf.get_rect (center = (400, 50))

#snail
snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))#300 places the snail on the ground
snail_x_pos = 600

#player
player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300)) # the 80, 300 defines where the specified part of the rectange is placed. Now the player is nicely on the ground.
player_gravity = 0
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand_rect = player_stand.get_rect(center = (400, 200))    

#game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >=300: # only jump when player is 'touching' the ground:
                if player_rect.collidepoint(event.pos):
                    player_gravity -= 20 #make the player jump, but on mousebutton down

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >=300: # only jump when player is 'touching' the ground
                    player_gravity = -20 #make the player jump.
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True # when left like this Space will restart the game at the last frame where the collision happend, so....
                snail_rect.left = 800 #we reset the snail to 800 for
                start_time = int(pygame.time.get_ticks() / 1000) #reset time to enable restart of the game
                     
    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        display_score()
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800 # is the right part of the snail leaves the screen, reset it at the beginning.
        screen.blit(snail_surface, snail_rect)
        
        #player
        player_gravity += 1 # will add exponential -> 300, 303 306 etc.
        player_rect.y += player_gravity # to connect the gravity variable to the player rectangle.

        #create the floor. All we want to check is the y position and reposition the player so that it looks like he/she is on the floor
        # player.bottom > 300: player.bottom = 300
        if player_rect.bottom >= 300: player_rect.bottom = 300


        screen.blit(player_surface, player_rect)

        #collision

        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill(94, 129, 162)
        screen.blit(player_stand, player_stand_rect)


    #draw all our elements
    #update everything
    pygame.display.update()
    clock.tick(60)

    