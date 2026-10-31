
# 8 Queens using Simulated Annealing

import random
import math

N = 8


# Calculate attacking pairs
def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):

            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


# Generate a random neighbour
def neighbour(state):
    new_state = state.copy()

    col = random.randint(0, N - 1)
    row = random.randint(0, N - 1)

    while row == state[col]:
        row = random.randint(0, N - 1)

    new_state[col] = row

    return new_state


# Display chessboard
def display(state):
    for r in range(N):
        for c in range(N):
            if state[c] == r:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Simulated Annealing
def simulated_annealing():

    current = [random.randint(0, 7) for i in range(N)]
    best = current.copy()

    T = 100
    cooling_rate = 0.995
    iteration = 0

    print("INITIAL STATE")
    print("State:", current)
    print("Initial Cost:", cost(current))
    display(current)

    while T > 0.1:

        iteration += 1

        current_cost = cost(current)

        if current_cost == 0:
            break

        next_state = neighbour(current)
        next_cost = cost(next_state)

        delta = current_cost - next_cost

        print("\n--------------------------------")
        print("Iteration:", iteration)
        print("Temperature:", round(T, 3))
        print("Current Cost:", current_cost)
        print("Neighbour:", next_state)
        print("Neighbour Cost:", next_cost)
        print("Delta E:", delta)

        # Acceptance probability
        if delta > 0:
            probability = 1
            current = next_state
            print("Decision: BETTER STATE ACCEPTED")

        else:
            probability = math.exp(delta / T)

            print("Acceptance Probability:",
                  round(probability, 4))

            if random.random() < probability:
                current = next_state
                print("Decision: WORSE/EQUAL STATE ACCEPTED")
            else:
                print("Decision: STATE REJECTED")

        # Update best state
        if cost(current) < cost(best):
            best = current.copy()

        print("Current State:", current)
        print("Current Cost:", cost(current))

        # Stop if solution found
        if cost(current) == 0:
            break

        # Decrease temperature
        T = T * cooling_rate

    print("\n================================")
    print("SIMULATED ANNEALING RESULT")
    print("================================")

    if cost(current) == 0:
        best = current.copy()
        print("SOLUTION FOUND!")
    elif cost(best) == 0:
        print("SOLUTION FOUND!")
    else:
        print("Temperature reached minimum.")
        print("Best solution obtained.")

    print("Final State:", best)
    print("Final Cost:", cost(best))
    print("\nFINAL CHESSBOARD")
    display(best)


simulated_annealing()
