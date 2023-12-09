from heapq import heappop, heappush

def solve_8_puzzle(initial_state):
    # Define the goal state
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # Define the Euclidean distance heuristic function
    def heuristic(state):
        distance = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] != 0:
                    row = (state[i][j] - 1) // 3
                    col = (state[i][j] - 1) % 3
                    target_row = i
                    target_col = j
                    distance += ((row - target_row) ** 2 + (col - target_col) ** 2) ** 0.5
        return distance

    # Define the A* algorithm
    def astar():
        open_set = []
        heappush(open_set, (heuristic(initial_state), 0, initial_state, []))
        closed_set = set()

        while open_set:
            _, cost, current_state, path = heappop(open_set)
            if current_state == goal_state:
                return path

            closed_set.add(tuple(map(tuple, current_state)))

            for move in get_possible_moves(current_state):
                new_state = apply_move(current_state, move)
                if tuple(map(tuple, new_state)) not in closed_set:
                    new_cost = cost + 1
                    new_path = path + [move]
                    heappush(open_set, (new_cost + heuristic(new_state), new_cost, new_state, new_path))

    # Helper functions (implement these functions)
    def get_possible_moves(state):
        # Returns a list of possible moves (up, down, left, right)
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    if i > 0:
                        possible_moves.append('up')
                    if i < 2:
                        possible_moves.append('down')
                    if j > 0:
                        possible_moves.append('left')
                    if j < 2:
                        possible_moves.append('right')
        return possible_moves

    def apply_move(state, move):
        # Applies the given move to the state and returns the new state
        new_state = [row[:] for row in state]
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    if move == 'up':
                        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
                    elif move == 'down':
                        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
                    elif move == 'left':
                        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
                    elif move == 'right':
                        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
        return new_state

    # Call the A* algorithm
    solution = astar()
    return solution

# Collect user input for the initial state
print("Enter the initial state of the 8-puzzle (3x3 grid) with numbers 0-8 (use space or newline as separators):")
initial_state = []
for _ in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)

# Call the solve_8_puzzle function with user input
solution = solve_8_puzzle(initial_state)
print("Solution Path:", solution)
