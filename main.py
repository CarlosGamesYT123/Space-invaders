import random
import time
import sys
import math
import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Space Invaders")
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (800, 600))
playerImg = pygame.image.load("player.png")
playerImg = pygame.transform.scale(playerImg, (64, 64))
playerImg2 = pygame.image.load("player2.png")
playerImg2 = pygame.transform.scale(playerImg2, (64, 64))
playerImg3 = pygame.image.load("player3.png")
playerImg3 = pygame.transform.scale(playerImg3, (64, 64))
playerImg4 = pygame.image.load("player4.png")
playerImg4 = pygame.transform.scale(playerImg4, (64, 64))
playerImg5 = pygame.image.load("player5.png")
playerImg5 = pygame.transform.scale(playerImg5, (64, 64))
playerwinner = pygame.image.load("winner.png")
playerwinner = pygame.transform.scale(playerwinner, (64, 64))
playerX = 370
playerY = 480
playerX_change = 0
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)
bullet = pygame.image.load("laser.png")
bullet = pygame.transform.scale(bullet, (32, 32))
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"
score_value = 0
ammo_fired = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10
ammos = pygame.font.Font("freesansbold.ttf", 32)
over_font = pygame.font.Font("freesansbold.ttf", 64)
instructions_font = pygame.font.Font("freesansbold.ttf", 14)
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 200)
bright_blue = (0, 0, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
pause = False
def show_score(x, y):
    global score
    score = font.render("Score: " + str(score_value), True, white)
    screen.blit(score, (x, y))
def show_instructions(x, y):
    directions = instructions_font.render("Press P to pause, D or right arrow to move "
                                          "right, A or left arrow to move left, Space to fire lasers", True, white)
    screen.blit(directions, (x, y))
def ammo_spent(x, y):
    ammo_used = ammos.render("Ammo fired: " + str(ammo_fired), True, white)
    screen.blit(ammo_used, (x, y))
def display_fps(x, y):
    fps = font.render("FPS(max: 120fps): " + str(int(clock.get_fps())), True, white)
    screen.blit(fps, (x, y))
    pygame.display.flip()
    clock.tick(120)
def display_ship(x, y):
    if score_value < 10:
        ships = ammos.render("Ship: " + "ship 1" + " Next ship: " + "ship 2", True, white)
        screen.blit(ships, (x, y))
    elif 9 < score_value < 20:
        ships = ammos.render("Ship: " + "ship 2" + " Next ship: " + "ship 3", True, white)
        screen.blit(ships, (x, y))
    elif 19 < score_value < 30:
        ships = ammos.render("Ship: " + "ship 3" + " Next ship: " + "ship 4", True, white)
        screen.blit(ships, (x, y))
    elif 29 < score_value < 40:
        ships = ammos.render("Ship: " + "ship 4" + " Next ship: " + "ship 5", True, white)
        screen.blit(ships, (x, y))
    elif 39 < score_value < 50:
        ships = ammos.render("Ship: " + "ship 5" + " Next ship: " + "Final ship", True, white)
        screen.blit(ships, (x, y))
    else:
        ships = ammos.render("Ship: " + "Final ship" + " Next ship: " + "none", True, white)
        screen.blit(ships, (x, y))
def game_over_text():
    screen.fill(black)
    if score_value < 50:
        over_text = over_font.render("GAME OVER!", True, white)
        
        sys.exit()
    else:
        over_text = over_font.render("VICTORY!", True, white)
    screen.blit(over_text, (200, 250))
    screen.blit(score, (200, 305))
def player(x, y):
    if score_value < 10:
        screen.blit(playerImg, (x, y))
    elif 9 < score_value < 20:
        screen.blit(playerImg2, (x, y))
    elif 19 < score_value < 30:
        screen.blit(playerImg3, (x, y))
    elif 29 < score_value < 40:
        screen.blit(playerImg4, (x, y))
    elif 39 < score_value < 50:
        screen.blit(playerImg5, (x, y))
    else:
        screen.blit(playerwinner, (x, y))
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x + 16, y + 10))
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == "play":
                while True:
                    game_loop()
            elif action == "unpause":
                unpause()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, ic, (x, y, w, h))
    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    smalltext = smalltext.render(msg, True, black)
    screen.blit(smalltext, ((x + (w / 2)), (y + (h / 2))))
def unpause():
    global pause
    pause = False
def paused():
    bigtext = pygame.font.Font("freesansbold.ttf", 64)
    bigtext = bigtext.render("Paused", True, white)
    screen.blit(bigtext, (200, 250))
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Continue", 100, 400, 300, 101, blue, bright_blue, "unpause")
        button("Quit", 450, 400, 300, 101, red, bright_red, "quit")
        pygame.display.update()
def game_intro():
    startbackground = pygame.image.load("startbackground.png")
    startbackground = pygame.transform.scale(startbackground, (800, 600))
    screen.blit(startbackground, (0, 0))
    bigtext = pygame.font.Font("freesansbold.ttf", 64)
    bigtext = over_font.render("Space Invaders", True, white)
    screen.blit(bigtext, (200, 250))
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play", 100, 400, 300, 101, blue, bright_blue, "play")
        button("Quit", 450, 400, 300, 101, red, bright_red, "quit")
        pygame.display.update()
def game_loop():
    global pause
    global bullet_state
    global ammo_fired
    global playerX
    global playerX_change
    global bulletX
    global bulletY
    global score_value
    screen.fill(black)
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                    ammo_fired = int(ammo_fired) + 1
            if event.key == pygame.K_p:
                pause = True
                paused()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    for i in range(num_of_enemies):
        if enemyY[i] > 395:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change  
    player(playerX, playerY)
    show_score(textX, textY)
    ammo_spent(textX, int(textY) + 25)
    show_instructions(textX, int(textY) + 55)
    display_ship(textX, int(textY) + 75)
    display_fps(int(textX) + 350, textY)
    pygame.display.update()
game_intro()