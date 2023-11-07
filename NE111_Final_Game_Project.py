# Initialization - Zain Khalil
import pygame  
from pygame import mixer
from fighter import Fighter

mixer.init()
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

#define game variables - Ryaan Mohideen
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0,0] ##player scores - [P1, P2]
round_over = False
ROUND_OVER_COOLDOWN = 2000


#Define Fighter Variables - Ryan Rahman
GOKU_WIDTH = 150
GOKU_HEIGHT = 175
GOKU_SCALE = 1
GOKU_DATA = [GOKU_WIDTH,GOKU_HEIGHT, GOKU_SCALE]
VEGETA_WIDTH = 150
VEGETA_HEIGHT = 137
VEGETA_SCALE = 1.2
VEGETA_DATA = [VEGETA_WIDTH,VEGETA_HEIGHT,VEGETA_SCALE]

# Load Music and Sound Effects - Zain Khalil
pygame.mixer.music.load("assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5) # Volume of music
pygame.mixer.music.play(-1, 0.0, 5000) # Repitition, Slowly Fades in @ Beginning
sword_fx = pygame.mixer.Sound("assets/audio/sword.wav") # Selected Sound effect for 
sword_fx.set_volume(0.5)
magic_fx = pygame.mixer.Sound("assets/audio/sword.wav") # Selected Sound effect for 
magic_fx.set_volume(0.5)

#Load Background - Ryan Rahman
bg_image = pygame.image.load("assets/bg_image - instasize.jpg").convert_alpha()

#Load Spritesheets - Ryan Rahman
goku_sheet = pygame.image.load("assets/Goku/Goku Super Saiyan.png").convert_alpha()
vegeta_sheet = pygame.image.load("assets/Vegeta/vegeta.png").convert_alpha()

#Define number of steps in each animation - Ryan Rahman
GOKU_ANIMATION_STEPS = [6,8,4,6,3,8,3,4,6,9,2,4,3]
VEGETA_ANIMATION_STEPS = [6,6,4,6,3,7,3,4,6,5,2,3,4]

#define font - Ryaan Mohideen
count_font = pygame.font.Font("assets/pixelated_princess.ttf", 80)
score_font = pygame.font.Font("assets/pixelated_princess.ttf", 35)

#function for drawing text - Ryaan Mohideen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))
    
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
fighter_1 = Fighter(1, 200, 310,False, GOKU_DATA, goku_sheet,GOKU_ANIMATION_STEPS)
fighter_2 = Fighter(2, 700, 310,False, VEGETA_DATA, vegeta_sheet,VEGETA_ANIMATION_STEPS)

#Game Loop - Ryan Rahman
run = True
while run:
    
    clock.tick(FPS)

    #Draw Background - Ryan Rahman
    draw_bg()

    #show player stats - Owen Gibbs
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 580, 20)
    ##show scores - Ryaan Mohideen
    draw_text("P1: "  + str(score[0]), score_font, RED, 20, 60 )
    draw_text("P2: "  + str(score[1]), score_font, RED, 580, 60 )
    #update countdown - Ryaan Mohideen
    if intro_count <= 0:
        #move fighters - Owen Gibbs
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
    else:
        #display count timer - Ryaan Mohideen
        draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH/2, SCREEN_HEIGHT/3)
        #update count timer - Ryaan Mohideen
        if (pygame.time.get_ticks() - last_count_update) > 1000:
            intro_count -= 1 
            last_count_update = pygame.time.get_ticks()
    
    #update fighters - Ryan Rahman
    fighter_1.update()
    fighter_2.update()

    #draw fighter - Owen Gibbs
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #check for player defeat - Ryaan Mohideen
    if round_over == False:
        if fighter_1.alive == False:
            score[1]+=1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0]+=1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        #display victory image - Ryaan Mohideen
        draw_text("VICTORY!", count_font, RED, 360, 150)
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            fighter_1 = Fighter(1, 200, 310,False, GOKU_DATA, goku_sheet,GOKU_ANIMATION_STEPS)
            fighter_2 = Fighter(2, 700, 310,False, VEGETA_DATA, vegeta_sheet,VEGETA_ANIMATION_STEPS)
    #Event Handler - Ryan Rahman
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Update Display - Ryan Rahman
    pygame.display.update()
            

#exit pygame - Ryan Rahman

pygame.quit()
