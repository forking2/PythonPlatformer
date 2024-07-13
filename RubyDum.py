

import pygame
pygame.init()


class Object(pygame.sprite.Sprite):
    def __init__(self,x,y,file):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load(file).convert_alpha()
        self.rect=self.image.get_rect(center=(x,y))

width=1000
height=500


sc=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()

player=Object(100,400,'1.png')



while True:
    sc.fill(pygame.Color('white'))


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()


sc.blit(player.image,player.rect)





pygame.display.update()
cloock.tickt(60)