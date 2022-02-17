import pygame
import random
import os

pygame.init()
pygame.mixer.init()

# Color
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

# Creating Window
screen_width = 900
screen_height = 600

# Window setup
game_window = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("MiliSnake")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

# Background Image
bgimg = pygame.image.load('images.jfif')
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plot_snake(color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])

def music_background():
    pygame.mixer.music.load('music_background.mp3')
    pygame.mixer.music.play()
def music_game_over():
    pygame.mixer.music.load('music_game_over.wav')
    pygame.mixer.music.play()


def game_loop():
    music_background()
    exit_game = False
    game_over = False
    snake_x = 400
    snake_y = 300
    snake_size = 20
    snk_list = []
    snk_length = 1
    init_velocity = 10
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(100,screen_width-100)
    food_y = random.randint(50,screen_height-50)
    fps = 30
    score = 0
    # Check if hiscore file exists
    if(not os.path.exists("hiscore.txt")):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))           
            game_window.fill(black)
            text_screen("Hi-Score = "+str(hiscore),white,250,100)
            text_screen("Your Score = "+str(score),white,500,100)
            text_screen("Game Over!",red,310,200)
            text_screen("Press Enter and Try again.",white,200,300)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
                
        else:             
            for event in pygame.event.get():                                
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        velocity_x = 0
                        velocity_y = -init_velocity

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        velocity_x = 0
                        velocity_y = init_velocity
                

            snake_x += velocity_x
            snake_y += velocity_y    
            
            game_window.fill(white)
            game_window.blit(bgimg, (0, 0))
            pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])

            # Just the initial start for the snake
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if abs(snake_x - food_x) < 15 and abs(snake_y - food_y) < 15:
                score += 1
                food_x = random.randint(100,screen_width-100)
                food_y = random.randint(50,screen_height-50)
                snk_length += 5
            
            if head in snk_list[:-1]:
                music_game_over() 
                game_over = True

            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                music_game_over() 
                game_over = True
            
            plot_snake(black,snk_list,snake_size)  
            
            text_screen("Score = "+ str(score),red,20,20)
         
        pygame.display.update()
        clock.tick(fps)
game_loop()
pygame.quit()
quit()