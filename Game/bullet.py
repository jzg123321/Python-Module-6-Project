import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, x, y, motion, speed=14):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.motion = motion
        self.speed = speed

    def update(self):
        if self.rect.x > 700 or self.rect.x < 0 or self.rect.y > 700 or self.rect.y < 0:
            self.kill()
        if self.motion == 1:
            self.rect.y -= self.speed
        if self.motion == 2:
            self.rect.x += self.speed
        if self.motion == 3:
            self.rect.y += self.speed
        if self.motion == 4:
            self.rect.x -= self.speed