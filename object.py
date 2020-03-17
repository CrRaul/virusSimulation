
import numpy as np

class object():
	def __init__(self, x,y):
		self.__position = np.array([x,y], dtype='float64')
		self.__velocity = np.array([0,0], dtype='float64')
		self.__acceleration = np.array([0,0], dtype='float64')
		self.__infected = False

	def setPosition(self,position):
		self.__position = position
	def setVelocity(self,velocity):
		self.__velocity = velocity
	def setAcceleration(self,acceleration):
		self.__acceleration = acceleration
	def setInfected(self,ok):
		self.__infected = ok

	def getPosition(self):
		return self.__position
	def getVelocity(self):
		return self.__velocity
	def getAcceleration(self):
		return self.__acceleration
	def getInfected(self):
		return self.__infected

	def flipHorizontal(self):
		self.__velocity[0] = (-1) * self.__velocity[0] 
	def flipVertical(self):
		self.__velocity[1] = (-1) * self.__velocity[1]


	def update(self):
		self.__velocity += self.__acceleration
		self.__position += self.__velocity
		self.__acceleration *= 0
