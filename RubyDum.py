# # import sys
# import pygame
# pygame.init()
#
#
# # screen = pygame.display.set_mode((640, 480))
# # sprite = pygame.image.load("1.png")
# #
# # screen.blit(sprite, (20, 20))
# # pygame.quit()
#
#
#
# class Object(pygame.sprite.Sprite):
#     def __init__(self,x,y,file, rect, image):
#         pygame.sprite.Sprite.__init__(self)
#
#
#
#         self.image=pygame.image.load(file).convert_alpha()
#         self.rect=self.image.get_rect(center=(x,y))
#
# width=1000
# height=500
#
#
# sc = pygame.display.set_mode((width,height))
# clock = pygame.time.Clock()
#
# class player(Object):
#     def __init__(self, x=100, y=400, file='1.png'):
#         pygame.sprite.Sprite.__init__(self)
#         self.x = x
#         self.y = y
#         self.file = file
#
#         self.image = pygame.image.load(file).convert_alpha()
#         self.rect = self.image.get_rect(center=(x, y))
#
#
# running = True
#
# while running:
#     sc.fill(pygame.Color('white'))
#
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
#
#     clock.tick(60)
#
#
# # screen.blit(sprite,(20,20))
# sc.blit( player.rect,player.image)
# pygame.display.flip()
# pygame.display.update()






import sys
import pygame
pygame.init()

width = 1000
height = 500
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
background = pygame.image.load('bg.jpg').convert()
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, file, rect, image, height, speed, pos):
        self.x = x
        self.y =  y
        self.file =  file
        self.rect = rect
        self.image =image
        self.height = height
        self.speed = speed
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

        def move(self):
            self.pos = self.pos.move(self.speed, 0)
            if self.pos.right > 500:
                self.pos.left = 0
class Player(Object):
    def __init__(self, x=100, y=400, file='1.png', ):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.file = file
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))

        def move(self):
            self.pos = self.pos.move(self.speed, 0)
            if self.pos.right > 600:
                self.pos.left = 0


player = pygame.image.load('1.png').convert()
objects = []
for x in range(10):
    o = Player(x*40,x)
    objects.append(o)
running = True
while running:
    sc.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for o in objects:
        sc.blit(background, o().pos, o().pos)
    for o in objects:
        o().move()
        sc.blit(o.image, o().pos)
    sc.blit(Player().image, Player().rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()





















