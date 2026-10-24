
# 8 Puzzle using A* - Manhattan Distance

import heapq

start = "283164705"
goal = "123804765"


def heuristic(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != "0":
            current = i
            target = goal.index(tile)

            distance += abs(current // 3 - target // 3)
            distance += abs(current % 3 - target % 3)

    return distance


def astar():
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state in visited:
            continue
        visited.add(state)

        path = path + [state]

        if state == goal:
            print("Solution Found!")
            print("Moves:", g)
            for s in path:
                print(s[:3], s[3:6], s[6:])
                print()
            return

        zero = state.index("0")
        row, col = zero // 3, zero % 3

        moves = []
        if row > 0:
            moves.append(zero - 3)
        if row < 2:
            moves.append(zero + 3)
        if col > 0:
            moves.append(zero - 1)
        if col < 2:
            moves.append(zero + 1)

        for move in moves:
            new = list(state)
            new[zero], new[move] = new[move], new[zero]
            new = ''.join(new)

            if new not in visited:
                ng = g + 1
                nf = ng + heuristic(new)
                heapq.heappush(pq, (nf, ng, new, path))


astar()
