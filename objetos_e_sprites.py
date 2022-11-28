from pygame import *
from random import *

class Bird: # personagem 

    def init(self, window):
        self.window = window
        self.lista = []

        for i in range(1,4):
            img = image.load(f'Assets/Bird/bird{i}.png')
            self.lista.append(img)
        self.reset()