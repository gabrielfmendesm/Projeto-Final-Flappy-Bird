from pygame import *
from random import *
from config import *
from assets import *

class Bird: # personagem 
    def __init__(self, window):
        self.window = window
        self.lista = []

        for i in range(1,4):
            img = image.load(f'Assets/Bird/bird{i}.png')
            self.lista.append(img)
        self.reset()

	def update(self): # gravidade e movimento do bird

        # gravidade ------------------------------------
		self.velocidade += 0.3
		if self.velvocidade >= 8:
			self.velocidade = 8
		if self.rect.bottom <= altura_tela:
			self.rect.y += int(self.velocidade)

		if self.vivo:
		# pulo ------------------------------------------
			if mouse.get_pressed()[0] == 1 and not self.pulo:
				som_asa.play()
				self.pulo = True
				self.velocidade = -6
			if mouse.get_pressed()[0] == 0:
				self.pulo = False
			
			self.contador_asa()

			self.image = transform.rotate(self.lista[self.frame], self.velocidade * -2)

		else:

			if self.rect.bottom <= altura_tela:
				self.angle -= 2
			self.image = transform.rotate(self.lista[self.frame], self.angle)
		
		self.window.blit(self.image, self.rect)