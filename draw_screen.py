import pygame


def draw_object(screen):
    pygame.draw.polygon(screen, "#c29f2e",
                        [(110, 300), (160, 300), (160, 500), (110, 500), (110, 480), (140, 480), (140, 320),
                         (110, 320)])
    pygame.draw.polygon(screen, "#c29f2e",
                        [(890, 300), (840, 300), (840, 500), (890, 500), (890, 480), (860, 480), (860, 320),
                         (890, 320)])

    pygame.draw.rect(screen, "#c29f2e", (480, 155, 40, 100))
    pygame.draw.rect(screen, "#c29f2e", (480, 545, 40, 100))
    pygame.draw.rect(screen, "#c29f2e", (255, 380, 100, 40))
    pygame.draw.rect(screen, "#c29f2e", (645, 380, 100, 40))
    pygame.draw.rect(screen, "#c29f2e", (0, 50, 1000, 700), 25)
