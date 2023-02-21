import pygame


class Arena:
    def __init__(self, num_arena, screen):
        self.num_arena = num_arena
        self.screen = screen
        self.yp = 75

    def draw_object(self):
        # draw L left
        list_reacts = []

        # draw screen
        pygame.draw.line(self.screen, (255, 255, 255),(650, 75), (650, 725), 5)
        camp_player_1 = pygame.draw.rect(self.screen, (255, 255, 255), (20, 277, 80, 220), 5)
        camp_player_2 = pygame.draw.rect(self.screen, (255, 255, 255), (1200, 277, 80, 220), 5)
        self.get_rect_camp(camp_player_1, camp_player_2)
        screen_1 = pygame.draw.rect(self.screen, "#c29f2e", (0, 50, 1300, 25))
        list_reacts.append(screen_1)

        screen_2 = pygame.draw.rect(self.screen, "#c29f2e", (0, 725, 1300, 25))
        list_reacts.append(screen_2)

        screen_3 = pygame.draw.rect(self.screen, "#c29f2e", (1275, 75, 25, 650))
        list_reacts.append(screen_3)

        screen_6 = pygame.draw.rect(self.screen, "#c29f2e", (0, 75, 25, 650))
        list_reacts.append(screen_6)
        return list_reacts

    def get_rect_camp(self, camp_1, camp_2):
        return camp_1, camp_2

