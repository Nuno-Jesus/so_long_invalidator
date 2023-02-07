import random
import os
from colorama import Style
from colorama import Fore

# COLOR MACROS
RESET = Style.RESET_ALL
LRED = Fore.LIGHTRED_EX
LYELLOW = Fore.LIGHTYELLOW_EX
LBLUE = Fore.LIGHTBLUE_EX
LGREEN = Fore.LIGHTGREEN_EX

# OTHER MACROS
GEN_PATH = "maps/generated"
WALL_PROBABILITY = 0.80
COIN_PROBABILITY = 0.80
HORIZONTAL = 0
VERTICAL = 1
DIRECTIONS = [HORIZONTAL, VERTICAL]

def generate_coins(contents, x, y) -> None:
	num_coins = random.randint(0, max(x, y) * COIN_PROBABILITY)
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

def flood_fill(contents, point, dims, prob):
	if contents[point[1]][point[0]] != '0' or \
		point[1] not in range(0, dims[1] - 1) or \
		point[0] not in range(0, dims[0] - 1):
		return
	
	n = random.randint(1, 100)
	if n in range(0, 100 - prob):
		contents[point[1]][point[0]] = '1'
		return
	flood_fill(contents, [point[0] - 1, point[1]], dims, int(prob * WALL_PROBABILITY))	#L
	flood_fill(contents, [point[0] + 1, point[1]], dims, int(prob * WALL_PROBABILITY)) 	#R
	flood_fill(contents, [point[0], point[1] - 1], dims, int(prob * WALL_PROBABILITY))	#U
	flood_fill(contents, [point[0], point[1] + 1], dims, int(prob * WALL_PROBABILITY))	#D

def generate_walls(contents, x, y):
	for line in contents[2::2]:
		px = random.randint(0, x - 1)
		width = random.randint(0, x - 1)
		
		#print(f'{line} -> x = {px} width = {width}')
		i = 0
		for i in range (0, x - 1):
			if line[i] == '0' and i in range(px, px + width):
				line[i] = '1'
			i += 1
	
	for i in range(0, x - 1, 3):
		py = random.randint(0, y - 1)
		width = random.randint(0, y - 1)
		
		#print(f'col -> y = {py} width = {width}')
		for k in range (0, y - 1):
			if contents[k][i] == '0' and k in range(py, py + width):
				contents[k][i] = '1'
	
	#flood_fill(contents, [px, py], [x, y], 100)


def generate_map(filename, x, y) -> None:
	contents = []

	contents.append(['1' for _ in range(0, x)] + ['\n'])
	for _ in range(0, y - 2):
		contents.append(['1'] + list((x - 2) * "0") + ['1', '\n'])
	contents.append(['1' for _ in range(0, x)] + ['\n'])

	generate_player_and_exit(contents, x, y)
	generate_coins(contents, x, y)
	generate_walls(contents, x, y)

	f = open(filename, "x")
	for line in contents:
		print("".join(line), end = '') 
		f.write("".join(line))
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
	