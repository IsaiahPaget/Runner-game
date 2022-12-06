import pygame
import sys
from random import randint

pygame.init()


RES = ((800,450))
Difficulty = 1
screen = pygame.display.set_mode(RES)
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
gamestate = {'start': 1, 'main': 0, 'end': 0}

# scoreboard init
score = 1

# end screen

end_surface = pygame.Surface((800,450))
end_surface.fill('grey')
end_font = pygame.font.Font(None, 50)
end_fontsurf = end_font.render(f"High Score: {score - 1} Hold Space To Play Again", False, 'black')

# start screen
start_surface = pygame.image.load("graphics/startscreen.png").convert_alpha()
start_font = pygame.font.Font(None, 100)
start_fontsurf = start_font.render(f'Press Space To Start', False, (228,197,132))

# end screen surface
end_surface = pygame.image.load("graphics/startscreen.png").convert_alpha()

# background surface
bg_surface = pygame.image.load("graphics/ground.png").convert_alpha()
bg_rect = bg_surface.get_rect(topleft = (800,250))

# obstacle surfaces
obstacle_surface = pygame.image.load("graphics/Ball.png").convert_alpha()
obstacle_rect = obstacle_surface.get_rect(topleft = (750, 300))
obs_counter = 0


# ground surface
ground_surface = pygame.image.load("graphics/bg.png").convert_alpha()
ground_rect = ground_surface.get_rect(bottomleft = (800,250))

# player surface
player_surface = pygame.Surface((50, 50))
player_walk = [
    pygame.image.load("graphics/pWalkRight.png").convert_alpha(),
    pygame.image.load("graphics/pWalkRight1.png").convert_alpha(),
    ]
player_index = 0
p_rect = player_surface.get_rect(topleft = (50,200))

def scoreboard():
    global text_font, text_surface, end_fontsurf

    text_font = pygame.font.Font(None, 50)
    text_surface = text_font.render(f'Score: {score - 1}', False, (228,197,132))

    end_font = pygame.font.Font(None, 50)
    end_fontsurf = end_font.render(f"High Score: {score - 1} Hold Space To Play Again", False, (228,197,132))

def collisions():
    global gamestate
    if pygame.Rect.colliderect(p_rect, obstacle_rect):
        
        gamestate['main'] = 0
        gamestate['end'] = 1

def obstacle_movement():
    global obstacle_rect, obs_counter
    
    if obs_counter == 0:
        obstacle_rect.y = randint(200,440)
    obs_counter += 1
    if obs_counter >= 1:
        obstacle_rect.left -= Difficulty
    if obstacle_rect.left <= -50:
        obs_counter = 0
        obstacle_rect.left = 800
        difficulty()

def difficulty():
    global Difficulty, score

    Difficulty = (25 * score) / (score + 24)
    score += 1


def player_animation():
    global player_surface, player_index
    
    if player_index > 1.9:
        player_index = 0
    else:
        player_index += 0.04
        player_surface = player_walk[int(player_index)]

def player_move():

    keys = pygame.key.get_pressed()
    
    # movement on the y axis
    if keys[ord('w')] and not p_rect.centery <= 250:
        p_rect.top -= 5
    if keys[ord('s')] and not p_rect.bottom >= 450:
        p_rect.bottom += 5

    # movement on the x axis
    if keys[ord('a')] and not p_rect.left <= 10:
        p_rect.left -= 5
    if keys[ord('d')] and not p_rect.right >= 300:
        p_rect.right += 5
            

while True:
    
    # check if the window has been closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit
    if gamestate['start'] == 1 and gamestate['main'] == 0 and gamestate['end'] == 0:
        
        screen.blit(start_surface, (0, 0))
        screen.blit(start_fontsurf, (65, 150))
        
        startkey = pygame.key.get_pressed()
        if startkey[ord(' ')]:
            gamestate['start'] = 0
            gamestate['main'] = 1
    
    if gamestate['main'] == 1 and gamestate['start'] == 0 and gamestate['end'] == 0:
        
        # functions
        scoreboard()
        player_move()
        obstacle_movement()
        player_animation()
        collisions()

        # drawing
        screen.blit(bg_surface, (0, 0))
        screen.blit(text_surface, (25, 25))
        screen.blit(ground_surface, (0, 250))
        screen.blit(player_surface, p_rect)
        screen.blit(obstacle_surface, obstacle_rect)
    
    if gamestate['end'] == 1 and gamestate['start'] == 0 and gamestate['main'] == 0:

        scoreboard()
        screen.blit(end_surface, (0, 0))
        screen.blit(end_fontsurf, (75, 100))

        endkey = pygame.key.get_pressed()
        if endkey[ord(' ')]:
            gamestate['start'] = 0
            gamestate['main'] = 1
            gamestate['end'] = 0
            score = 1
            obstacle_rect.left = 800
            Difficulty = 1


    pygame.display.update()
    clock.tick(60)