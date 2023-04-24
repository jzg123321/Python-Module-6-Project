import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None, direction=None, speed=6):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('spiky-monster.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect(center=(x or random.randint(0, 700), y or random.randint(0, 700)))
        self.direction = direction or random.choice(('ver', 'hor'))
        self.speed = speed

    def update(self):
        if self.direction == 'ver':
            self.rect.y += self.speed
            if self.rect.y > 700:
                self.speed = -abs(self.speed)
            if self.rect.y < 0:
                self.speed = abs(self.speed)
        elif self.direction == 'hor':
            self.rect.x += self.speed
            if self.rect.x > 700:
                self.speed = -abs(self.speed)
            if self.rect.x < 0:
                self.speed = abs(self.speed)