import pygame
from random import randrange as r


# Variables
minWaitTime = 1.5
maxWaitTime = 3
reps = 3


# Initializes pygame
pygame.init()

# Declaring Variable
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
isTest = False
startTime = 0
reacts = []


while running:

    currentTime = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and isTest and endTime <= currentTime:
                reacts.append(currentTime-endTime)
                isTest = False

        elif event.type == pygame.QUIT:
            running = False

    if not isTest:
        reps -= 1
        if reps == -1:
            running = False
        
        screen.fill("red")
        startTime = currentTime
        endTime = startTime + r(4*10, 12*10)*100
        isTest = True
    
    elif isTest and endTime > currentTime:
        screen.fill("red")

    elif isTest and endTime <= currentTime:
        screen.fill("green")


    pygame.display.flip()

    clock.tick(120)


print(reacts)