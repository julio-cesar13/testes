import pygame

pygame.font.init()

sc_width = 1000
sc_height = 750
screen = pygame.display.set_mode((sc_width, sc_height))

green = (0, 255, 0)
blue = (0, 0, 255)

ang_left = 0
ang_right = 0

count_limit = 3
speed_ball = 5
border = 25
screen.fill("#9f4100")
pygame.display.set_caption("Breakout Game")
font = pygame.font.Font("sprites/PressStart2P.ttf", 40)
