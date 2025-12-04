import numpy as np

# --- Day 1 ---
with open('test.txt', 'r') as f:
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
	hit = 0
	if rotation_direction == 'L':
		pol = -1
	else:
		pol = 1

	new_value = initial_value + pol*adjust_value
	full_rot = int(new_value/100)
	remainder = np.mod(new_value)
	print(new_value,full_rot)
	if full_rot != 0 and new_value != 0:
		hit += abs(full_rot)
		new_value = np.mod(new_value, 100)
	elif full_rot != 0 and 
	


	if new_value < 0:
		new_value = 100 + new_value
		hit += 1
	elif new_value == 0:
		hit += 1
	else:
		pass
	print(hit)
	return new_value, hit

dial_value = 50
hit = np.zeros(N, dtype=int)
for i in range(N):
	dial_value, hit[i] = move_dial(dial_value,rotation_directions[i],dial_distance[i])
passcode = sum(hit)
print("Passcode for secret entrance: {}".format(passcode))