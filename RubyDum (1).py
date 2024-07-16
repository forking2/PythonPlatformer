import pygame
import time

pygame.init()

walkRight = [pygame.image.load('2.png'), pygame.image.load('3.png')]
walkLeft = [pygame.image.load('22.png'), pygame.image.load('33.png')]
bg = pygame.image.load("bg4.jpg")
idle = [pygame.image.load('1.png'), pygame.image.load('11.png')]
platform = pygame.image.load('Platform2.png')
Threes = [pygame.image.load('TheersCadr1.png'), pygame.image.load('ThreeCadr2.png')]

standcount = 0
walkcount = 0
left = False
right = False
last_direction = None

clock = pygame.time.Clock()

isJump = False
jumpcount = 10
fall_speed = 7

display_width = 1200
display_height = 800
win = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption("Ruby Dum")

x = 50
y = 650
vel = 5

trees_positions = [
    (150, 500),
    (950, 500)
]

platforms = [
    (760, 600),
    (50, 660),
    (683, 400)
]

tree_frame = 0
tree_last_update = time.time()
tree_animation_delay = 0.3

def player(x, y):
    global standcount
    global walkcount
    global tree_frame
    global tree_last_update

    win.blit(bg, (0, 0))

    for platform_pos in platforms:
        win.blit(platform, platform_pos)

    current_time = time.time()
    if current_time - tree_last_update >= tree_animation_delay:
        tree_frame = (tree_frame + 1) % len(Threes)
        tree_last_update = current_time

    for tree_pos in trees_positions:
        win.blit(Threes[tree_frame], tree_pos)

    if walkcount + 1 >= 8:
        walkcount = 0

    if standcount + 1 >= 9:
        standcount = 0

    if left and isJump:
        win.blit(walkLeft[0], (x, y))
        walkcount += 1
    elif right and isJump:
        win.blit(walkRight[0], (x, y))
        walkcount += 1
    elif left:
        win.blit(walkLeft[walkcount // 4], (x, y))
        walkcount += 1
    elif right:
        win.blit(walkRight[walkcount // 4], (x, y))
        walkcount += 1
    else:
        if last_direction == 'left':
            win.blit(idle[1], (x, y))
        else:
            win.blit(idle[0], (x, y))
        standcount += 1

    pygame.display.update()

def check_platform_collision(x, y):
    player_rect = pygame.Rect(x, y, idle[0].get_width(), idle[0].get_height())

    for platform_pos in platforms:
        platform_rect = pygame.Rect(platform_pos[0], platform_pos[1], platform.get_width(), platform.get_height())

        if player_rect.colliderect(platform_rect):
            return platform_pos[1] - idle[0].get_height()

    return None

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

    new_y = check_platform_collision(x, y + vel)

    if new_y is not None and not isJump:
        y = new_y
    elif new_y is None and not isJump:
        y += fall_speed
        jumpcount = 0

    if y > display_height:
        font = pygame.font.SysFont(None, 75)
        text = font.render('You Lost', True, (255, 0, 0))
        win.blit(text, (display_width // 2 - text.get_width() // 2, display_height // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(1000)
        running = False

    player(x, y)

pygame.quit()