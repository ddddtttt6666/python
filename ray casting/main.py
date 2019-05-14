import math
import os 
import random
import time
import sys

os.system("cls");

# -- main code --

TERMINAL_SIZE = os.get_terminal_size();
screenWidth = TERMINAL_SIZE[0]
screenHeight = TERMINAL_SIZE[1]

def brightChars(val=0):
	lvs = [' ', '.', '-', '=', '*', '?', '#', '%', '@']
	return lvs[int(val*8)]

def printMiniMap(Map):
	for i in range(len(Map)):
		textToPrint = ''
		for j in range(len(Map[i])):
			if Map[i][j] == 1:
				textToPrint += '[]'
			else:
				textToPrint += '  '
		print(textToPrint);


class Player():
	def __init__(self, MapSize):
		self.posx = int(MapSize/2)
		self.posy = int(MapSize/2)
		self.dir = 0

	def look(self, Map, Total):
		Distances = [0 for i in range(Total)];

		maxDistanceToTravel = len(Map)

		angle = -(3.1415926535897932378/4)+self.dir
		for i in range(Total):

			px = self.posx
			py = self.posy
			sx = math.cos(angle)*0.1
			sy = math.sin(angle)*0.1

			distanceTraveled = 0
			while distanceTraveled < maxDistanceToTravel:
				px += sx
				py += sy

				if Map[int(px)][int(py)] == 1:
					break;

				distanceTraveled = math.sqrt((px-self.posx)**2+(py-self.posy)**2);

			Distances[i] = max(distanceTraveled, 1)
			angle += (3.1415926535897932378/2)/Total

		return Distances

	def render(self, Map):
		MapSize = len(Map)
		Dists = self.look(Map, screenWidth);
		bufer = [[" " for i in range(screenHeight)] for j in range(screenWidth)]
		
		for i in range(len(bufer)):
			for j in range(len(bufer[i])):
				if 1/Dists[i]*(screenHeight/2) > abs(-j+(screenHeight/2)):
					bufer[i][j] = brightChars(1/(Dists[i]**2))

		toPrint = ''
		for i in range(len(bufer[0])):
			SubToPrint = ''
			for j in range(len(bufer)):
				SubToPrint += bufer[j][i]
			toPrint += '\n'+SubToPrint

		sys.stdout.write(toPrint);
		# print(toPrint);
		return True

def main():
	MapSize = 160

	Map = [[0 for i in range(MapSize)] for j in range(MapSize)];

	player = Player(MapSize);

	for i in range(MapSize):
		for j in range(MapSize):
			if random.uniform(0, 1) < 0.3 or i == 0 or j == 0 or i == MapSize-1 or j == MapSize-1:
				Map[i][j] = 1;

	MainFrameCounter = 0
	while True:
		# os.system("cls");

		player.render(Map);
		player.posy+=0.05

		#printMiniMap(Map);

		time.sleep(0.02);
		MainFrameCounter += 1
		if MainFrameCounter > 1000:
			break



# -- -- 
main()