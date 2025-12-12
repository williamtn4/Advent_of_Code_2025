import numpy as np

#--- Day 3 ---

def find_joltage(input):
	batt_bank = np.array([int(char) for char in input])
	N = len(batt_bank)
	batt_bank_sorted = np.sort(batt_bank)
	sorted_key = sorted(range(N), key=lambda k: batt_bank[k])
	
	# Get unique values in array and see if the max value of the array repeats twice
	unique_batt, unique_key, counts = np.unique(batt_bank_sorted, return_index=True, return_counts=True)

	if counts[-1] > 1:
		joltage = unique_batt[-1]*11
		return joltage

	# Case 1: Largest is before second largest
	new_bank = []
	for i in range(N):
		if sorted_key[-1] < sorted_key[i] and batt_bank_sorted[-1] > batt_bank_sorted[i]:
			new_bank.append(batt_bank_sorted[i])

	if not new_bank:
		pass
	else:
		tens_batt = batt_bank_sorted[-1]
		single_batt = new_bank[-1]
		joltage = tens_batt*10 + single_batt
		return joltage
	
	# Case 2: Largest is after second largest
	new_bank = []
	joltage = unique_batt[-2]*10 + unique_batt[-1]
	return joltage


with open('input_d3.txt','r') as f:
	lines = f.readlines()
	batt_bank_list = []
	for line in lines:
		batt_bank_list.append(line.split('\n')[0])

max_joltage = 0
for batt_bank in batt_bank_list:
	joltage = find_joltage(batt_bank)
	print(joltage)
	max_joltage += joltage
print(max_joltage)