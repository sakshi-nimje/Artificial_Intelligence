import heapq

# Define the graph as an adjacency list
graph = {
    'S': {'A': 1, 'G': 12},
    'A': {'S': 1, 'C': 1, 'B': 3},
    'B': {'A': 3, 'D': 3},
    'C': {'A': 1, 'D': 1, 'G': 2},
    'D': {'B': 3, 'C': 1, 'G':3},
    'G': {'S': 12, 'D': 3, 'C': 2},
}

# Input heuristic values (h(n)) for each node
heuristics = {}
for node in graph.keys():
    heuristic_value = int(input(f"Enter heuristic value (h(n)) for node {node}: "))
    heuristics[node] = heuristic_value

# A* algorithm
def astar(graph, start, goal, heuristics):
    open_list = [(0, start)]
    g_scores = {node: float('inf') for node in graph}
    g_scores[start] = 0
    came_from = {}

    while open_list:
        current_g, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.insert(0, current_node)
                current_node = came_from[current_node]
            path.insert(0, start)
            return path, g_scores[goal]

        for neighbor, cost in graph[current_node].items():
            tentative_g = g_scores[current_node] + cost
            if tentative_g < g_scores[neighbor]:
                came_from[neighbor] = current_node
                g_scores[neighbor] = tentative_g
                f_score = tentative_g + heuristics[neighbor]
                heapq.heappush(open_list, (f_score, neighbor))

    return None, None

start_node = input("Enter the start node (A-H): ").upper()
goal_node = input("Enter the goal node (A-H): ").upper()

if start_node in graph and goal_node in graph:
    path, total_cost = astar(graph, start_node, goal_node, heuristics)
    if path:
        print("Shortest path:", " -> ".join(path))
        print("Total cost:", total_cost)
    else:
        print("No path found.")
else:
    print("Invalid node names. Please use alphabetic nodes (A-H).")
