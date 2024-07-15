

import pygame
pygame.init()


class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,file, rect, image):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load(file).convert_alpha()
        self.rect=self.image.get_rect(center=(x,y))

width=1000
height=500


sc = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

class player(Object):
    def __init__(self, x=100, y=400, file='1.png'):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.file = file

        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))


running = True

while running:
    sc.fill(pygame.Color('white'))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(60)

sc.blit(player.image, player.rect)
pygame.display.flip()
pygame.display.update()
