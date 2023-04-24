import pygame


class Alien(pygame.sprite.Sprite):

    def __init__(self, x, y, size):
        pygame.sprite.Sprite.__init__(self)
        self.original_image = pygame.image.load('skull_in_a_ufo_spacecraft.png')
        self.image = pygame.transform.scale(self.original_image, (size, size))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 6
        self.motion = 1