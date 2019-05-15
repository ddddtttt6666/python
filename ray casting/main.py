import math
import os 
import random
import time
import sys
import engine

os.system("cls");

# -- main code --

TERMINAL_SIZE = os.get_terminal_size();
screenWidth = TERMINAL_SIZE[0]
screenHeight = TERMINAL_SIZE[1]

def brightChars(val=0):
	lvs = [' ', '.', '-', '=', '*', '|', '?', '#', '%', '8', '@']
	return lvs[int(val*8)]

def printMiniMap(Map, bufer, playerPos, playerDir):
	for i in range(len(Map)):
		for j in range(len(Map[i])):
			if Map[i][j] == 1:
				bufer.set(i*2, j, '[');
				bufer.set(i*2+1, j, ']');
			else:
				bufer.set(i*2, j, ' ');
				bufer.set(i*2+1, j, ' ');
	bufer.set(int(playerPos[0]*2), int(playerPos[1]), "@");
	# bufer.set(int(playerPos[0]*2)+1, int(playerPos[1]), ">");
	bufer.set(int(math.cos(playerDir)*2)+int(playerPos[0]*2), int(math.sin(playerDir)*2)+int(playerPos[1]), "+");

class Player():
	def __init__(self, MapSize):
		self.posx = int(1)
		self.posy = int(1)
		self.dir = 1

	def look(self, Map, Total):
		Distances = [0 for i in range(Total)];

		maxDistanceToTravel = 160

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
		buf = engine.Buffer();
		
		for i in range(screenWidth):
			buf.line(i, int(screenHeight/2-(screenHeight/3*(1/Dists[i]))), i, int(screenHeight/2+(screenHeight/3*(1/Dists[i]))), buf.brightness(1/(Dists[i])));
		printMiniMap(Map, buf, [self.posx, self.posy], self.dir)
		buf.render();
		return True

def main():
	MapSize = 16

	Map = [[0 for i in range(MapSize)] for j in range(MapSize)];

	player = Player(MapSize);

	for i in range(MapSize):
		for j in range(MapSize):
			if random.uniform(0, 1) < 0.1 or i == 0 or j == 0 or i == MapSize-1 or j == MapSize-1:
				Map[i][j] = 1;

	MainFrameCounter = 0
	while True:
		# os.system("cls");

		player.render(Map);
		player.posy+=0.01
		player.posx+=0.01
		player.dir += 0.02

		#printMiniMap(Map);

		time.sleep(0.02);
		MainFrameCounter += 1
		if MainFrameCounter > 10000:
			break



# -- -- 
main()