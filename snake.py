import pygame
import random
import time

pygame.init()


class block:
    blockwidth = 25
    blockheight = 25
    blocksize = 25
    wall = True
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


class snake2:
    leng = 4
    x = random.randint(1, block.blockwidth - 2)
    y = random.randint(1, block.blockheight - 2)
    dire = 5
    speed = 10
    tailx = []
    taily = []
    deaths = 0
    color = (0, 0, 100)
    head_color = (0, 0, 255)
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
        if snake2.leng == 4:
            snake.score -= 0.25
        else:
            snake.score -= 5

    def death2():
        snake2.leng = 4
        snake2.x = random.randint(1, block.blockwidth - 2)
        snake2.y = random.randint(1, block.blockheight - 2)
        snake2.dire = 5
        snake2.speed = 10
        snake2.tailx = []
        snake2.taily = []
        snake2.deaths += 1
        time.sleep(0.1)
        snake2.dire = 5
        if snake.leng == 4:
            snake2.score -= 0.25
        else:
            snake2.score -= 5
			
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

        for i in range(len(snake2.tailx)):
            color = snake2.color
            pygame.draw.rect(screen, color,
                             pygame.Rect(block.blocksize * snake2.tailx[i], block.blocksize * snake2.taily[i], block.blocksize, block.blocksize))
        color = snake2.head_color
        pygame.draw.rect(screen, color, pygame.Rect(block.blocksize * snake2.x, block.blocksize * snake2.y, block.blocksize, block.blocksize))

    def keyboard():
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            if (snake.dire != 2):
                snake.dire = 0
        if pressed[pygame.K_RIGHT]:
            if (snake.dire != 3):
                snake.dire = 1
        if pressed[pygame.K_DOWN]:
            if (snake.dire != 0):
                snake.dire = 2
        if pressed[pygame.K_LEFT]:
            if (snake.dire != 1):
                snake.dire = 3

        if pressed[pygame.K_w]:
            if (snake2.dire != 2):
                snake2.dire = 0
        if pressed[pygame.K_d]:
            if (snake2.dire != 3):
                snake2.dire = 1
        if pressed[pygame.K_s]:
            if (snake2.dire != 0):
                snake2.dire = 2
        if pressed[pygame.K_a]:
            if (snake2.dire != 1):
                snake2.dire = 3

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

    def ref2():
        game.tails2()
        if (snake2.dire == 0):
            game.move2(0, -1)
            # snake.y -=1
        elif (snake2.dire == 1):
            game.move2(1, 0)
            # snake.x+=1
        elif (snake2.dire == 2):
            # snake.y+=1
            game.move2(0, 1)
        elif (snake2.dire == 3):
            game.move2(-1, 0)
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
        game.crash(snake.x, snake.y, snake2.tailx, snake2.taily, 1)

    def move2(x, y):
        # x check
        if (snake2.x + x) >= block.blockwidth - 1:
            if (block.wall):
                snake2.x = 1
            else:
                game.death2()
            # print ("out of bounds")

        elif (snake2.x + x) <= 0:
            # print ("out of bounds")
            if (block.wall):
                snake2.x = block.blockwidth - 2
            else:
                game.death2()

        else:
            snake2.x += x
        # y check
        if (snake2.y + y) >= block.blockheight - 1:
            # print ("out of bounds")
            if (block.wall):
                snake2.y = 1
            else:
                game.death2()
        elif (snake2.y + y) <= 0:
            # print ("out of bounds")
            if (block.wall):
                snake2.y = block.blockheight - 2
            else:
                game.death2()

        else:
            snake2.y += y
        # bean
        if (snake2.x == bean.x) and (snake2.y == bean.y):
            snake2.leng += 1
            bean.lvl += 1
            bean.x = random.randint(1, block.blockwidth - 2)
            bean.y = random.randint(1, block.blockheight - 2)
            snake2.score += 10
            # print("bean pos:\nX - "+str(bean.x)+"\nY - "+str(bean.y))
        cdeaths = snake2.deaths
        for i in range(len(snake2.tailx)):
            if (snake2.deaths == cdeaths):
                if (snake2.x == snake2.tailx[i]):
                    if (snake2.y == snake2.taily[i]):
                        # print("game over")
                        game.death2()
        game.crash(snake2.x, snake2.y, snake.tailx, snake.taily, 2)

    def crash(x1, y1, x2, y2, key):
        for i in range(len(x2)):
            if x1 == x2[i] and y1 == y2[i]:
                if key == 1:
                    game.death()
                if key == 2:
                    game.death2()

    def tails():
        snake.tailx.append(snake.x)
        snake.taily.append(snake.y)
        if (len(snake.tailx) > snake.leng):
            snake.tailx.pop(0)
            snake.taily.pop(0)

    def tails2():
        snake2.tailx.append(snake2.x)
        snake2.taily.append(snake2.y)
        if (len(snake2.tailx) > snake2.leng):
            snake2.tailx.pop(0)
            snake2.taily.pop(0)


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
        game.ref2()
        c = 0
    pygame.display.set_caption(" P1 Score: " + str(snake.score) + " P2 Score: " + str(snake2.score))
    pygame.display.flip()
    clock.tick(100)

    if pygame.time.get_ticks() >= 60 * 1000:
        myfont = pygame.font.SysFont("test", 150)
        if snake.score > snake2.score:
            text = "P1 WIN "
        elif snake.score < snake2.score:
            text = "P2 WIN "
        else:
            text = "STANDOFF"
        test = myfont.render(text, 50, (255, 255, 255))
        screen.blit(test, (1, 1))
        pygame.display.flip()
        time.sleep(5)
        quit()


