# Hoang Phuc Luan Truong
# Pi Estimate program with graphical user interface

from math import sqrt
import pygame, random

SIZE = 600
RADIUS = SIZE / 2
RED = (255, 0, 0)
BLUE = (128, 166, 229)
BLACK = (0, 0, 0)
total = 0
in_circle = 0
pi = 0
output_pi = 0
timer = 0


class Point(pygame.sprite.Sprite):
    def __init__(self, color, pos_x, pos_y) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([2, 2])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x + RADIUS, pos_y + RADIUS] 



# generate a random point and check if it is in the circle or not
def generate(sprite_group):
    pos_x = random.randint(-RADIUS, RADIUS)
    pos_y = random.randint(-RADIUS, RADIUS)
    dis_to_origin = sqrt(pos_x * pos_x + pos_y * pos_y)

    global total, pi, in_circle, output_pi
    total += 1
    # if the distance to the origin > the circle's radius => it is outside of the circle
    if dis_to_origin > RADIUS:
        color = RED
    # else, the point is inside of the circle    
    else:
        in_circle += 1
        color = BLUE
    pi = 4 * in_circle / total
    # add the point generated to the sprite group
    point = Point(color, pos_x, pos_y)
    sprite_group.add(point)

    # we don't want the output to constantly change too fast
    # therefore, we update the output after a period of time
    if (total % 50 == 0):
        output_pi = pi


def create_gui():
    pygame.init()                                           # initialize pygame
    sprite_group = pygame.sprite.Group()                    # the group that contains all sprites
    clock = pygame.time.Clock()
    pygame.display.set_caption('Estimate Pi')               # the window's title
    screen = pygame.display.set_mode((SIZE, SIZE + 50))     # the screen
    screen.fill(BLACK)                                      # black background
    font = pygame.font.SysFont("monospace bold", 32)        # text output font
    
    while True:
        process(sprite_group, screen, clock)
        display_output(font, screen)
        input_handling()


def input_handling():
    # quitting when user closes windows or presses esc
    for event in pygame.event.get():
        if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            quit()


def process(sprite_group, screen, clock):
    pygame.display.flip()
    sprite_group.draw(screen)
    generate(sprite_group)
    clock.tick(60)


# display the output text at the bottom of the screen
def display_output(font, screen):
    output = font.render("      " + str("%.20f" % round(output_pi, 20)) + "      ", True, BLUE, BLACK)
    rect = output.get_rect()
    rect.center = (RADIUS, SIZE + 25)
    screen.blit(output, rect)


if __name__ == "__main__":
    create_gui()
