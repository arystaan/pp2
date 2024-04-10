import pygame, sys, time, random
from pygame.locals import *
pygame.init()

clock = pygame.time.Clock()
#Создание цветов
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Перменные которые мы будем исполььзовать
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
MONEY = 0

#Созадние текстовый фалов или же просто текстов 
money = pygame.font.SysFont(None, 20)
text_money = money.render("Монеты:", True, BLACK)

font = pygame.font.SysFont(None, 60)
game_over = font.render("Game Over", True, BLACK)

screen_font = pygame.font.SysFont(None, 20)
your_score_text = screen_font.render("Ваш счет:", True, BLACK)

backgraund = pygame.image.load("AnimatedStreet.png")

#Создаем само окно
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image1 = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image1.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(100, SCREEN_HEIGHT-80))
        
    def empty_space(self):
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(100, SCREEN_HEIGHT-80))
        while pygame.sprite.collide_rect(P1, C1):
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), random.randint(100, SCREEN_HEIGHT-80))
        return self.rect.center

#Создание классов для врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if(self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

#Создание класса для игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys [K_UP]:
                self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys [K_DOWN]:
                self.rect.move_ip(0, 5)
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

P1 = Player()
E1 = Enemy()
C1 = coin()

#Создания групп по спрайтам
enemies = pygame.sprite.Group()
enemies.add(E1)
enemy_and_player = pygame.sprite.Group()
enemy_and_player.add(E1)
enemy_and_player.add(P1)
COIN = pygame.sprite.Group()
COIN.add(C1)


#Создание посльзовательской очереди событий
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED:
            SPEED += 0.5
    
    DISPLAYSURF.blit(backgraund, (0,0))
    
    DISPLAYSURF.blit(your_score_text, (10, 10))
    scores = screen_font.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10,25))
    
    DISPLAYSURF.blit(text_money, (10, 40))
    coins = money.render(str(MONEY), True, BLACK)
    DISPLAYSURF.blit(coins, (10,55))
    DISPLAYSURF.blit(C1.image1, C1.rect)
    
    #Перемещение объектов
    for entity in enemy_and_player:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
        
    #Столкновение между игроком и врагом.
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(0.5)
        
        DISPLAYSURF.fill(WHITE)
        DISPLAYSURF.blit(game_over, (90,250))
        
        pygame.display.update()
        for entity in enemy_and_player:
            entity.kill()
        time.sleep(1.5)
        pygame.quit()
        sys.exit()
    
    #Столкновение с монеткой
    if pygame.sprite.spritecollideany(P1, COIN):
        MONEY += 1
        C1.rect.center = C1.empty_space()
        
    pygame.display.update()
    clock.tick(60)