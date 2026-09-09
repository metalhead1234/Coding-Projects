import pygame


WHITE = (255,255,255)
BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
pygame.init()
pygame.display.set_caption("emojiThing")
screen = pygame.display.set_mode((400,300))
screen.fill(WHITE)

quitVar = True

while quitVar == True:

    pygame.draw.rect(screen, GREEN, ((200,100,25,50)))
    pygame.draw.line(screen, BLUE, (200,100), (200,150), 4)
    pygame.draw.line(screen, BLUE, (200,100), (225,100), 4)
    pygame.draw.line(screen, BLUE, (225,100), (225,150), 4)
    pygame.draw.line(screen, BLUE, (225,150), (200,150), 4)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
    pygame.display.update()

pygame.quit()
