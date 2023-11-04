import pygame
from fighter import Fighter

pygame.init()


#Creating Game Window - Ryan Rahman

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DBZ Fighter")

#set framerate - Owen Gibbs
clock = pygame.time.Clock()
FPS = 60

#define colours - Owen Gibbs
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#Define Fighter Variables - Ryan Rahman
GOKU_WIDTH = 90
GOKU_HEIGHT = 166
GOKU_SCALE = 1
GOKU_DATA = [GOKU_WIDTH,GOKU_HEIGHT, GOKU_SCALE]
VEGETA_WIDTH = 90
VEGETA_HEIGHT = 153
VEGETA_SCALE = 1
VEGETA_DATA = [VEGETA_WIDTH,VEGETA_HEIGHT,VEGETA_SCALE]


#Load Background - Ryan Rahman
bg_image = pygame.image.load("bg_image - instasize.jpg").convert_alpha()

#Load Spritesheets - Ryan Rahman
goku_sheet = pygame.image.load("Goku/Goku Super Saiyan.png").convert_alpha()
vegeta_sheet = pygame.image.load("Vegeta/Vegeta Super Saiyan.png").convert_alpha()

#Define number of steps in each animation - Ryan Rahman
GOKU_ANIMATION_STEPS = [6,8,4,6,3,3,3,8,3,3,3,3,5,4,6,6,6,6,4,6,6,4,6,5,6,6,7,6,6,6,6,6,9,9,6,10,7,7,4,9,4,4,2,2,4,2,2,4,2,2,4,4,4,7,7,4,3,2,2]
VEGETA_ANIMATION_STEPS = [2,6,7,6,4,6,3,3,3,7,3,3,3,4,7,4,5,10,4,7,4,6,7,4,5,6,4,4,4,9,5,7,4,7,12,7,4,6,6,12,10,4,4,2,2,4,2,2,4,2,2,4,4,4,8,4,7,10,2]

#Function to Draw Background - Ryan Rahman
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))

#function for drawing fighter health bars - Owen Gibbs
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x -2, y -2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

#create two instances of fighter - Owen Gibbs
fighter_1 = Fighter(200, 310,False, GOKU_DATA, goku_sheet,GOKU_ANIMATION_STEPS)
fighter_2 = Fighter(700, 310,False, VEGETA_DATA, vegeta_sheet,VEGETA_ANIMATION_STEPS)

#Game Loop - Ryan Rahman
run = True
while run:
    
    clock.tick(FPS)

    #Draw Background - Ryan Rahman
    draw_bg()

    #show player stats - Owen Gibbs
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)

    #move fighters - Owen Gibbs
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    #fighter_2.move()

    #draw fighter - Owen Gibbs
    fighter_1.draw(screen)
    fighter_2.draw(screen)


    #Event Handler - Ryan Rahman
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Update Display - Ryan Rahman
    pygame.display.update()
            

#exit pygame - Ryan Rahman

pygame.quit()
