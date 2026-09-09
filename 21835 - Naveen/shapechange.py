import pygame

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
pygame.display.set_caption("Shape Change")
clock = pygame.time.Clock()
screen = pygame.display.set_mode((600, 600))

rect_width = 200
rect_height = 200
rect_x = (screen.get_width() - rect_width) // 2
rect_y = (screen.get_height() - rect_height) // 2
my_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)

current_radius = 0
max_radius = min(rect_width, rect_height) // 2
morph_speed = 4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    if current_radius < max_radius:
        current_radius += morph_speed
        current_radius = min(current_radius, max_radius)

    pygame.draw.rect(screen, GREEN, my_rect, width=0, border_radius=current_radius)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()