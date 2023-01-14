import pygame
from draw_screen import draw_object
from move import move

pygame.init()
pygame.font.init()

size = (1000, 750)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Breakout Game")
screen.fill("#9f4100")

font = pygame.font.Font("PressStart2P.ttf", 30)

score_point_player1 = font.render("0", True, (0, 255, 0))
score_point_player1_rect = score_point_player1.get_rect()
score_point_player1_rect.center = (350, 30)

score_point_player2 = font.render("0", True, (0, 0, 255))
score_point_player2_rect = score_point_player2.get_rect()
score_point_player2_rect.center = (650, 30)

player1 = pygame.sprite.Sprite()
player1.image = pygame.image.load("player1.png")
player1.image = pygame.transform.scale(player1.image, (50, 50))
player1.image = pygame.transform.rotate(player1.image, 180)
player1.rect = pygame.Rect(910, 380, 0, 0)
x_player1 = 910
y_player2 = 380
angle = 0
player2 = pygame.image.load("player2.png")
player2 = pygame.transform.scale(player2, (50, 50))
player2_x = 50
player2_y = 380

clock = pygame.time.Clock()
angle = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("#9f4100")

    a = move(player1, angle)[0]
    b = move(player1, angle)[1]
    c = move(player1, angle)[2]
    angle = c
    screen.blit(a, b)

    draw_object(screen)

    screen.blit(player2, (50, 380))
    screen.blit(score_point_player1, score_point_player1_rect)
    screen.blit(score_point_player2, score_point_player2_rect)
    pygame.display.flip()
    clock.tick(50)
