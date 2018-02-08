import json
import random
import time

def check_digits(state):
	return len(state) == 9 and len(set(state)) == len(state)

def is_solvable(state):
	pass

count = 0

def add_digit_to_state(states, partial_state, digit=''):
	global count
	partial_state += digit
	if len(partial_state) == 9:
		states.append(partial_state)
	else:
		for s in '12345678 ':
			count += 1
			if s not in partial_state:
				add_digit_to_state(states, partial_state, s)

def create_states():
	states = []
	add_digit_to_state(states, '')
	return states

start = time.clock()
states = create_states()
print('generated {} in {} after checking {} states'.format(len(states), time.clock() - start, str(count)))

states_sorted_nested = [[], [], [], [], [], [], [], [], []]

for state in states:
	states_sorted_nested[state.index(' ')].append(state)

states_sorted = []
for group in states_sorted_nested:
	states_sorted.extend(group)

with open('states.txt', 'w') as f:
	json.dump(states_sorted, f)