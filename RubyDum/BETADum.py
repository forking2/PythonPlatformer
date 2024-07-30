import pygame
import sys
pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
SPRITE_HEIGHT = 20
SPRITE_WIDTH = 30


class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, file, rect, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))


class Thees(Object):
    def __init__(self,x=120,y=100,file='Threes.png'):
        pygame.sprite.Sprite.__init__(self)
        self.x=x
        self.y=y
        self.file=file
        self.image=pygame.image.load(file).convert_alpha()
        self.rect=self.image.get_rect(center=(x,y))





class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)

    def move(self, up=False, down=False, left=False, right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if down:
            self.pos.top += self.speed
        if up:
            self.pos.top -= self.speed
        if self.pos.right > WIDTH:
            self.pos.left = 0
        if self.pos.top > HEIGHT - SPRITE_HEIGHT:
            self.pos.top = 0
        if self.pos.right < SPRITE_WIDTH:
            self.pos.right = WIDTH
        if self.pos.top < 0:
            self.pos.top = HEIGHT - SPRITE_HEIGHT

clock = pygame.time.Clock()
player = pygame.image.load('1.png').convert_alpha()
background = pygame.image.load('bg.jpg').convert_alpha()
screen.blit(background, (0, 0))
p = GameObject(player, 10, 3)
objects = []
for x in range(0):
    o = GameObject(player, x*40, x)
    objects.append(o)
while True:
    screen.blit(background, p.pos, p.pos)
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys[pygame.K_RIGHT]:
        p.move(right=True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(p.image, p.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(60)