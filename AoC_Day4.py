import numpy as np

#--- Day 4 ---
def get_roll(idx,idy,array):
	if array[idx,idy] == '.':
		return 0
	else:
		return 1
	
def check_roll_remove(idx,idy,array):
	# array is a 2D array
	# check for the 8 elements around it

	n_rows = len(array)
	n_columns = len(array[0,:])
	
	if not get_roll(idx,idy,array):
		return 0
	else:
		if idx == 0 or idx == n_rows-1:
			# Check for corners
			if idy == 0 or idy == n_columns-1:
				return 1
			# Check first row
			elif idx == 0:
				roll_sum = 0
				for i in [0,1]:
					for j in [-1,0,1]:
						roll_sum += get_roll(idx+i,idy+j,array)
				roll_sum -= 1
				if roll_sum >= 4:
					return 0
				else:
					return 1
			# Check last row
			else:
				roll_sum = 0
				for i in [-1,0]:
					for j in [1,0,-1]:
						roll_sum += get_roll(idx+i,idy+j,array)
				roll_sum -= 1
				if roll_sum >= 4:
					return 0
				else:
					return 1
		elif idy == 0 or idy == n_columns-1:
			# Check first column
			if idy == 0:
				roll_sum = 0
				for i in [-1,0,1]:
					for j in [0,1]:
						roll_sum += get_roll(idx+i,idy+j,array)
				roll_sum -= 1
				if roll_sum >= 4:
					return 0
				else:
					return 1
			# Check last column
			else:
				roll_sum = 0
				for i in [-1,0,1]:
					for j in [-1,0]:
						roll_sum += get_roll(idx+i,idy+j,array)
				roll_sum -= 1
				if roll_sum >= 4:
					return 0
				else:
					return 1
		else:
			# General case
			roll_sum = 0
			for i in [-1,0,1]:
				for j in [-1,0,1]:
					roll_sum += get_roll(idx+i,idy+j,array)
			roll_sum -= 1
			if roll_sum >= 4:
				return 0
			else:
				return 1

def new_roll_mod(array,idx,idy,roll_removal):
	new_roll_array = array
	if roll_removal:
		new_roll_array[idx][idy] = '.'
	return new_roll_array

with open('input_d4.txt','r') as f:
	lines = f.readlines()
	roll_array = []
	for line in lines:
		roll_array.append(line.split('\n')[0])	

roll_array = np.array(roll_array) 
roll_array = np.array([list(row) for row in roll_array])
print(roll_array)
nrow = len(roll_array)
ncolumn = len(roll_array[0])
print(nrow,ncolumn)

# roll_total = 0
# for i in range(nrow):
# 	for j in range(ncolumn):
# 		roll_check = check_roll_remove(i,j,roll_array)
# 		roll_total += roll_check
# print("Removed ",roll_total," rolls")

roll_total = 1
new_roll_array = np.array([[roll_array[i,j] for j in range(ncolumn)] for i in range(nrow)])
rolls_removed = 0
while roll_total != 0:
	roll_total = 0
	for i in range(nrow):
		for j in range(ncolumn):
			roll_check = check_roll_remove(i,j,roll_array)
			roll_total += roll_check
			if roll_check == 1:
				new_roll_array[i,j] = '.'
	roll_array = np.array([[new_roll_array[i,j] for j in range(ncolumn)] for i in range(nrow)])
	print("Removed ",roll_total," rolls")
	rolls_removed += roll_total
print("Total rolls removed ",rolls_removed)