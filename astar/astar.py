from heapq import heappush, heappop
import time
import sys

def is_solvable(state):
    """determines whether the solved state is reachable from the given initial state"""
    swaps = 0
    pos = state.index('0')
    if pos != 8:  # move space to correct position
        if state.index('0') == 0:
            state = state[8] + state[7] + state[6] + state[5] + state[4] + state[3] + state[2] + state[1] + state[0]
        elif state.index('0') == 1:
            state = state[7] + state[6] + state[3] + state[8] + state[4] + state[0] + state[5] + state[2] + state[1]
        elif state.index('0') == 2:
            state = state[6] + state[3] + state[0] + state[7] + state[4] + state[1] + state[8] + state[5] + state[2]
        elif state.index('0') == 3:
            state = state[5] + state[8] + state[7] + state[2] + state[4] + state[6] + state[1] + state[0] + state[3]
        elif state.index('0') == 4:
            state = state[0] + state[1] + state[2] + state[3] + state[7] + state[5] + state[6] + state[8] + state[4]
        elif state.index('0') == 5:
            state = state[3] + state[0] + state[1] + state[6] + state[4] + state[2] + state[7] + state[8] + state[5]
        elif state.index('0') == 6:
            state = state[2] + state[5] + state[8] + state[1] + state[4] + state[7] + state[0] + state[3] + state[6]
        elif state.index('0') == 7:
            state = state[1] + state[2] + state[5] + state[0] + state[4] + state[8] + state[3] + state[6] + state[7]

    for i in range(0,8): # then swap tiles until we have the solved state, an even number of swaps implies the initial state is solvable
        if state[i] != str(i+1):
            state = _swap(state, i, state.index(str(i+1)))
            swaps += 1

    return swaps % 2 == 0


def _swap(state, posA, posB):
    l = list(state)
    l[posA], l[posB] = l[posB], l[posA]
    return ''.join(l)

def expand(valid_space_moves, state):
    """returns a list of valid moves from the given state"""

    moves = []
    index = state.index('0')
    for position in valid_space_moves[index]:
        moves.append(_swap(state, index, position))
    return moves

def solve(state, h):
    #if not is_solvable(state):
#        return []

    q = []
    heappush(q, (h(state), state, 0))
    parent = {}
    visited = set()
    current = (0,(), 0)

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

    while len(q) > 0 and current[1] != '123456780':
        current = heappop(q)
        for move in expand(valid_space_moves, current[1]):
            if move not in visited:
                visited.add(current[1])
                parent[move] = current
                heappush(q, (h(move) + current[2]+1, move, current[2]+1))

    print('visits: ', len(visited))

    key = '123456780'
    solution = []
    while key in parent and key != state:
        solution.append(''.join(key))
        key = parent[key][1]

    solution.append(state)
    solution.reverse()

    return solution


def manhattan(state):
    return (2 - state.index('0') % 3) + (2 - state.index('0') // 3)

def total_manhattan(state):
    distances = []
    distances.append(abs((0 - state.index('1')%3)) + (0 - state.index('1')//3))
    distances.append(abs((1 - state.index('2')%3)) + (0 - state.index('2')//3))
    distances.append(abs((2 - state.index('3')%3)) + (0 - state.index('3')//3))
    distances.append(abs((0 - state.index('4')%3)) + (1 - state.index('4')//3))
    distances.append(abs((1 - state.index('5')%3)) + (1 - state.index('5')//3))
    distances.append(abs((2 - state.index('6')%3)) + (1 - state.index('6')//3))
    distances.append(abs((0 - state.index('7')%3)) + (2 - state.index('7')//3))
    distances.append(abs((1 - state.index('8')%3)) + (2 - state.index('8')//3))
    distances.append(abs((2 - state.index('0')%3)) + (2 - state.index('0')//3))
    return sum(distances)

solution = solve(sys.argv[1], h=manhattan)
# solution = solve('647850321', h=manhattan)
print(solution)
print(len(solution)-1)



# state = '647850321'  31
# state = '703258614'  21
# state = '481630275'  17
# state = '862347501'  29
