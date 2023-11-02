import pygame
from fighter import Fighter

pygame.init()


#Creating Game Window

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DBZ Fighter")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#Load Background
bg_image = pygame.image.load("bg_image - instasize.jpg").convert_alpha()

#Function to Draw Background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))

#function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x -2, y -2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

#create two instances of fighter
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

#Game Loop
run = True
while run:
    
    clock.tick(FPS)

    #Draw Background
    draw_bg()

    #show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    #move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    #fighter_2.move()

    #draw fighter
    fighter_1.draw(screen)
    fighter_2.draw(screen)


    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Update Display
    pygame.display.update()
            

#exit pygame

pygame.quit()
