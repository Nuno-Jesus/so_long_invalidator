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
WALL = '1'
PLAYER = 'P'
COIN = 'C'
EXIT = 'E'
EMPTY = '0'

def generate_coins(contents, x, y) -> None:
	num_coins = random.randint(0, math.floor((max(x, y) * COIN_PROBABILITY)))
	print(f"Num coins: {num_coins}")

	for i in range(0, num_coins):
		cx, cy = random.randint(1, x - 2), random.randint(1, y - 2)
		
		if contents[cy][cx] == EMPTY:
			contents[cy][cx] = COIN

def generate_player_and_exit(contents, x, y) -> None:
	px, py = random.randint(1, x - 2), random.randint(1, y - 2)

	#print(f"Player (X/Y): {[px, py]}")
	ex, ey = random.randint(1, x - 2), random.randint(1, y - 2)

	#print(f"Exit (X/Y): {[ex, ey]}")
	contents[py][px] = 'P'
	contents[ey][ex] = 'E'

def get_random_unvisited_node(visited, x, y):

	unvisited_nodes = []

	if not visited[y - 1][x]:
		unvisited_nodes.append([x, y - 1])
	if not visited[y + 1][x]:
		unvisited_nodes.append([x, y + 1])
	if not visited[y][x - 1]:
		unvisited_nodes.append([x - 1, y])
	if not visited[y][x + 1]:
		unvisited_nodes.append([x + 1, y])
	if len(unvisited_nodes) < 2:
		return None
	return unvisited_nodes[random.randint(0, len(unvisited_nodes) - 1)]

def randomized_dfs(contents, x, y, visited):
	visited[y][x] = True
	contents[y][x] = EMPTY
	pos = get_random_unvisited_node(visited, x, y)

	while pos != None:
		randomized_dfs(contents, pos[0], pos[1], visited)
		pos = get_random_unvisited_node(visited, x, y)
		
def generate_walls(contents, x, y):
	visited = []
	visited.append([True for _ in range (0, x)])
	for _ in range (0, y - 2):
		visited.append([True] + [False for _ in range(0, x - 2)] + [True])
	visited.append([True for _ in range (0, x)])

	# print(visited)
	start_x, start_y = random.randint(1, x - 2), random.randint(1, y - 2)
	randomized_dfs(contents, start_x, start_y, visited)

	
def generate_map(filename, x, y) -> None:
	contents = [[WALL for _ in range(0, x)] for _ in range(0, y)]

	generate_walls(contents, x, y)
	generate_coins(contents, x, y)
	generate_player_and_exit(contents, x, y)

	f = open(filename, "x")
	for line in contents:
		for char in line:
			if char is WALL:
				print(f'{LBLUE}{char}{RESET}', end = "")
			elif char is COIN:
				print(f'{LYELLOW}{char}{RESET}', end = "")
			elif char is EXIT:
				print(f'{LGREEN}{char}{RESET}', end = "")
			elif char is PLAYER:
				print(f'{LRED}{char}{RESET}', end = "")
			else:
				print(char, end = "")
		print()
	print(f'\n\t --- The map was saved in {LRED}{filename}{RESET}. ---\n')

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
	