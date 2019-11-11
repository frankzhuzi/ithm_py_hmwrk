import pygame

pygame.init()

screen = pygame.display.set_mode((480, 700))

background = pygame.image.load("./images/background.png")

screen.blit(background, (0, 0))

hero = pygame.image.load("./images/me1.png")

screen.blit(hero, (180, 500))

pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(180, 500, 102, 126)

while True:
    clock.tick(60)

    screen.blit(background, (0, 0))

    hero_rect.y -= 1

    screen.blit(hero, hero_rect)

    pygame.display.update()

    pass

pygame.quit()
