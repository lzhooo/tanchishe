import pygame
def loop(self):
    clock = pygame.time.Clock()
    while self.stat != 'quit':
        elapse = clock.tick(25)
        if self.stat == 'menu':
            self.stat = self.menu.run(elapse)
        elif self.stat == 'game':
            self.stat = self.main.run(elapse)

        if self.stat.startswith('level'):
            level = int(self.stat.split()[1])
            print("Start game at level", level)
            self.main.start(level)
            self.stat = "game"

        pygame.display.update()
    pygame.quit()