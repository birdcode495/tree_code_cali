import pygame

class Personaje():

	def __init__(self, x, y):

		self.shape = pygame.Rect(0, 0, 50, 50)
		self.shape.center = (x, y)

	def draw(self, interface):

		pygame.draw.rect(interface, (255, 255, 0), self.shape)

