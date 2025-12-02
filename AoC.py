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
print("Passcode for secret entrance: {}".format(passcode))

# --- Day 2 ---
