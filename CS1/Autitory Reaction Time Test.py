import pygame
from random import randrange as r


# Variables
minWaitTime = 2.5
maxWaitTime = 4
reps = 3


# Initializes pygame
pygame.init()

# Sets up music pygame player 
mixer = pygame.mixer
mixer.init()
mixer.music.load("realBeep.mp3")
mixer.music.set_volume(1) 

# Declaring variable
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
isTest = False
startTime = 0
reacts = []
isPlayed = False


while running:
    currentTime = pygame.time.get_ticks()
    screen.fill("white")

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and isTest and endTime <= currentTime:
                reacts.append(currentTime-endTime)
                print("click")
                isTest = False

        elif event.type == pygame.QUIT:
            running = False

    if not isTest:
        if reps == 0:
            running = False
        reps -= 1
        startTime = currentTime
        endTime = startTime + r(4*10, 12*10)*100
        isTest = True
        isPlayed = False
    
    elif isTest and endTime <= currentTime:
        if not isPlayed:
            mixer.music.play(0, 0.09, 0) 
            isPlayed = True
    
    pygame.display.flip()
    clock.tick(120)


print(reacts)