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

def generate_coins(contents, x, y) -> None:
	num_coins = random.randint(0, 15)
	print(f"Num coins: {num_coins}")

	for i in range(0, num_coins):
		cy = random.randint(1, y - 2)
		cx = random.randint(1, x - 2)
		
		if contents[cy][cx] == '0':
			contents[cy][cx] = 'C'

def generate_player_and_exit(contents, x, y) -> None:
	py = random.randint(1, y - 2)
	px = random.randint(1, x - 2)

	ey = random.randint(1, y - 2)
	ex = random.randint(1, x - 2)

	contents[py][px] = 'P'
	contents[ey][ex] = 'E'

def generate_walls(content, x, y):
	pass

def generate_map(filename, x, y) -> None:
	contents = []

	contents.append(['1' for _ in range(0, x)] + ['\n'])
	for _ in range(0, y - 2):
		contents.append(['1'] + list((y - 2) * "0") + ['1', '\n'])
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



def generate_file() -> str:
	n = 1
	
	while os.path.exists(f'{GEN_PATH}/map{n}.ber'):
		n += 1
	
	return (f'{GEN_PATH}/map{n}.ber')

if __name__ == "__main__" :
	x = -1
	y = -1

	while y < 3 or x < 3:
		try:
			x = int(input(f'Width: '))
			y = int(input(f'Height: '))
		except ValueError:
			print(f'\n\t===== {LRED}INPUT MUST BE BIGGER THAN 2{RESET} =====\n')

	random.seed()		
	generate_map(generate_file(), x, y)
	