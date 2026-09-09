import pygame

GREEN = [0,255,0]
WHITE = [255,255,255]
pygame.init()
pygame.display.set_caption("Whack a LLiam")
screen = pygame.display.set_mode((1080,1080))
screen.fill(WHITE)

lliam = pygame.image.load('./lliam.png')
scaled_lliam = pygame.transform.scale_by(lliam,0.1)
quitVar = True

while quitVar == True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    screen.fill(WHITE)
    screen.blit(scaled_lliam, (540,540))
    pygame.display.update()