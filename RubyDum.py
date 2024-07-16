# import pygame
#
# pygame.init()
#
# walkRight = [pygame.image.load('2.png'), pygame.image.load('3.png')]
# walkLeft = [pygame.image.load('22.png'), pygame.image.load('33.png')]
# bg = pygame.image.load("bg4.jpg")
# idle = [pygame.image.load('1.png'), pygame.image.load('11.png')]
# platform=pygame.image.load('Platform2.png')
#
# standcount = 0
# walkcount = 0
# left = False
# right = False
# last_direction = None
#
# clock = pygame.time.Clock()
#
# isJump = False
# jumpcount = 10
#
# display_width = 1200
# display_height = 800
# win = pygame.display.set_mode((display_width, display_height))
#
# pygame.display.set_caption("Grand Theft Ewok")
#
# x = 50
# y = 650
# vel = 5  #
# def player(x, y):
#     global standcount
#     global walkcount
#     win.blit(bg, (0, 0))
#
#     if walkcount + 1 >= 8:
#         walkcount = 0
#
#     if standcount + 1 >= 9:
#         standcount = 0
#     if left and isJump == True:
#         win.blit(walkLeft[0], (x, y))
#         walkcount += 1
#     elif right and isJump == True:
#         win.blit(walkRight[0], (x, y))
#         walkcount += 1
#     elif left:
#         win.blit(walkLeft[walkcount // 4], (x, y))
#         walkcount += 1
#         pygame.time.delay(30)
#     elif right:
#         win.blit(walkRight[walkcount // 4], (x, y))
#         walkcount += 1
#         pygame.time.delay(30)
#     else:
#         if last_direction == 'left':
#             win.blit(idle[1], (x, y))
#         else:
#             win.blit(idle[0], (x, y))
#         standcount += 1
#
#     pygame.display.update()
#
# # Основний цикл гри
# running = True
# while running:
#     clock.tick(30)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     # Рух
#     keys = pygame.key.get_pressed()
#
#     if keys[pygame.K_a] and x > vel:
#         x -= vel
#         left = True
#         right = False
#         standcount = 0
#         last_direction = 'left'
#     elif keys[pygame.K_d] and x < display_width - vel - idle[0].get_width():
#         x += vel
#         right = True
#         left = False
#         standcount = 0
#         last_direction = 'right'
#     else:
#         right = False
#         left = False
#         walkcount = 0
#
#     if not isJump:
#         if keys[pygame.K_SPACE]:
#             isJump = True
#             left = False
#             right = False
#     else:
#         if jumpcount >= -10:
#             neg = 1
#             if jumpcount < 0:
#                 neg = -1
#             y -= (jumpcount ** 2) * 0.5 * neg
#             jumpcount -= 1
#         else:
#             isJump = False
#             jumpcount = 10
#
#     player(x, y)
















import pygame

pygame.init()

walkRight = [pygame.image.load('2.png'), pygame.image.load('3.png')]
walkLeft = [pygame.image.load('22.png'), pygame.image.load('33.png')]
bg = pygame.image.load("bg4.jpg")
idle = [pygame.image.load('1.png'), pygame.image.load('11.png')]
platform = pygame.image.load('Platform2.png')

standcount = 0
walkcount = 0
left = False
right = False
last_direction = None

clock = pygame.time.Clock()

isJump = False
jumpcount = 10

display_width = 1200
display_height = 800
win = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Grand Theft Ewok")

x = 50
y = 650
vel = 5  #

# Платформы (пример координат)
platforms = [
    (300, 600),
    (800, 500),
    (100, 400)
]

def player(x, y):
    global standcount
    global walkcount
    win.blit(bg, (0, 0))

    # Отображение платформ
    for platform_pos in platforms:
        win.blit(platform, platform_pos)

    if walkcount + 1 >= 8:
        walkcount = 0

    if standcount + 1 >= 9:
        standcount = 0
    if left and isJump == True:
        win.blit(walkLeft[0], (x, y))
        walkcount += 1
    elif right and isJump == True:
        win.blit(walkRight[0], (x, y))
        walkcount += 1
    elif left:
        win.blit(walkLeft[walkcount // 4], (x, y))
        walkcount += 1
        pygame.time.delay(30)
    elif right:
        win.blit(walkRight[walkcount // 4], (x, y))
        walkcount += 1
        pygame.time.delay(30)
    else:
        if last_direction == 'left':
            win.blit(idle[1], (x, y))
        else:
            win.blit(idle[0], (x, y))
        standcount += 1

    pygame.display.update()

# Основний цикл гри
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel
        left = True
        right = False
        standcount = 0
        last_direction = 'left'
    elif keys[pygame.K_d] and x < display_width - vel - idle[0].get_width():
        x += vel
        right = True
        left = False
        standcount = 0
        last_direction = 'right'
    else:
        right = False
        left = False
        walkcount = 0


    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
            y -= (jumpcount ** 2) * 0.5 * neg
            jumpcount -= 1
        else:
            isJump = False
            jumpcount = 10

    # Проверка столкновений с платформами
    for platform_pos in platforms:
        platform_rect = pygame.Rect(platform_pos[0], platform_pos[1], platform.get_width(), platform.get_height())
        player_rect = pygame.Rect(x, y, idle[0].get_width(), idle[0].get_height())

        if player_rect.colliderect(platform_rect) and not isJump:
            y = platform_pos[1] - idle[0].get_height()
            isJump = False
            jumpcount = 10

    player(x, y)

pygame.quit()

























# .......
# class Object(pygame.sprite.Sprite):
#      def __init__(self,x,y,file, rect, image):
#         pygame.sprite.Sprite.__init__(self)
#
#
#
#         self.image=pygame.image.load(file).convert_alpha()
#         self.rect=self.image.get_rect(center=(x,y))
#
# class platforms(Object):
#     def __init__(self, x=100, y=400, file='Platform2.png'):
#         pygame.sprite.Sprite.__init__(self)
#         self.x = x
#         self.y = y
#         self.file = file
#
#         self.image = pygame.image.load(file).convert_alpha()
#         self.rect = self.image.get_rect(center=(x, y))



















pygame.quit()