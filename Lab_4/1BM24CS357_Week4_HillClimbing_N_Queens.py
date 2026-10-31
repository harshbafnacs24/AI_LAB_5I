
# Hill Climbing for 4-Queens Problem

from itertools import combinations

# Initial state
state = [3, 1, 2, 0]


# Calculate number of attacking pairs
def cost(s):
    count = 0

    for i, j in combinations(range(4), 2):
        if s[i] == s[j] or abs(s[i] - s[j]) == abs(i - j):
            count += 1

    return count


# Display chessboard
def display(s):
    for r in range(4):
        for c in range(4):
            if s[c] == r:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


# Hill Climbing algorithm
def hill_climbing(state):

    while True:

        current_cost = cost(state)

        print("Current State:", state)
        print("Current Cost:", current_cost)
        display(state)

        if current_cost == 0:
            print("Goal Reached!")
            return

        best_state = state.copy()
        best_cost = current_cost
        best_pair = None

        print("Neighbour States:")

        # Generate all possible swaps
        for i, j in combinations(range(4), 2):

            new_state = state.copy()
            new_state[i], new_state[j] = new_state[j], new_state[i]

            new_cost = cost(new_state)

            print((i, j), new_state, "Cost:", new_cost)

            # Select lowest-cost neighbour
            # First pair wins in case of a tie
            if new_cost < best_cost:
                best_cost = new_cost
                best_state = new_state
                best_pair = (i, j)

        if best_state == state:
            print("No better neighbour found!")
            return

        print("Selected Swap:", best_pair)
        print("Next State:", best_state)
        print("------------------------")

        state = best_state


hill_climbing(state)
