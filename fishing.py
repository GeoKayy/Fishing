import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
screen.fill((0, 100, 255))
clock = pygame.time.Clock()
mousebuttondown = False
boxlength = 400
boxy = 580
endboxy = boxy + boxlength
boxvely = 0
fishvely = 0
fishy = 500
fishmovecd = 0
fishup = False
endfishy = fishy + 50
fishin = False
progress = 0
gameend = False
coins = 0
progcolour = (255, 0, 0)
fishicon = pygame.image.load("fish.png")
pygame.display.set_icon(fishicon)
fishcatch = pygame.image.load("fish2.png")
fishinbox = pygame.image.load("fishin.png")
fishoutbox = pygame.image.load("fishout.png")
pygame.display.set_caption("fishing")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousebuttondown = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mousebuttondown = False

    if fishmovecd <= 0:
        if random.randint(0, 1) == 1: ## randomly move fish
            fishmovecd = 10
            fishup = True
        else:
            fishmovecd = 15
            fishup = False

    screen.fill((0, 100, 255)) # clear screen
    pygame.draw.rect(screen, (255, 255, 255), (1400, 100, 100, 880))  # backbox
    pygame.draw.circle(screen, (255, 255, 255), (1450, 100), 50)  # topback circle
    pygame.draw.circle(screen, (255, 255, 255), (1450, 980), 50)  # bottomback circle
    
    pygame.draw.rect(screen, (255, 255, 255), (1200, 290, 50, 500))  # progbox
    pygame.draw.rect(screen, progcolour, (1200, (790-progress*5), 50, progress*5))  # prog

    boxy += boxvely
    endboxy = boxy + boxlength - 100
    fishy += fishvely
    endfishy = fishy + 50
    
    if endboxy >= 881: #### bottom box bounds
        boxvely = 0
        boxy = 580

    elif boxy <= 99: ##### top box bounds
        boxvely = 0
        boxy = 100

    if endfishy >= 1031: #### bottom fish bounds
        fishvely = 0
        fishy = 981

    elif fishy <= 99: ##### top fish bounds
        fishvely = 0
        fishy = 100

    if fishup: ####### increase fish vel
        fishvely -= 0.5
    else:
        fishvely += 0.5

    if mousebuttondown: ####### increase box vel (if in bounds)
        boxvely -= 1.5
    elif not mousebuttondown:
        boxvely += 1.5
        
    if fishy + 25 >= boxy and endfishy - 200 <= endboxy: ### bounds
        fishin = True
        progress += 0.5
    else:
        fishin = False
        progress -= 1
        
    if progress > 100:
        gameend = True
    elif progress < 0:
        progress = 0
        
    if gameend:
        progress = 0
        coins += 1
        boxy = 580
        boxvely = 0
        fishy = 500
        fishvely = 0
        progcolour = (255, 0, 0)
        gameend = False

    progcolour = (255-progress*2.55, progress*2.55, 0)
    endboxy = boxy + boxlength - 100 ### update endboxy
    
    if fishin == True:
        screen.blit(fishinbox, (1280, boxy-40)) #### capturebox
    else:
        screen.blit(fishoutbox, (1280, boxy-40)) #### capturebox

    screen.blit(fishcatch, (1400, fishy-30)) ### fish
    fishmovecd -= 1
    pygame.display.flip()
    clock.tick(60)
