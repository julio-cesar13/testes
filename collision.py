import pygame
import math
from draw_screen import draw_object


def load_images(sprite, ang, w, h, xp, yp, image):
    sprite.image = pygame.image.load(image)
    sprite.image = pygame.transform.scale(sprite.image, (w, h))
    sprite.image = pygame.transform.rotate(sprite.image, ang)
    cor_x = sprite.image.get_rect(center=(xp + 25, yp + 25))
    sprite.rect = cor_x
    return cor_x


def collision_objects(ang_left, ang_right, xp1, xp2, yp1, yp2,screen):
    # players collide with objects
    collision_1 = pygame.sprite.Sprite()
    collision_1_cor = load_images(collision_1, ang_left, 10, 50,
                                  xp1 + 30 * math.cos(math.radians(-ang_left)),
                                  yp1 + 30 * math.sin(math.radians(-ang_left)), "collision_object.png")

    collision_2 = pygame.sprite.Sprite()
    collision_2_cor = load_images(collision_2, ang_right, 10, 50, xp2 - 30 * math.sin(math.radians(ang_right + 90)),
                                  yp2 - 30 * math.cos(math.radians(ang_right + 90)), "collision_object.png")

    if draw_object(screen, collision_1):
        per_1 = True
    else:
        per_1 = False

    # collision player 2 with objects
    if draw_object(screen, collision_2):
        per_2 = True
    else:
        per_2 = False

    return per_1, per_2
