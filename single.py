import pygame
import random
import time

pygame.init()


class block:
    blockwidth = 25
    blockheight = 25
    blocksize = 25
    wall = False
    points = 0
    coloroffset = 5
    done = False

block.screenwidth = block.blockwidth * block.blocksize
block.screenheight = block.blockheight * block.blocksize
clock = pygame.time.Clock()
screen = pygame.display.set_mode((block.screenwidth, block.screenheight))
c = 0

class bean:
    x = random.randint(1, block.blockwidth - 2)
    y = random.randint(1, block.blockheight - 2)
    lvl = 0

class snake:
    leng = 4
    x = random.randint(1, block.blockwidth - 2)
    y = random.randint(1, block.blockheight - 2)
    dire = 5
    speed = 10
    tailx = []
    taily = []
    deaths = 0
    color = (100, 0, 0)
    head_color = (255, 0, 0)
    score = 0


class game:
    def death():
        snake.leng = 4
        snake.x = random.randint(1, block.blockwidth - 2)
        snake.y = random.randint(1, block.blockheight - 2)
        snake.dire = 5
        snake.speed = 10
        snake.tailx = []
        snake.taily = []
        snake.deaths += 1
        time.sleep(0.1)
        snake.dire = 5


    def square():
        for x in range(int(block.screenwidth / block.blocksize)):
            for y in range(int(block.screenheight / block.blocksize)):
                pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(x * block.blocksize, y * block.blocksize, block.blocksize, block.blocksize))
				

    def draw():
        # Framerate of 10
        pygame.draw.rect(screen, (8, 8, 8), pygame.Rect(0, 0, block.blocksize, block.screenheight))
        pygame.draw.rect(screen, (8, 8, 8), pygame.Rect(block.screenwidth - block.blocksize, 0, block.blocksize, block.screenheight))
        pygame.draw.rect(screen, (8, 8, 8), pygame.Rect(0, 0, block.screenwidth, block.blocksize))
        pygame.draw.rect(screen, (8, 8, 8), pygame.Rect(0, block.screenheight - block.blocksize, block.screenwidth, block.blocksize))
        color = (0, 255, 0)
        pygame.draw.rect(screen, color, pygame.Rect(block.blocksize * bean.x + 2, block.blocksize * bean.y + 2, block.blocksize - 4, block.blocksize - 4))
        pygame.draw.rect(screen, color, pygame.Rect(block.blocksize * bean.x + 2, block.blocksize * bean.y + 2, block.blocksize - 4, block.blocksize - 4))
        for i in range(len(snake.tailx)):
            color = snake.color
            pygame.draw.rect(screen, color,
                             pygame.Rect(block.blocksize * snake.tailx[i], block.blocksize * snake.taily[i], block.blocksize, block.blocksize))
        color = snake.head_color
        pygame.draw.rect(screen, color, pygame.Rect(block.blocksize * snake.x, block.blocksize * snake.y, block.blocksize, block.blocksize))
		
    def keyboard():
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            if (snake.dire != 2):
                snake.dire = 0
        if pressed[pygame.K_d]:
            if (snake.dire != 3):
                snake.dire = 1
        if pressed[pygame.K_s]:
            if (snake.dire != 0):
                snake.dire = 2
        if pressed[pygame.K_a]:
            if (snake.dire != 1):
                snake.dire = 3

    def ref():
        game.tails()
        if (snake.dire == 0):
            game.move(0, -1)
            # snake.y -=1
        elif (snake.dire == 1):
            game.move(1, 0)
            # snake.x+=1
        elif (snake.dire == 2):
            # snake.y+=1
            game.move(0, 1)
        elif (snake.dire == 3):
            game.move(-1, 0)
            # snake.x-=1
			
    def move(x, y):
        # x check
        if (snake.x + x) >= block.blockwidth - 1:
            if (block.wall):
                snake.x = 1
            else:
                game.death()
            # print ("out of bounds")

        elif (snake.x + x) <= 0:
            # print ("out of bounds")
            if (block.wall):
                snake.x = block.blockwidth - 2
            else:
                game.death()

        else:
            snake.x += x
        # y check
        if (snake.y + y) >= block.blockheight - 1:
            # print ("out of bounds")
            if (block.wall):
                snake.y = 1
            else:
                game.death()
        elif (snake.y + y) <= 0:
            # print ("out of bounds")
            if (block.wall):
                snake.y = block.blockheight - 2
            else:
                game.death()

        else:
            snake.y += y
        # bean
        if (snake.x == bean.x) and (snake.y == bean.y):
            snake.leng += 1
            bean.lvl += 1
            snake.score += 10
            bean.x = random.randint(1, block.blockwidth - 2)
            bean.y = random.randint(1, block.blockheight - 2)
            # print("bean pos:\nX - "+str(bean.x)+"\nY - "+str(bean.y))
        cdeaths = snake.deaths;
        for i in range(len(snake.tailx)):
            if (snake.deaths == cdeaths):
                if (snake.x == snake.tailx[i]):
                    if (snake.y == snake.taily[i]):
                        # print("game over")
                        game.death()
		
    def tails():
        snake.tailx.append(snake.x)
        snake.taily.append(snake.y)
        if (len(snake.tailx) > snake.leng):
            snake.tailx.pop(0)
            snake.taily.pop(0)
        
        
while not block.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            block.done = True
            exit()
            quit()

    game.square()
    game.keyboard()
    c += 1
    game.draw()
    if (c >= (100 / snake.speed)):
        game.ref()
        c = 0
    if not(snake.dire  == 5):
        pygame.display.set_caption("Snake!!!|Score: "+str(snake.leng-4))
    pygame.display.flip()
    clock.tick(100)