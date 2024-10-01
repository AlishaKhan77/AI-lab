# Write your code here :-)
class GreedyGraph(Graph):
    def greedy_best_first(self, start, goal, heuristic):
        open_set = []  # Nodes to explore
        heapq.heappush(open_set, (heuristic[start], Node(start)))  # Priority based on heuristic
        visited = set()  # Track visited nodes

        while open_set:  # While there are nodes to explore
            current = heapq.heappop(open_set)[1]  # Node with lowest heuristic

            if current == goal:
                return True  # Goal found

            visited.add(current.state)  # Mark current node as visited

            for next_node in current.generate_next_states():  # Generate next states
                if next_node.state not in visited:  # Visit unvisited states
                    heapq.heappush(open_set, (heuristic[next_node.state], next_node))  # Add to open set

        return False  # No path found
