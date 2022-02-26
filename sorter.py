from typing import List
from box import Box
from config import *


class Sorter:
    def __init__(self, list_box: List[Box]):
        self.i = 0
        self.j = 0
        self.list_box = list_box

    def __next__(self):
        stop = COUNT_BOX - self.i - 1
        while True:
            if self.list_box[self.j].height > self.list_box[self.j + 1].height:
                self.list_box[self.j + 1].index = self.j
                self.list_box[self.j].index = self.j + 1
                self.list_box[self.j], self.list_box[self.j + 1] = (
                    self.list_box[self.j + 1],
                    self.list_box[self.j],
                )
                return self.j, self.j + 1

            self.j += 1
            if self.j >= stop:
                if self.i >= COUNT_BOX:
                    raise StopIteration
                self.i += 1
                stop = COUNT_BOX - self.i - 1
                self.j = 0


    def reset(self):
        self.i, self.j = 0, 0
        print("sorter resetlendi")
