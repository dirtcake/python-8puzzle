import json
import time

def get_valid_moves(stateA_index, stateB_start, class_size, spaceA, spaceB):
	valid = []
	stateA = states[stateA_index]
	for j in range(stateB_start, stateB_start+class_size):
		stateB = states[j]
		moved_pieceA = stateB[spaceA]
		moved_pieceB = stateA[spaceB]
		stateA_ = stateA.replace(' ', moved_pieceA)
		stateB_ = stateB.replace(' ', moved_pieceB)
		if stateA_ == stateB_ and spaceB in valid_space_moves[spaceA]:
			print('valid move at {}[{}] -> {}[{}]'.format(stateA, i, stateB, j))
			valid.append([stateA, stateB])
	return valid

with open('solvable_states.txt', 'r') as f:
	states = json.load(f)

valid_space_moves = {
	0: [1, 3],
	1: [0, 2, 4],
	2: [1, 5],
	3: [0, 4, 6],
	4: [1, 3, 5, 7],
	5: [2, 4, 8],
	6: [3, 7],
	7: [4, 6, 8],
	8: [5, 7]
}

start = time.clock()
valid_moves = []
class_size = 20160 # size of the 'space-is-in-same-position' equivalence class


# for i in range(0, 181440):
start = time.clock()
for i in range(0, 181440):
	stateA = states[i]
	if i >= 8*class_size: # space is at index 8, valid moves are to 5, 7
		valid_moves.extend(get_valid_moves(i, 5*class_size, class_size, 8, 5))
		valid_moves.extend(get_valid_moves(i, 7*class_size, class_size, 8, 7))
	elif i >= 7*class_size: # space is at index 7, valid moves are to 4, 6, 8
		valid_moves.extend(get_valid_moves(i, 4*class_size, class_size, 7, 4))
		valid_moves.extend(get_valid_moves(i, 6*class_size, class_size, 7, 6))
		valid_moves.extend(get_valid_moves(i, 8*class_size, class_size, 7, 8))
	elif i >= 6*class_size: # space is at index 6, valid moves are to 3, 7
		valid_moves.extend(get_valid_moves(i, 3*class_size, class_size, 6, 3))
		valid_moves.extend(get_valid_moves(i, 7*class_size, class_size, 6, 7))
	elif i >= 5*class_size: # space is at index 5, valid moves are to 2, 4, 8
		valid_moves.extend(get_valid_moves(i, 2*class_size, class_size, 5, 2))
		valid_moves.extend(get_valid_moves(i, 4*class_size, class_size, 5, 4))
		valid_moves.extend(get_valid_moves(i, 8*class_size, class_size, 5, 8))
	elif i >= 4*class_size: # space is at index 4, valid moves are to 1, 3, 5, 7
		valid_moves.extend(get_valid_moves(i, 1*class_size, class_size, 4, 1))
		valid_moves.extend(get_valid_moves(i, 3*class_size, class_size, 4, 3))
		valid_moves.extend(get_valid_moves(i, 5*class_size, class_size, 4, 5))
		valid_moves.extend(get_valid_moves(i, 7*class_size, class_size, 4, 7))
	elif i >= 3*class_size: # space is at index 3, valid moves are to 0, 4, 6
		valid_moves.extend(get_valid_moves(i, 0*class_size, class_size, 3, 0))
		valid_moves.extend(get_valid_moves(i, 4*class_size, class_size, 3, 4))
		valid_moves.extend(get_valid_moves(i, 6*class_size, class_size, 3, 6))
	elif i >= 2*class_size: # space is at index 2, valid moves are to 1, 5
		valid_moves.extend(get_valid_moves(i, 1*class_size, class_size, 2, 1))
		valid_moves.extend(get_valid_moves(i, 5*class_size, class_size, 2, 5))

	if i >= 1*class_size: # space is at index 1, valid moves are to 0, 2, 4		
		valid_moves.extend(get_valid_moves(i, 0*class_size, class_size, 1, 0))
		valid_moves.extend(get_valid_moves(i, 2*class_size, class_size, 1, 2))
		valid_moves.extend(get_valid_moves(i, 4*class_size, class_size, 1, 4))
	elif i >= 0: # space is at index 0, valid moves are to 1, 3
		valid_moves.extend(get_valid_moves(i, 1*class_size, class_size, 0, 1))
		valid_moves.extend(get_valid_moves(i, 3*class_size, class_size, 0, 3))
	


print(time.clock()-start)
print(len(valid_moves))
with open('valid_moves.txt', 'w') as f:
	json.dump(valid_moves, f)