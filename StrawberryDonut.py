import pygame


pygame.init()
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Strawberry Donut")
run = True
center_of_screen = (250, 250)
while run is True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.circle(window, (233, 187, 133), center_of_screen, 100, 75)
    pygame.draw.circle(window, (255, 105, 180), center_of_screen, 100, 65)

    pygame.display.update()
pygame.quit()

# learning basic graphics using pygame
