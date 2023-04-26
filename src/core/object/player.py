import pygame as pg



class Player:
	def __init__(self):
		self.image = [
			pg.image.load('assets/player/idle.png').convert_alpha(),
			pg.image.load('assets/player/walk-0.png').convert_alpha(),
			pg.image.load('assets/player/walk-1.png').convert_alpha(),
			pg.image.load('assets/player/walk-2.png').convert_alpha()]

		self.anim = []

		self.pos = [0, 0]
		self.vel = [0, 0]


	def update(self):
		self.physics()


	def render(self, frame):
		frame.blit(self.animate(), self.pos)


	def animate(self):
		currentImage = self.image[0]

		return currentImage


	def physics(self):
		pass