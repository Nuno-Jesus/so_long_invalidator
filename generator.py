import random
import math
import os
from colorama import Style
from colorama import Fore

#! Colors
RESET = Style.RESET_ALL
LRED = Fore.LIGHTRED_EX
LYELLOW = Fore.LIGHTYELLOW_EX
LBLUE = Fore.LIGHTBLUE_EX
LGREEN = Fore.LIGHTGREEN_EX

#! Other macros
GEN_PATH = "maps/generated"
WALL_PROBABILITY = 0.80
COIN_PROBABILITY = 0.80

#! Entities
WALL = "1"
PLAYER = "P"
COIN = "C"
EXIT = "E"
EMPTY = "0"

def generate_coins(contents, x, y) -> None:
	num_coins = random.randint(0, math.floor((max(x, y) * COIN_PROBABILITY)))
	print(f"Num coins: {num_coins}")

	for i in range(0, num_coins):
		cy = random.randint(1, y - 2)
		cx = random.randint(1, x - 2)
		
		#print(f"Coin (X/Y): {[cx, cy]}")
		if contents[cy][cx] == '0':
			contents[cy][cx] = 'C'

def generate_player_and_exit(contents, x, y) -> None:
	py = random.randint(1, y - 2)
	px = random.randint(1, x - 2)

	print(f"Player (X/Y): {[px, py]}")
	ey = random.randint(1, y - 2)
	ex = random.randint(1, x - 2)

	print(f"Exit (X/Y): {[ex, ey]}")
	contents[py][px] = 'P'
	contents[ey][ex] = 'E'

def get_random_unvisited_node(visited, x, y):

	unvisited_nodes = []

	if not visited[y - 1][x]:
		unvisited_nodes.append([y - 1, x])
	if not visited[y + 1][x]:
		unvisited_nodes.append([y + 1, x])
	if not visited[y][x - 1]:
		unvisited_nodes.append([y, x - 1])
	if not visited[y][x + 1]:
		unvisited_nodes.append([y, x + 1])
	if len(unvisited_nodes) < 2:
		return None
	return unvisited_nodes[random.randint(0, len(unvisited_nodes) - 1)]

def randomized_dfs(contents, x, y, visited):
	visited[y][x] = True
	contents[y][x] = EMPTY
	pos = get_random_unvisited_node(visited, x, y)

	while pos != None:
		randomized_dfs(contents, pos[1], pos[0], visited)
		pos = get_random_unvisited_node(visited, x, y)
		

def generate_walls(contents, x, y):
	visited = []
	visited.append([True for _ in range (0, x)])
	for _ in range (0, y - 2):
		visited.append([True] + [False for _ in range(0, x - 2)] + [True])
	visited.append([True for _ in range (0, x)])

	# print(visited)
	start_x, start_y = random.randint(1, x - 1), random.randint(1, y - 1)
	randomized_dfs(contents, start_x, start_y, visited)

	
def generate_map(filename, x, y) -> None:
	contents = [[WALL for _ in range(0, x)] for _ in range(0, y)]

	generate_player_and_exit(contents, x, y)
	generate_coins(contents, x, y)
	generate_walls(contents, x, y)

	f = open(filename, "x")
	for line in contents:
		print("".join(line), end = '\n') 
		f.write("".join(line) + '\n')
	f.close()
	print(f'The map was saved in {LRED}{filename}{RESET}.')

if __name__ == "__main__" :
	n = 1
	x, y = -1, -1

	while y < 3 or x < 3:
		try:
			x = int(input(f'Width: '))
			y = int(input(f'Height: '))
		except ValueError:
			print(f'\n\t===== {LRED}INPUT MUST BE BIGGER THAN 2{RESET} =====\n')
	
	while os.path.exists(f'{GEN_PATH}/map{n}.ber'):
		n += 1
	
	random.seed()
	generate_map(f'{GEN_PATH}/map{n}.ber', x, y)
	