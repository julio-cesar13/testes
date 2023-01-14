import pygame


def move(player1, angle):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        angle += 1
        rotated_image = pygame.transform.rotate(player1.image, angle)
        new_position = rotated_image.get_rect(
            center=(player1.rect.x + 25, player1.rect.y + 25))
        return rotated_image, new_position, angle
    elif keys[pygame.K_RIGHT]:
        angle -= 1
        rotated_image = pygame.transform.rotate(player1.image, angle)
        new_position = rotated_image.get_rect(
            center=(player1.rect.x + 25, player1.rect.y + 25))
        return rotated_image, new_position, angle

    if keys[pygame.K_a]:
        angle += 1
        rotated_image = pygame.transform.rotate(player1.image, angle)
        new_position = rotated_image.get_rect(
            center=(player1.rect.x + 25, player1.rect.y + 25))
        return rotated_image, new_position, angle
    elif keys[pygame.K_RIGHT]:
        angle -= 1
        rotated_image = pygame.transform.rotate(player1.image, angle)
        new_position = rotated_image.get_rect(
            center=(player1.rect.x + 25, player1.rect.y + 25))
        return rotated_image, new_position, angle
    else:
        rotated_image = pygame.transform.rotate(player1.image, angle)
        new_position = rotated_image.get_rect(
            center=(player1.rect.x + 25, player1.rect.y + 25))
        return rotated_image, new_position, angle
