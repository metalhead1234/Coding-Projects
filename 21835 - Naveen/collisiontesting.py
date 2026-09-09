import pygame
pygame.init()

PURPLE  = [255,0,255]
BLACK = [0,0,0]
WHITE = [255,255,255]

quitVar = True
show = True
screen = pygame.display.set_mode((540,380))
blackX = 80
FPS = 24
clock = pygame.time.Clock()

while quitVar == True:

    screen.fill(WHITE)

    if show == True: 
        whiteRect  = pygame.draw.rect(screen, PURPLE, (250,300,50,50))    
        blackRect  = pygame.draw.rect(screen, BLACK, (blackX,315,20,20))

    if whiteRect.colliderect(blackRect):
                show = False
    else: 
          blackX += 2

    for event in pygame.event.get():
          if event.type == pygame.QUIT:
                quitVar = False

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
