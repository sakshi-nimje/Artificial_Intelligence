from collections import deque

# Function to represent the state of the jugs as a tuple (x, y)
# where x is the amount of water in the first jug, and y is the amount in the second jug.
def state_tuple(x, y):
    return (x, y)

# Function to perform BFS to find a solution to the Water Jug problem.
def water_jug_bfs(capacity_x, capacity_y, target):
    visited = set()  # To keep track of visited states
    queue = deque()  # Queue for BFS
    initial_state = state_tuple(0, 0)
    queue.append(initial_state)
    path = {}  # To store the path to reach each state

    while queue:
        current_state = queue.popleft()
        x, y = current_state

        if x == target or y == target:
            # Found a solution, reconstruct the path
            solution_path = []
            while current_state != initial_state:
                solution_path.append(current_state)
                current_state = path[current_state]
            solution_path.append(initial_state)
            solution_path.reverse()
            return solution_path

        # Generate possible next states and add them to the queue
        next_states = []

        # Fill the first jug
        next_states.append(state_tuple(capacity_x, y))
        
        # Fill the second jug
        next_states.append(state_tuple(x, capacity_y))
        
        # Empty the first jug
        next_states.append(state_tuple(0, y))
        
        # Empty the second jug
        next_states.append(state_tuple(x, 0))
        
        # Pour from the first jug into the second jug
        pour = min(x, capacity_y - y)
        next_states.append(state_tuple(x - pour, y + pour))
        
        # Pour from the second jug into the first jug
        pour = min(y, capacity_x - x)
        next_states.append(state_tuple(x + pour, y - pour))

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
                path[state] = current_state

    return None  # No solution found

# Take user input for jug capacities and target amount
capacity_x = int(input("Enter the capacity of the first jug: "))
capacity_y = int(input("Enter the capacity of the second jug: "))
target = int(input("Enter the target amount of water to measure: "))

solution_path = water_jug_bfs(capacity_x, capacity_y, target)

if solution_path:
    print("Solution Path:")
    for state in solution_path:
        print(f"({state[0]}, {state[1]})")
else:
    print("Solution path is not found.")
