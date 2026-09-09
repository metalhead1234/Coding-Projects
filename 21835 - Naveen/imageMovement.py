import pygame


WHITE = (255,255,255)
BLACK = [0,0,0]
RED = [255,0,0]
GREEN = [0,255,0]
BLUE = [0,0,255]
pygame.init()
pygame.display.set_caption("lliams head moves")
screen = pygame.display.set_mode((1080,1080))
screen.fill(WHITE)
lliam = pygame.image.load('21835 - Naveen/lliam.png')
scaled_lliam = pygame.transform.scale_by(lliam,0.1)
imageX = 50
imageY = 100
FPS = 30
fpsClock = pygame.time.Clock()
speed = 8

quitVar = True

img_width = scaled_lliam.get_width()
img_height = scaled_lliam.get_height()
window_width = 1080
window_height = 1080

path_points = [
    (window_width - img_width - 50, 50),
    (50, window_height - img_height - 50),
    (window_width - img_width - 50, window_height - img_height - 50),
    (50, 50),
]

target_index = 1
imageX, imageY = path_points[0]

while quitVar == True: 
    screen.fill(WHITE)
    screen.blit(scaled_lliam, (imageX, imageY))

    target_x, target_y = path_points[target_index]

    if imageX < target_x:
        imageX += min(speed, target_x - imageX)
    elif imageX > target_x:
        imageX -= min(speed, imageX - target_x)

    if imageY < target_y:
        imageY += min(speed, target_y - imageY)
    elif imageY > target_y:
        imageY -= min(speed, imageY - target_y)

    if (imageX, imageY) == (target_x, target_y):
        target_index = (target_index + 1) % len(path_points)

    fpsClock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitVar = False

    pygame.display.update()

pygame.quit()