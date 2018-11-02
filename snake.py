import pygame
import random
import time

pygame.init()


class vr:
    gw = 25
    gh = 25
    pxl = 25
    wl = True
    points = 0
    coloroffset = 5
    done = False


vr.sw = vr.gw * vr.pxl
vr.sh = vr.gh * vr.pxl
clock = pygame.time.Clock()
screen = pygame.display.set_mode((vr.sw, vr.sh))
c = 0


class apple:
    x = random.randint(1, vr.gw - 2)
    y = random.randint(1, vr.gh - 2)
    lvl = 0


class snake:
    leng = 4
    x = random.randint(1, vr.gw - 2)
    y = random.randint(1, vr.gh - 2)
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
    x = random.randint(1, vr.gw - 2)
    y = random.randint(1, vr.gh - 2)
    dire = 5
    speed = 10
    tailx = []
    taily = []
    deaths = 0
    color = (0, 0, 100)
    head_color = (0, 0, 255)
    score = 0


class gamef:
    def death():
        snake.leng = 4
        snake.x = random.randint(1, vr.gw - 2)
        snake.y = random.randint(1, vr.gh - 2)
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
        snake2.x = random.randint(1, vr.gw - 2)
        snake2.y = random.randint(1, vr.gh - 2)
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

    def grid():
        for x in range(int(vr.sw / vr.pxl)):
            for y in range(int(vr.sh / vr.pxl)):
                pygame.draw.rect(screen, (32, 32, 32), pygame.Rect(x * vr.pxl, y * vr.pxl, vr.pxl, vr.pxl))

    def draw():
        # Framerate of 10
        pygame.draw.rect(screen, (8, 8, 8), pygame.Rect(0, 0, vr.pxl, vr.sh))
        pygame.draw.rect(screen, (8, 8, 8), pygame.Rect(vr.sw - vr.pxl, 0, vr.pxl, vr.sh))
        pygame.draw.rect(screen, (8, 8, 8), pygame.Rect(0, 0, vr.sw, vr.pxl))
        pygame.draw.rect(screen, (8, 8, 8), pygame.Rect(0, vr.sh - vr.pxl, vr.sw, vr.pxl))
        color = (0, 255, 0)
        pygame.draw.rect(screen, color, pygame.Rect(vr.pxl * apple.x + 2, vr.pxl * apple.y + 2, vr.pxl - 4, vr.pxl - 4))
        pygame.draw.rect(screen, color, pygame.Rect(vr.pxl * apple.x + 2, vr.pxl * apple.y + 2, vr.pxl - 4, vr.pxl - 4))
        for i in range(len(snake.tailx)):
            color = snake.color
            pygame.draw.rect(screen, color,
                             pygame.Rect(vr.pxl * snake.tailx[i], vr.pxl * snake.taily[i], vr.pxl, vr.pxl))
        color = snake.head_color
        pygame.draw.rect(screen, color, pygame.Rect(vr.pxl * snake.x, vr.pxl * snake.y, vr.pxl, vr.pxl))

        for i in range(len(snake2.tailx)):
            color = snake2.color
            pygame.draw.rect(screen, color,
                             pygame.Rect(vr.pxl * snake2.tailx[i], vr.pxl * snake2.taily[i], vr.pxl, vr.pxl))
        color = snake2.head_color
        pygame.draw.rect(screen, color, pygame.Rect(vr.pxl * snake2.x, vr.pxl * snake2.y, vr.pxl, vr.pxl))

    def keyd():
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
        gamef.tails()
        if (snake.dire == 0):
            gamef.move(0, -1)
            # snake.y -=1
        elif (snake.dire == 1):
            gamef.move(1, 0)
            # snake.x+=1
        elif (snake.dire == 2):
            # snake.y+=1
            gamef.move(0, 1)
        elif (snake.dire == 3):
            gamef.move(-1, 0)
            # snake.x-=1

    def ref2():
        gamef.tails2()
        if (snake2.dire == 0):
            gamef.move2(0, -1)
            # snake.y -=1
        elif (snake2.dire == 1):
            gamef.move2(1, 0)
            # snake.x+=1
        elif (snake2.dire == 2):
            # snake.y+=1
            gamef.move2(0, 1)
        elif (snake2.dire == 3):
            gamef.move2(-1, 0)
            # snake.x-=1

    def move(x, y):
        # x check
        if (snake.x + x) >= vr.gw - 1:
            if (vr.wl):
                snake.x = 1
            else:
                gamef.death()
            # print ("out of bounds")

        elif (snake.x + x) <= 0:
            # print ("out of bounds")
            if (vr.wl):
                snake.x = vr.gw - 2
            else:
                gamef.death()

        else:
            snake.x += x
        # y check
        if (snake.y + y) >= vr.gh - 1:
            # print ("out of bounds")
            if (vr.wl):
                snake.y = 1
            else:
                gamef.death()
        elif (snake.y + y) <= 0:
            # print ("out of bounds")
            if (vr.wl):
                snake.y = vr.gh - 2
            else:
                gamef.death()

        else:
            snake.y += y
        # apple
        if (snake.x == apple.x) and (snake.y == apple.y):
            snake.leng += 1
            apple.lvl += 1
            snake.score += 10
            apple.x = random.randint(1, vr.gw - 2)
            apple.y = random.randint(1, vr.gh - 2)
            # print("Apple pos:\nX - "+str(apple.x)+"\nY - "+str(apple.y))
        cdeaths = snake.deaths;
        for i in range(len(snake.tailx)):
            if (snake.deaths == cdeaths):
                if (snake.x == snake.tailx[i]):
                    if (snake.y == snake.taily[i]):
                        # print("game over")
                        gamef.death()
        gamef.crash(snake.x, snake.y, snake2.tailx, snake2.taily, 1)

    def move2(x, y):
        # x check
        if (snake2.x + x) >= vr.gw - 1:
            if (vr.wl):
                snake2.x = 1
            else:
                gamef.death2()
            # print ("out of bounds")

        elif (snake2.x + x) <= 0:
            # print ("out of bounds")
            if (vr.wl):
                snake2.x = vr.gw - 2
            else:
                gamef.death2()

        else:
            snake2.x += x
        # y check
        if (snake2.y + y) >= vr.gh - 1:
            # print ("out of bounds")
            if (vr.wl):
                snake2.y = 1
            else:
                gamef.death2()
        elif (snake2.y + y) <= 0:
            # print ("out of bounds")
            if (vr.wl):
                snake2.y = vr.gh - 2
            else:
                gamef.death2()

        else:
            snake2.y += y
        # apple
        if (snake2.x == apple.x) and (snake2.y == apple.y):
            snake2.leng += 1
            apple.lvl += 1
            apple.x = random.randint(1, vr.gw - 2)
            apple.y = random.randint(1, vr.gh - 2)
            snake2.score += 10
            # print("Apple pos:\nX - "+str(apple.x)+"\nY - "+str(apple.y))
        cdeaths = snake2.deaths
        for i in range(len(snake2.tailx)):
            if (snake2.deaths == cdeaths):
                if (snake2.x == snake2.tailx[i]):
                    if (snake2.y == snake2.taily[i]):
                        # print("game over")
                        gamef.death2()
        gamef.crash(snake2.x, snake2.y, snake.tailx, snake.taily, 2)

    def crash(x1, y1, x2, y2, key):
        for i in range(len(x2)):
            if x1 == x2[i] and y1 == y2[i]:
                if key == 1:
                    gamef.death()
                if key == 2:
                    gamef.death2()

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


while not vr.done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            vr.done = True
            exit()
            quit()

    gamef.grid()
    gamef.keyd()
    c += 1
    gamef.draw()
    if (c >= (100 / snake.speed)):
        gamef.ref()
        gamef.ref2()
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


