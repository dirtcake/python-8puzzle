import json

with open('valid_moves.txt', 'r') as f:
	moves = json.load(f)

reformatted = {}

count = 0
for move in moves:
	count += 1
	print(str(count))
	initial = move[0]
	if initial in reformatted:
		reformatted[initial].append(move[1])
	else:
		reformatted[initial] = [move[1]]

with open('valid_moves_dict.txt', 'w') as f:
	json.dump(reformatted, f)

