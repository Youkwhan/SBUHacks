import pygame

pygame.init()

win = pygame.display.set_mode((1080, 500))
pygame.display.set_caption("KBHero")
clock = pygame.time.Clock()
background = pygame.image.load("milky-way.jpg")  # background picture
score = 0


class rectangle(object):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.hitbox = (self.x, self.y, width, height)  # wtf

    def draw(self, color):
        pygame.draw.rect(win, color, self.hitbox, 0)


class circle(object):
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color;
        self.vel = 5
        self.visible = True

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def hit(self):  # less than
        if (self.x - self.radius) < (rectangle.x + rectangle.width):
            self.visible = False

    def move(self):
        self.x -= self.vel


def redrawGameWindow():
    win.blit(background, (0, 0))
    text = font.render("Score: " + str(score), 1, (0, 0, 0))
    win.blit(text, (170, 10))
    fred1.draw(fred1.color)  # rectangle
    fred2.draw(fred2.color)
    fred3.draw(fred3.color)
    fred4.draw(fred4.color)
    fred5.draw(fred5.color)

    notes.draw(win)
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 30, True)

fred1 = rectangle(15, 15, 60, 60, (255, 0, 0))
fred2 = rectangle(15, 90, 60, 60, (255, 154, 130))
fred3 = rectangle(15, 165, 60, 60, (255, 242, 26))
fred4 = rectangle(15, 240, 60, 60, (1, 158, 0))
fred5 = rectangle(15, 315, 60, 60, (0, 0, 255))

notes = circle(1000, 45, 18, (130, 5, 250))

run = True
while run:
    clock.tick(30)
    # if circle.visible == True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # draw
    # change circle speed
    # check visable

    key = pygame.key.get_pressed()

    if key[pygame.K_q]:
        fred1.draw((255, 127, 130))

    if key[pygame.K_w]:
        fred2.draw((255, 199, 127))
    if key[pygame.K_e]:
        fred3.draw((255, 249, 153))

    if key[pygame.K_r]:
        fred4.draw((153, 255, 153))

    if key[pygame.K_SPACE]:
        fred5.draw((135, 206, 235))


    redrawGameWindow()
pygame.quit()
