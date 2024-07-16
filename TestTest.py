import pygame, time, itertools

pygame.init()

# background image
walkRight = pygame.image.load('2.png')
walkLeft = pygame.image.load('2.png')
bg = pygame.image.load("bg.jpg")
idle = [pygame.image.load('2.png'), pygame.image.load('3.png'), pygame.image.load('3.png')]
standcount = True

clock = pygame.time.Clock()

# jump
isJump = False
jumpcount = 10

# window
display_width = 600
display_height = 400
win = pygame.display.set_mode((display_width, display_height))

# title & icon
pygame.display.set_caption("Grand Theft Ewok")
icon = pygame.image.load('1.png')
pygame.display.set_icon(icon)

# player creds
x = 50
y = 280
vel = .1

# playerIMG
playerIMG = pygame.image.load('1.png')


def player(x, y):
    global standcount
    global walkcount
    win.blit(bg, (0, 0))
    # win.blit(playerIMG, (x,y))

    if walkcount + 1 >= 9:
        walkcount = 0

    if standcount + 1 >= 9:
        standcount = 0

    if left:
        win.blit(idle[walkcount // 3], (x, y))
        walkcount += 1
    elif right:
        win.blit(idle[walkcount // 3], (x, y))
        walkcount += 1
    elif standcount:
        p = 0
        for frame in idle:
            win.blit(idle[p], (x, y))
            p += 1
            if p >= 2:
                p = 0
                continue

    pygame.display.update()


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > (vel - 25):
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_d] and x < 520:
        x += vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkcount = 0
        standcount = True

    if not (isJump):
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

    player(x, y)
    pygame.display.update()

pygame.quit()