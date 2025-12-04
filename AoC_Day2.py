import numpy as np

# --- Day 2 ---

def find_invalid(number,repeat_times):
	number = str(number)
	arr = [char for char in number]
	invalid = 0
	n = len(arr)

	if all(np.isin(arr,arr[0])):
		if len(arr) == repeat_times:
			invalid == int(number)
		elif repeat_times == None:
			invalid = int(number)
		else:
			pass
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

with open('input_d2p12.txt','r') as f:
	line = f.readline()
	ID_ranges = line.split(',')

invalid_list = []
for i,ID_range in enumerate(ID_ranges):
	start = int(ID_range.split('-')[0])
	stop = int(ID_range.split('-')[-1])
	for number in range(start,stop+1):
		invalid = find_invalid(number,None)
		if invalid != 0:
			invalid_list.append(invalid)

invalid_sum = np.sum(invalid_list)
print(invalid_sum)