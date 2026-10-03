# 8 Puzzle using DFS

start = "123450786"
goal = "123456708"

visited = set()
path = []


def dfs(state):

    if state == goal:
        path.append(state)
        return True

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

            if dfs(new_state):
                path.append(state)
                return True

    return False


if dfs(start):

    path.reverse()

    print("Solution Found!")
    print("Number of moves:", len(path) - 1)
    print()

    for i, state in enumerate(path):

        print("Step", i)

        for j in range(0, 9, 3):
            print(state[j], state[j + 1], state[j + 2])

        print()

else:
    print("No solution found")
