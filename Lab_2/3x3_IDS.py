# 8 Puzzle using IDS

start = "102453786"
goal = "123456780"

path = []


def dls(state, depth, visited):

    if state == goal:
        path.append(state)
        return True

    if depth == 0:
        return False

    visited.add(state)

    zero = state.index("0")
    row = zero // 3
    col = zero % 3

    moves = []

    # Possible moves of blank
    if row < 2:
        moves.append(zero + 3)  
    if row > 0:
        moves.append(zero - 3)  
    if col > 0:
        moves.append(zero - 1)  
    if col < 2:
        moves.append(zero + 1)     

    for move in moves:

        new_state = list(state)

        new_state[zero], new_state[move] = \
            new_state[move], new_state[zero]

        new_state = ''.join(new_state)

        if new_state not in visited:

            if dls(new_state, depth - 1, visited):
                path.append(state)
                return True

    return False


def ids():

    depth = 0

    while True:

        print("Searching at depth:", depth)

        visited = set()

        if dls(start, depth, visited):
            return depth

        depth += 1


depth = ids()

path.reverse()

print("\nSolution Found!")
print("Solution Depth:", depth)
print("Number of moves:", len(path) - 1)
print()

for i, state in enumerate(path):

    print("Step", i)

    for j in range(0, 9, 3):
        print(state[j], state[j + 1], state[j + 2])

    print()
