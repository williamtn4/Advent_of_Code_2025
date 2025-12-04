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

def find_invalid(number,repeat_times):
	number = str(number)
	arr = [char for char in number]
	invalid = 0
	n = len(arr)

	if np.mod(n,2) == 1 and all(np.isin(arr,arr[0])):
		invalid = int(number)
	else:
		digit_factors = set()
		i = 1
		while i*i <= n:
			if n % i == 0:
				digit_factors.add(i)
				digit_factors.add(n // i)
			i += 1
		digit_factors = sorted(digit_factors)
		if repeat_times != None:
			digit_factors = [digit_factors[-repeat_times]]
		else:
			digit_factors = digit_factors[1:-1]
		N = len(digit_factors)
		
		for j in range(N):
			combined = [''.join(arr[i:i + digit_factors[j]]) for i in range(0,len(arr),digit_factors[j])]
			if all(np.isin(combined,combined[0])):
				invalid = int(number)
			else:
				exit
	return invalid

with open('input_d2.txt','r') as f:
	line = f.readline()
	ID_ranges = line.split(',')

invalid_list = []
for i,ID_range in enumerate(ID_ranges):
	start = int(ID_range.split('-')[0])
	stop = int(ID_range.split('-')[-1])
	for number in range(start,stop+1):
		invalid = find_invalid(number,2)
		if invalid != 0:
			invalid_list.append(invalid)

invalid_sum = np.sum(invalid_list)
print(invalid_sum)