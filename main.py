import pygame as pg
from box import Box
from sorter import Sorter
from config import *
import random


class Game:
    def __init__(self):
        pg.init()
        self.surface = pg.display.set_mode([WIDTH, HEIGHT])
        self.is_running = True
        self.list_box = [
            Box(random.randint(HEIGHT_MIN, HEIGHT_MAX), i) for i in range(COUNT_BOX)
        ]
        self.clock = pg.time.Clock()
        self.sorter = Sorter(self.list_box)

        self.is_sorting = False

    def main(self):
        while self.is_running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.is_running = False

                if event.type == pg.KEYDOWN:

                    if event.key == pg.K_ESCAPE:
                        self.is_running = False

                    if event.key == pg.K_b:
                        self.is_sorting = True

                    if event.key == pg.K_r:
                        self.reset()
                        self.mix()
            self.surface.fill((255, 255, 255))
            i, j = None, None
            if self.is_sorting:
                try:
                    i, j = next(self.sorter)
                except StopIteration:
                    self.reset()
                    print("bitti")

            if i and j:
                self.list_box[i].set_color(0, 255, 0)
                self.list_box[j].set_color(0, 0, 255)

            self.draw()

            if i and j:
                self.list_box[i].reset_color()
                self.list_box[j].reset_color()

            pg.display.flip()
            self.clock.tick()
            pg.display.set_caption(f"FPS => {self.clock.get_fps()}")

    def draw(self):
        for box in self.list_box:
            box.draw(self.surface)

    def mix(self):
        for box in self.list_box:
            box.height = random.randint(HEIGHT_MIN, HEIGHT_MAX)
        print("yukseklikler degistirildi")

    def reset(self):
        self.is_sorting = False
        self.sorter.reset()


if __name__ == "__main__":
    Game().main()
