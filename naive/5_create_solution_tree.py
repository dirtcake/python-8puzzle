import json
from queue import Queue

class State:
	def __init__(self, state):
		self.state = state
		self.distance = -1
		self.parent = None

	def __str__(self):
		return [self.state, self.parent, self.distance]



def create_tree(moves, solved_state):
	queue = Queue()
	queue.put(solved_state)
	tree = {}
	visited = []
	while not queue.empty():
		current = queue.get()
		print(queue.qsize())
		for state in moves[current]:
			if state not in visited:
				visited.append(state)
				tree[state] = current
				queue.put(state)


	# states = {}
	# for stateA in moves:
	# 	beginstate = State(stateA)
	# 	states[beginstate] = []
	# 	for stateB in moves[stateA]:
	# 		states[beginstate].append(State(stateB)) 


	# while not queue.empty():
	# 	current = queue.get()
	# 	print(queue.qsize())
	# 	for state in states[current]:
	# 		if state.distance == -1:
	# 			state.distance = current.distance + 1
	# 			state.parent = current
	# 			queue.put(state)
	# 			tree.append(state)

	return tree



with open('solvable_states.txt', 'r') as f:
	states_list = json.load(f)

with open('valid_moves_dict.txt', 'r') as f:
	moves = json.load(f)

tree = create_tree(moves, '12345678 ')
with open('solution_tree.txt', 'w') as f:
	json.dump(tree, f)