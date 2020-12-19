import sys, time
from GameOfLife_project.model import *
from GameOfLife_project.view import *

class Life:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Life') #название окна

        self.screen = pygame.display.set_mode((610, 610)) #создаем окно
        self.u=0   #

        self.model = Model()  #создаем объект model


        self.view = View(self.screen)     #
        self.view.draw_grid()             # сетка
        self.view.draw_cells(self.model)  #

    def input(self, events):
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.view.y0 -= 1
            self.view.draw_cells(self.model)
            time.sleep(0.1)
        elif pygame.key.get_pressed()[pygame.K_DOWN]:
            self.view.y0 += 1
            self.view.draw_cells(self.model)
            time.sleep(0.1)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            self.view.x0 -= 1
            self.view.draw_cells(self.model)
            time.sleep(0.1)
        elif pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.view.x0 += 1
            self.view.draw_cells(self.model)
            time.sleep(0.1)

        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if(self.u)==0:
                          self.u=1
                else:
                  self.u = 0


            elif event.type == pygame.MOUSEBUTTONUP and event.button in [1, 3]:
                x, y = event.pos
                x = x // self.view.length + self.view.x0
                y = y // self.view.length + self.view.y0
                if event.button == 1:
                    self.model.insert_cell((x, y))
                else:
                    self.model.delete_cell((x, y))
                self.view.draw_cells(self.model)

    def action(self):
        while 1:
            pygame.time.delay(100)
            if (self.u==1):
                self.model = self.model.next_g()
                self.view.draw_cells(self.model)
            self.input(pygame.event.get())
            self.view.draw()


def main():
    life = Life()
    life.action()

if __name__ == '__main__': main()
