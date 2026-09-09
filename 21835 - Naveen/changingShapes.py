import pygame


WHITE = (255,255,255)
BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
pygame.init()
pygame.display.set_caption("emojiThing")
screen = pygame.display.set_mode((400,300))

quitVar = True

while quitVar == True: 
    
    screen.fill(WHITE)
    pygame.draw.polygon(screen, GREEN, ((173,50),(245,106),(218,177),(128,177),(100,106)))
    pygame.draw.line(screen, RED, (0,0), (60,0), 4)
    pygame.draw.line(screen,RED, (0,60),(60,0),4)
    pygame.draw.line(screen, RED, (0,60), (60,60), 4)
    pygame.draw.circle(screen, RED, (375,20), 20, 0)
    pygame.draw.ellipse(screen,RED, (350,290,40,8), 1)
    pygame.draw.rect(screen, BLUE, (0,250,100,50))
     
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False
    pygame.display.update()

pygame.quit()