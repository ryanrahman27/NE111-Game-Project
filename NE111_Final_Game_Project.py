import pygame

pygame.init()

#Creating Game Window

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("DBZ Fighter")

#Load Background
bg_image = pygame.image.load("bg_image - instasize.jpg").convert_alpha()

#Function to Draw Background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH,SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0,0))


#Game Loop
run = True
while run:

    #Draw Background
    draw_bg()


    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Update Display
    pygame.display.update()
            

#exit pygame

pygame.quit()
