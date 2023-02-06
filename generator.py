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
ENTITIES = "01C"
GEN_PATH = "maps/generated"

def generate_entity() -> str:
	n = random.randint(1, 100)

	if n in range(1, 70):
		return '0'
	elif n in range(71, 95):
		return '1'
	else:
		return 'C'


def generate_map(filename, x, y) -> None:
	contents = []

	contents.append(['1' for _ in range(0, x)] + ['\n'])
	for _ in range(0, y - 2):
		contents.append(['1'] + [generate_entity() for _ in range(0, x - 2)] + ['1', '\n'])
	contents.append(['1' for _ in range(0, x)] + ['\n'])

	py = random.randint(1, y - 2)
	px = random.randint(1, x - 2)

	ey = random.randint(1, y - 2)
	ex = random.randint(1, x - 2)

	contents[py][px] = 'P'
	contents[ey][ex] = 'E'

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

	while y < 0 or x < 0:
		try:
			x = int(input(f'Width: '))
			y = int(input(f'Height: '))
		except ValueError:
			print(f'\n\t===== {LRED}INPUT MUST BE BIGGER THAN 3{RESET} =====\n')

	random.seed()		
	generate_map(generate_file(), x, y)
	