import pygame
pygame.init()
pygame.display.set_caption("Keyboard Input Test")
screen = pygame.display.set_mode((240,180))

blackX = 80 
WHITE = [255,255,255]
BLACK = [0,0,0]

show = True



quitVar = True

myText = ""

while quitVar == True:
    
    screen.fill(WHITE)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                myText = "Space"
            if event.key == pygame.K_UP or event.key == pygame.K_W:
                myText = "Up"
            if event.key == pygame.K_DOWN or event.key == pygame.K_S:
                myText = "Down"
            if event.key == pygame.K_LEFT or event.key == pygame.K_A:
                myText = "Left"
            if event.key == pygame.K_RIGHT or event.key == pygame.K_D:
                myText = "Right"
        pygame.display.update()
pygame.quit()

