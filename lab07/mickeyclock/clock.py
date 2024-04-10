import pygame
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((700, 525))
i = pygame.image.load('mm.png')
l = pygame.image.load('left.png')
r = pygame.image.load('right.png')
new_size = (700, 525)
bg = pygame.transform.scale(i, (700, 525))

def rotateRightArm(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

def rotateLeftArm(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect)

leftarm = pygame.transform.scale(l, (60, 320))
leftarm = pygame.transform.rotate(leftarm, -9)

rightarm = pygame.transform.scale(r, (261, 215))
rightarm = pygame.transform.rotate(rightarm, (-9))

x1, y1 = 296, 100
angle1 = 8
x2, y2 = 204, 136
angle2 = -45
while True:
        clock.tick(60)
        screen.blit(bg, (0, 0))

        rotateLeftArm(screen, leftarm, (x1, y1), angle1)
        angle1 += -0.1
        rotateRightArm(screen, rightarm, (x2, y2), angle2)
        angle2 += -0.002

        pygame.display.flip()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        exit()