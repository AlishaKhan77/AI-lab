class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()  # Initialize visited nodes
        visited.add(start)  # Mark the current node as visited
        print(start, end=' ')  # Process the current node (here, we print it)

        for neighbor in self.graph.get(start, []):  # Loop through neighbors
            if neighbor not in visited:  # Visit unvisited neighbors
                self.dfs(neighbor, visited)  # Recursive DFS call


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.dfs(0)
