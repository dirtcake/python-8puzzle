import json
import time

def move_space_to_br(state):
	if state.index(' ') == 0:
		return state[8] + state[7] + state[6] + state[5] + state[4] + state[3] + state[2] + state[1] + state[0]
	elif state.index(' ') == 1:
		return state[7] + state[6] + state[3] + state[8] + state[4] + state[0] + state[5] + state[2] + state[1]
	elif state.index(' ') == 2:
		return state[6] + state[3] + state[0] + state[7] + state[4] + state[1] + state[8] + state[5] + state[2]
	elif state.index(' ') == 3:
		return state[5] + state[8] + state[7] + state[2] + state[4] + state[6] + state[1] + state[0] + state[3]
	elif state.index(' ') == 4:
		return state[0] + state[1] + state[2] + state[3] + state[7] + state[5] + state[6] + state[8] + state[4]
	elif state.index(' ') == 5:
		return state[3] + state[0] + state[1] + state[6] + state[4] + state[2] + state[7] + state[8] + state[5]
	elif state.index(' ') == 6:
		return state[2] + state[5] + state[8] + state[1] + state[4] + state[7] + state[0] + state[3] + state[6]
	elif state.index(' ') == 7:
		return state[1] + state[2] + state[5] + state[0] + state[4] + state[8] + state[3] + state[6] + state[7]

def swap(state, posA, posB):
	swapped = ''
	for i, s in enumerate(state):
		if i == posA:
			swapped += state[posB]
		elif i == posB:
			swapped += state[posA]
		else:
			swapped += state[i]
	return swapped

def is_solvable(state):
	swaps = 0
	pos = state.index(' ')
	if pos != 8:
		state = move_space_to_br(state)
	for i in range(0,8):
		if state[i] != str(i+1):
			state = swap(state, i, state.index(str(i+1)))
			swaps += 1

	return swaps % 2 == 0

with open('states.txt', 'r') as f:
	states = json.load(f)


solvable = []
count = 0

start = time.clock()
for state in states:
	if is_solvable(state):
		count += 1
		print(state + ' is ' + str(count))
		solvable.append(state)
print(time.clock()-start)
# with open('solvable_states.txt', 'w') as f:
	# json.dump(solvable, f)
	
print(str(count))