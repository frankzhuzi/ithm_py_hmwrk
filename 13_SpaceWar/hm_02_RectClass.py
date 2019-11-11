import pygame

hero_rect = pygame.Rect(100, 500, 120, 125)

print("Original Point %d, %d" % (hero_rect.x, hero_rect.y))
print("Size %d, %d" % (hero_rect.width, hero_rect.height))
print("%d %d" % hero_rect.size)
