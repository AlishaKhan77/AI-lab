# Write your code here :-)
import heapq

class AStarGraph(Graph):
    def a_star(self, start, goal, heuristic):
        open_set = []  # Nodes to explore
        heapq.heappush(open_set, (0, Node(start)))  # Priority queue
        came_from = {}  # Track paths
        g_score = {node: float('inf') for node in self.graph}  # Cost from start
        g_score[start] = 0  # Cost to start node is 0
        f_score = {node: float('inf') for node in self.graph}  # Total cost
        f_score[start] = heuristic[start]  # Initial heuristic cost

        while open_set:  # While there are nodes to explore
            current = heapq.heappop(open_set)[1]  # Node with lowest f_score

            if current == goal:
                return True  # Goal found

            for neighbor in self.graph.get(current, []):  # Check neighbors
                tentative_g_score = g_score[current] + 1  # Assuming cost is 1
                if tentative_g_score < g_score[neighbor]:  # Shorter path found
                    came_from[neighbor] = current  # Track path
                    g_score[neighbor] = tentative_g_score  # Update cost
                    f_score[neighbor] = tentative_g_score + heuristic[neighbor]  # Update total cost
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))  # Add to open set

        return False  # No path found
