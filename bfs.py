from collections import deque

class Graph:
    def bfs(self, start):
        visited = set()  # Track visited nodes
        queue = deque([start])  # Initialize queue with the start node
        visited.add(start)  # Mark the start node as visited

        while queue:  # While there are nodes to process
            vertex = queue.popleft()  # Dequeue the next node
            print(vertex, end=' ')  # Process the current node

            for neighbor in self.graph.get(vertex, []):  # Check neighbors
                if neighbor not in visited:  # Visit unvisited neighbors
                    visited.add(neighbor)  # Mark as visited
                    queue.append(neighbor)  # Enqueue the neighbor

# Example usage
g.bfs(0)  # Output: 0 1 2 3 4
