class Graph:
    def iddfs(self, start, goal, max_depth):
        for depth in range(max_depth):  # Increment depth until max depth
            visited = set()  # Track visited nodes
            if self.dls(start, goal, depth, visited):  # Perform depth-limited search
                return True  # Goal found
        return False  # No solution found within depth limits

    def dls(self, node, goal, depth, visited):
        if depth == 0 and node == goal:
            return True  # Goal found at this depth
        if depth > 0:  # Only explore if depth allows
            visited.add(node)  # Mark node as visited
            for neighbor in self.graph.get(node, []):  # Check neighbors
                if neighbor not in visited:  # Visit unvisited neighbors
                    if self.dls(neighbor, goal, depth - 1, visited):
                        return True  # Goal found in recursive call
        return False  # Goal not found
