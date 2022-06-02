import pygame

pygame.init()
winx, winy = 1000, 683
window = pygame.display.set_mode((winx, winy))
pygame.display.set_caption("KBHero")
running = True
clock = pygame.time.Clock()
refresh = 10
background = pygame.image.load("spacebro.jpg")

# colors
darkRed = (255, 0, 0)
lightRed = (255, 127, 130)
darkOrange = (255, 154, 25)
lightOrange = (255, 199, 127)
darkYellow = (255, 242, 26)
lightYellow = (255, 249, 153)
darkGreen = (1, 158, 0)
lightGreen = (153, 255, 153)
darkBlue = (0, 0, 255)
lightBlue = (135, 206, 235)
purple = (130, 5, 250)
position = 1000
radius = 18
edge = 60


class Note:

    def __init__(self, clickable, lane):
        this.clickable = clickable
        this.line = line


def draw(color):
    if color == 'r':
        pygame.draw.circle(window, purple, (position, 45), radius, 0)
    if color == 'o':
        pygame.draw.circle(window, purple, (position, 120), radius, 0)
    if color == 'y':
        pygame.draw.circle(window, purple, (position, 195), radius, 0)
    if color == 'g':
        pygame.draw.circle(window, purple, (position, 270), radius, 0)
    if color == 'b':
        pygame.draw.circle(window, purple, (position, 345), radius, 0)


while running:
    #window.fill((0, 0, 0))
    window.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(window, darkRed, pygame.Rect(15, 15, edge, 60))
    pygame.draw.rect(window, darkOrange, pygame.Rect(15, 90, edge, 60))
    pygame.draw.rect(window, darkYellow, pygame.Rect(15, 165, edge, 60))
    pygame.draw.rect(window, darkGreen, pygame.Rect(15, 240, edge, 60))
    pygame.draw.rect(window, darkBlue, pygame.Rect(15, 315, edge, 60))

    key = pygame.key.get_pressed()

    if key[pygame.K_q]:
        pygame.draw.rect(window, lightRed, pygame.Rect(15, 15, 60, 60))
    if key[pygame.K_w]:
        pygame.draw.rect(window, lightOrange, pygame.Rect(15, 90, 60, 60))
    if key[pygame.K_e]:
        pygame.draw.rect(window, lightYellow, pygame.Rect(15, 165, 60, 60))
    if key[pygame.K_r]:
        pygame.draw.rect(window, lightGreen, pygame.Rect(15, 240, 60, 60))
    if key[pygame.K_SPACE]:
        pygame.draw.rect(window, lightBlue, pygame.Rect(15, 315, 60, 60))

    draw('r')
    draw('o')
    draw('y')
    draw('g')
    draw('b')
    position -= 15
    if (position - radius) <= edge:
        print("contact")
    pygame.display.flip()
    clock.tick(60)
    #pygame.time.delay(refresh)
    #pygame.display.update()

pygame.quit()