import pygame

class Escena:
	def __init__(self, director):
		self.director=director

	def update(self, *args):
		raise NotImplemented("Tiene que implementar el metodo update.")
	
	def eventos(self, *args):
		raise NotImplemented("Tiene que implementar el metodo eventos.")
	
	def dibujar(self, win):
		raise NotImplemented("Tiene que implementar el metodo dibujar.")