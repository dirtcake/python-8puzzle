import json
import time
import sys

def solve(state):
	solution = []
	next_move = state
	while next_move != '12345678 ':
		next_move = tree[next_move]
		solution.append(next_move)
	return solution

with open('solution_tree.txt') as f:
	tree = json.load(f)

with open('solvable_states.txt') as f:
	states = json.load(f)


sol = solve(sys.argv[1])
print(sol)
print(len(sol))

