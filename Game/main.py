import pygame
from alien import Alien
from bullet import Bullet
from enemy import Enemy


pygame.init()

pygame.display.set_caption("Alien VS Monsters")

display_width = 1024
display_height = 768

Screen = pygame.display.set_mode((display_width, display_height))

alien = pygame.Rect(display_width / 2 - 12, display_height / 2 - 12, 25, 25)

background = pygame.image.load('sky1.png')

alien = Alien(40, 40, 40)

bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

font = pygame.font.Font(None, 25)

period_enemy = 200
current_period_enemy = 0

result = 0
next_level = 5

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                if len(bullet_group.sprites()) < 5:
                    bullet_group.add(Bullet(alien.rect.centerx, alien.rect.centery, alien.motion))

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        alien.rect.x -= alien.speed
        alien.motion = 4
    if key[pygame.K_RIGHT]:
        alien.rect.x += alien.speed
        alien.motion = 2
    if key[pygame.K_UP]:
        alien.rect.y -= alien.speed
        alien.motion = 1
    if key[pygame.K_DOWN]:
        alien.rect.y += alien.speed
        alien.motion = 3

    if current_period_enemy >= period_enemy:
        enemy_group.add(Enemy())
        current_period_enemy = 0

    bullet_group.update()
    enemy_group.update()

    if pygame.sprite.spritecollide(alien, enemy_group, False):
        run = False

    if pygame.sprite.groupcollide(bullet_group, enemy_group, True, True):
        result += 1
        if result >= next_level:
            next_level += 5
            period_enemy /= 2

    Screen.fill((0, 255, 0, 255))
    Screen.blit(background, (0, 0))
    Screen.blit(alien.image, alien.rect)
    bullet_group.draw(Screen)
    enemy_group.draw(Screen)
    Screen.blit(font.render(f'KILLS: {result}', True, (0, 0, 0), (0, 255, 0, 255)), (30, 30))
    Screen.blit(font.render(f'LEVEL: {int(next_level / 5)}', True, (0, 0, 0), (0, 255, 0, 255)), (200, 30))
    pygame.display.flip()
    pygame.time.delay(20)
    current_period_enemy += 1

pygame.quit()



