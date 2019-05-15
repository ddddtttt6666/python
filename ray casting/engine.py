import os
import sys
import time
import random

os.system('cls');

def cos(a):
	return 

class Buffer():
	def __init__(self):
		self.W = os.get_terminal_size()[0]
		self.H = os.get_terminal_size()[1]
		self.bufer = [[' ' for i in range(self.W)] for j in range(self.H)]

	def brightness(self, val):
		vals = [9617, 9618, 9619, 9608]
		return chr(vals[int((val-0.001)*len(vals))]);

	def randx(self):
		return random.randint(0, self.W-1)

	def randy(self):
		return random.randint(0, self.H-1)

	def background(self, val):
		for i in range(self.H):
			for j in range(self.W):
				self.bufer[i][j] = val

	def line(self, x0,y0, x1,y1, val):
		x0 = int(x0)
		y0 = int(y0)
		x1 = int(x1)
		y1 = int(y1)
		if abs(y1 - y0) < abs(x1 - x0):
			if x0 > x1:
				self.plotLineLow(x1, y1, x0, y0, val)
			else:
				self.plotLineLow(x0, y0, x1, y1, val)
		else:
			if y0 > y1:
				self.plotLineHigh(x1, y1, x0, y0, val)
			else:
				self.plotLineHigh(x0, y0, x1, y1, val)
	def plotLineHigh(self, x0,y0, x1,y1, val):
		dx = x1 - x0
		dy = y1 - y0
		xi = 1
		if dx < 0:
			xi = -1
			dx = -dx
		D = 2*dx - dy
		x = x0

		for y in range(y0, y1):
			self.set(x,y, val)
			if D > 0:
				x = x + xi
				D = D - 2*dy
			D = D + 2*dx
	def plotLineLow(self, x0,y0, x1,y1, val):
		dx = x1 - x0
		dy = y1 - y0
		yi = 1
		if dy < 0:
		  yi = -1
		  dy = -dy
		D = 2*dy - dx
		y = y0

		for x in range(x0, x1):
			self.set(x,y, val)
			if D > 0:
				y = y + yi
				D = D - 2*dx
			D = D + 2*dy

	def set(self, x, y, val):
		x = int(x)
		y = int(y)
		self.bufer[min(max(y, 0), self.H-1)][min(max(x, 0), self.W-1)] = val

	def render(self):
		toPrint = ''
		for i in range(self.H-1):
			for j in range(self.W-1):
				# sys.stdout.write(self.bufer[i][j]);
				toPrint += self.bufer[i][j]
			toPrint+='\n'
		# os.system('cls');
		# sys.stdout.flush();
		sys.stdout.write(toPrint);