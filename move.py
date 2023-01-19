import pygame
import math


def move_left(keys, permission_1, xp1, yp1, ang_left):
    # Move p1
    if keys[pygame.K_w] and permission_1:
        xp1 += math.cos(math.radians(ang_left))
        yp1 -= math.sin(math.radians(ang_left))
        return xp1,yp1,ang_left

    elif keys[pygame.K_a]:
        ang_left += 1
        return xp1, yp1, ang_left

    elif keys[pygame.K_d]:
        ang_left += -1
        return xp1, yp1, ang_left
    else:
        return False


def move_right(keys, permission_2, xp2, yp2, ang_right):
    # Move p2
    if keys[pygame.K_UP] and permission_2:
        xp2 += math.cos(math.radians(ang_right + 180))
        yp2 -= math.sin(math.radians(ang_right + 180))
        return xp2,yp2,ang_right

    elif keys[pygame.K_LEFT]:
        ang_right += 1
        return xp2, yp2, ang_right

    elif keys[pygame.K_RIGHT]:
        ang_right += -1
        return xp2, yp2, ang_right
    else:
        return False
