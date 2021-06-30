import pygame
import random

pygame.init()
#colors
white = (255,255,255) 
red = (255,0,0)
black = (0,0,0) 

#game window

screen_width = 900
screen_height = 600

gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snakes with prashant")
pygame.display.update()

#Game specific variables
exit_game = False
game_over = False

snake_x = 45
snake_y = 55
snake_size = 10
fps = 65

food_x = random.randint(20, (screen_width/2))
food_y = random.randint(20, (screen_height/2))
score = 0
init_velocity = 5
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55, bold=True, italic=False)

def screen_score(text, color, x, y):
    screen_score = pygame.font.render(text, True, color)
    gameWindow.blit(screen_score, [[x,y]])


velocity_x = 0
velocity_y = 0



#game loop

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = init_velocity
                velocity_y = 0
            if event.key == pygame.K_UP:
                velocity_y = -init_velocity  
                velocity_x = 0 
            if event.key == pygame.K_DOWN:
                velocity_y =  init_velocity 
                velocity_x = 0 
            if event.key == pygame.K_LEFT:
                velocity_x = -init_velocity
                velocity_y = 0     

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
        score += 1
        print("Score: ", score*10)
        food_x = random.randint(20, (screen_width/2))
        food_y = random.randint(20, (screen_height/2))    
    

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

        

pygame.quit()
quit()    