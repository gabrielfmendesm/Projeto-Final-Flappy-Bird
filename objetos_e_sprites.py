from pygame import *
from random import *
from config import *
from assets import *
from jogo import window


# Classe que representa o jogador (bird)
class Bird: 
	def __init__(self, window):
		self.window = window
		self.lista = []

		for i in range(1,4):
			img = image.load(f'Assets/Bird/bird{i}.png')
			self.lista.append(img)
		
		self.reset()
		
	def update(self): # gravidade e movimento do jogador (bird)
		# gravidade
		self.velocidade += 0.3
		if self.velocidade >= 8:
			self.velocidade = 8
		if self.rect.bottom <= altura_tela:
			self.rect.y += int(self.velocidade)
		
		if self.vivo:
			# pulo
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
		
	def contador_asa(self):
		# animação do bird
		self.contador += 1
		if self.contador > 5:
			self.contador = 0
			self.frame += 1
		if self.frame >= 3:
			self.frame = 0
			
	def movimento_asa(self):
		self.contador_asa()
		if self.posicao_asa <= -10 or self.posicao_asa > 10:
			self.inclinacao_asa *= -1
		self.posicao_asa += self.inclinacao_asa
		self.rect.y += self.inclinacao_asa
		self.rect.x = WIDTH // 2 - 20
		self.image = self.lista[self.frame]
		self.window.blit(self.image, self.rect)
		
	def reset(self):
		self.frame = 0
		self.image = self.lista[self.frame]
		self.rect = self.image.get_rect()
		self.rect.x = 60
		self.rect.y = int(altura_tela) // 2
		self.contador = 0
		self.velocidade = 0
		self.pulo = False
		self.vivo = True
		self.angle = 0
		self.meio_tela = altura_tela // 2
		self.posicao_asa = 0
		self.inclinacao_asa = 1

# Classe que representa o placar (contador de pontos)
class Placar:

	# posições das imagens
	def __init__(self, x, y, window):
		self.lista_placar = []
		for placar in range(10):
			img = image.load(f'Assets/placar/{placar}.png')
			self.lista_placar.append(img)
			self.x = x
			self.y = y

		self.window = window
		
	# atualização do placar
	def update(self, placar):
		placar = str(placar)
		for frame, num in enumerate(placar):
			self.image = self.lista_placar[int(num)]
			self.rect = self.image.get_rect()
			self.rect.topleft = self.x - 15 * len(placar) + 30 * frame, self.y
			self.window.blit(self.image, self.rect)



# Variáveis dos objetos e sprites
grupo_canos = sprite.Group()
bird = Bird(window)


