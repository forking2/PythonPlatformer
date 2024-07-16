import pygame

pygame.init()

# Зображення для анімації
walkRight = [pygame.image.load('2.png')]  # Якщо у вас більше зображень, додайте їх сюди
walkLeft = [pygame.image.load('22.png')]
runRight = [pygame.image.load('3.png')]
runLeft = [pygame.image.load('33.png')]
bg = pygame.image.load("Bg4.jpg")
idle = [pygame.image.load('1.png')]  # список idle має один елемент

# Ініціалізація змінних
standcount = 0
walkcount = 0
left = False
right = False

clock = pygame.time.Clock()

# Параметри стрибка
isJump = False
jumpcount = 10

# Вікно гри
display_width = 1200
display_height = 800
win = pygame.display.set_mode((display_width, display_height))

# Назва гри
pygame.display.set_caption("Grand Theft Ewok")

# Координати та швидкість гравця
x = 220
y = 650
vel = 8  # збільшено для помітнішого руху

def player(x, y):
    global standcount
    global walkcount
    win.blit(bg, (0, 0))

    if walkcount + 1 >= 9:
        walkcount = 0

    if standcount + 1 >= 9:
        standcount = 0

    if left:
        win.blit(walkLeft[0], (x, y))  # Використовуємо індекс 0, оскільки тільки один елемент у списку
        walkcount += 1
    elif right:
        win.blit(walkRight[0], (x, y))  # Використовуємо індекс 0, оскільки тільки один елемент у списку
        walkcount += 1
    else:
        win.blit(idle[0], (x, y))  # Виправлено індексацію
        standcount += 1

    pygame.display.update()

# Основний цикл гри
running = True
while running:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Рух
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > vel:
        x -= vel
        left = True
        right = False
        standcount = 0
    elif keys[pygame.K_d] and x < display_width - vel - idle[0].get_width():
        x += vel
        right = True
        left = False
        standcount = 0
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

    player(x, y)

pygame.quit()