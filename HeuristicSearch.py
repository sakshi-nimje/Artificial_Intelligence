# Define a class to represent a node in the search space
class Node:
    def __init__(self, state, heuristic=0, parent=None):
        self.state = state  # The current state of the node
        self.heuristic = heuristic  # The heuristic estimate of remaining cost
        self.parent = parent  # The parent node

# Define the Greedy Best-First Search algorithm function
def greedy_best_first_search(graph, start_node, goal_node, heuristic_func):
    open_set = []  # Priority queue for open nodes
    closed_set = set()  # Set to keep track of closed nodes

    start_node = Node(start_node, heuristic=heuristic_func(start_node, goal_node))
    open_set.append(start_node)

    while open_set:
        open_set.sort(key=lambda node: node.heuristic)
        current_node = open_set.pop(0)

        if current_node.state == goal_node:
            return current_node

        closed_set.add(current_node.state)

        for neighbor_state in graph[current_node.state]:
            if neighbor_state not in closed_set:
                neighbor_node = Node(neighbor_state, heuristic=heuristic_func(neighbor_state, goal_node), parent=current_node)
                open_set.append(neighbor_node)

    return None  # Goal state not found

# Define a heuristic function (example: Euclidean distance in one dimension)
def euclidean_distance_heuristic(state, goal_state):
    return abs(ord(state) - ord(goal_state))

# Define the graph (example: one-dimensional graph with edge costs)
graph = {
   """ 'P': {'A': 4, 'C': 4, 'R':4},
    'A': {'P': 4, 'M': 3},
    'C': {'R': 2, 'M': 6, 'U': 3, 'P':4},
    'R': {'P': 4, 'E': 5, 'C': 2},
    'M': {'U': 5, 'A': 3, 'L': 2, 'C': 6},
    'U': {'E': 5, 'C': 3, 'S': 4, 'M': 5, 'N': 5},
    'E': {'U': 5, 'R': 5, 'S': 1},
    'L': {'N': 5, 'M': 2},
    'N': {'L': 5, 'S': 6, 'U': 5},
    'S': {'E': 1, 'N': 6, 'U': 4},
    """
    'S': {'B': 1, 'A': 4},
    'A': {'C': 1, 'D': 2},
    'B': {'F': 3, 'E': 2},
    'F': {'G2': 1, 'I': 2},
    'E': {'H': 4, 'G1': 3},
    'C': {'H': 4},
    'D': {'A': 2},
    'H': {'E': 4},
    'G1': {'E': 3},
    'F': {'I': 2},
    'G2': {'F': 1},
}

# Set the start and goal nodes
start_node = 'S'
goal_node = 'G2'

# Perform Greedy Best-First Search
goal_node = greedy_best_first_search(graph, start_node, goal_node, euclidean_distance_heuristic)

if goal_node:
    # Reconstruct the path and calculate the cost of each edge
    path = []
    current_node = goal_node
    total_cost = 0
    while current_node:
        path.insert(0, current_node.state)
        if current_node.parent:
            total_cost += graph[current_node.parent.state][current_node.state]
        current_node = current_node.parent
    print(f"Path found from {start_node} to {goal_node.state} with a total cost of {total_cost}:")
    for i in range(len(path) - 1):
        print(f"Edge: {path[i]} -> {path[i + 1]} with cost {graph[path[i]][path[i + 1]]}")
else:
    print(f"No path found from {start_node} to {goal_node}.")
