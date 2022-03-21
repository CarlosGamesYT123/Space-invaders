


clock = pygame.time.Clock()
screen = pygame.display.set_mode([800, 800])
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

