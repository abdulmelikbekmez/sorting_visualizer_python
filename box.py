import pygame as pg
from config import *


class Box:
    def __init__(self, height: int, index: int) -> None:
        self.height = height
        self.color = (255, 0, 0)
        self.index = index

    def draw(self, surface: pg.surface.Surface):
        width = (WIDTH - (MARGIN_LEFT + MARGIN_RIGHT)) / COUNT_BOX
        top = MARGIN_TOP + HEIGHT_MAX - self.height
        left = MARGIN_LEFT + self.index * width
        pg.draw.rect(surface, self.color, pg.Rect(left, top, width, self.height))

    def reset_color(self):
        self.color = (255, 0, 0)

    def set_color(self, r: int, g: int, b: int):
        self.color = (r, g, b)
