import numpy as np

# --- Advent of Code ---
# This is a python file to run Advent of Code prompts with outputs displayed in the terminal

# --- Day 1 ---
with open('input_d1.txt', 'r') as f:
	lines = [line.split()[0] for line in f]

N = len(lines)

rotation_directions, dial_distance = np.zeros(N,dtype=str),np.zeros(N,dtype=int)

for i, word in enumerate(lines):
	value = word.split('\n')[0]
	rotation_directions[i] = value[0]
	if len(value) >= 2:
		dial_distance[i] = int(value[1::])
	else:
		dial_distance[i] = int(value[1])

def move_dial(initial_value,rotation_direction, adjust_value):
	if rotation_direction == 'L':
		pol = -1
	else:
		pol = 1

	new_value = np.mod(initial_value + pol*adjust_value, 100)

	if new_value < 0:
		new_value = 100 + new_value
		hit = 0
	elif new_value == 0:
		hit = 1
	else:
		hit = 0
	return new_value, hit

dial_value = 50
hit = np.zeros(N, dtype=int)
for i in range(N):
	dial_value, hit[i] = move_dial(dial_value,rotation_directions[i],dial_distance[i])
passcode = sum(hit)
# print("Passcode for secret entrance: {}".format(passcode))

# --- Day 2 ---
number = '138138138138'
print(number)
def find_invalid(number: str):
	n = len(number)
	arr = [char for char in number]
	invalid = 0
	
	digit_factors = set()
	i = 1
	while i*i <= n:
		if n % i == 0:
			digit_factors.add(i)
			digit_factors.add(n // i)
		i += 1
	digit_factors = list(digit_factors)
	print(digit_factors)
	max_char_len = max(digit_factors)
	digit_factors = digit_factors[1:-1]
	N = len(digit_factors)-1
	print(digit_factors)
	if np.mod(n,2) == 1 and all(np.isin(arr,arr[0])):
		invalid = int(number)
	else:
		new_arr = []
		for i in range(N):
			char = ''
			for j in range(n // ):

			new_arr.append()
			
	# elif np.mod(n,3) == 0:
	# 	while len(arr) > 2:
	# 		new_arr = []
	# 		for i in range(0,len(arr),3):

	# 		arr = [arr[i] + arr[i+1] + arr[i+2] for i in range(0,len(arr),3)]
	# 		if all(np.isin(arr,arr[0])):
	# 			invalid = int(number)
	# 		else:
	# 			pass
	# else:
	# 	while len(arr) > 2:
	# 		arr = [arr[i] + arr[i+1] for i in range(0,len(arr),2)]
	# 		if all(np.isin(arr,arr[0])):
	# 			invalid = int(number)
	# 		else:
				# pass
	return invalid

invalid = find_invalid(number)
print(invalid)