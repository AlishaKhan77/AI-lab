Search Algorithms - DFS, BFS, Iterative Deepening, and Beyond
Objective:
The objective of this lab is to implement and compare various search algorithms in artificial
intelligence, focusing on DFS, BFS, and IDDFS. Additionally, the lab aims to explore practical
considerations such as heuristic functions, informed search strategies, and their applications.
Tasks:
1. Implementing Basic Search Algorithms:
○ DFS (Depth-First Search):
■ Implement DFS to traverse a graph or search tree recursively.
■ Track visited nodes to prevent revisiting and handle cycles in graphs.
○ BFS (Breadth-First Search):
■ Implement BFS to explore all nodes at the present "depth" level before moving
on to nodes at the next level.
■ Utilize a queue data structure to manage nodes to be visited.
○ IDDFS (Iterative Deepening Depth-First Search):
■ Implement IDDFS to combine benefits of BFS and DFS for optimal memory
usage and completeness.
■ Perform DFS repeatedly with increasing depth limits until the goal is found.
2. Enhanced Search Strategies:
○ Informed Search (A Algorithm):*
■ Implement A* search algorithm using a heuristic function to guide the search
towards the goal efficiently.
■ Compare the performance of A* with the uninformed search algorithms (DFS,
BFS, IDDFS).
○ Greedy Best-First Search:
■ Implement Greedy Best-First Search using a heuristic function that selects the
node closest to the goal based on a heuristic estimate.
■ Discuss the limitations and advantages compared to A* and other algorithms.
3. Applications and Analysis:
○ Pathfinding in a Maze:
■ Apply each algorithm to find the shortest path through a maze represented as a
grid.
■ Compare path lengths, computational effort, and feasibility for larger maze sizes.
○ 8-Puzzle Problem:
■ Solve the 8-Puzzle using DFS, BFS, IDDFS, A*, and Greedy Best-First Search.
■ Analyze the number of moves, computational resources used, and effectiveness
of each algorithm


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.dfs(0)  # Output: 0 1 3 2 4


from collections import deque

class Graph:
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# Example usage
g.bfs(0)  # Output: 0 1 2 3 4


class Graph:
    def iddfs(self, start, goal, max_depth):
        for depth in range(max_depth):
            visited = set()
            if self.dls(start, goal, depth, visited):
                return True
        return False

    def dls(self, node, goal, depth, visited):
        if depth == 0 and node == goal:
            return True
        if depth > 0:
            visited.add(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    if self.dls(neighbor, goal, depth - 1, visited):
                        return True
        return False

# Example usage
g.iddfs(0, 3, 3)  # Output: True if path exists within depth limit


import heapq

class AStarGraph(Graph):
    def a_star(self, start, goal, heuristic):
        open_set = []
        heapq.heappush(open_set, (0, start))
        came_from = {}
        g_score = {node: float('inf') for node in self.graph}
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.graph}
        f_score[start] = heuristic[start]

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                return True  # Path found

            for neighbor in self.graph.get(current, []):
                tentative_g_score = g_score[current] + 1  # Assume all edges cost 1
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic[neighbor]
                    if neighbor not in [i[1] for i in open_set]:
                        heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return False  # No path found

# Example heuristic function (simple)
def heuristic(node):
    # Placeholder: return 0 for all nodes for simplification
    return 0

g = AStarGraph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.a_star(0, 2, heuristic)  # Output: True if path found




class GreedyGraph(Graph):
    def greedy_best_first(self, start, goal, heuristic):
        open_set = []
        heapq.heappush(open_set, (heuristic[start], start))
        visited = set()

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == goal:
                return True  # Path found

            visited.add(current)

            for neighbor in self.graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(open_set, (heuristic[neighbor], neighbor))

        return False  # No path found

# Example usage
g = GreedyGraph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.greedy_best_first(0, 2, heuristic)  # Output: True if path found




def bfs_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])
    visited = set([start])

    while queue:
        x, y = queue.popleft()

        if (x, y) == goal:
            return True

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Right, Down, Left, Up
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return False  # No path found

# Example maze (0 = path, 1 = wall)
maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
    [1, 1, 1, 0]
]
bfs_maze(maze, (0, 0), (3, 3))  # Output: True if path found



class Node:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.blank_index = state.index('0')
        self.g = 0  # Cost to reach this node
        self.h = 0  # Heuristic cost

    def get_blank_position(self):
        return self.blank_index // 3, self.blank_index % 3

    def get_possible_moves(self):
        row, col = self.get_blank_position()
        moves = []

        if row > 0:  # Move blank up
            moves.append('U')
        if row < 2:  # Move blank down
            moves.append('D')
        if col > 0:  # Move blank left
            moves.append('L')
        if col < 2:  # Move blank right
            moves.append('R')

        return moves

    def generate_next_states(self):
        next_states = []
        for move in self.get_possible_moves():
            new_state = list(self.state)
            blank_row, blank_col = self.get_blank_position()

            if move == 'U':
                new_blank_index = (blank_row - 1) * 3 + blank_col
            elif move == 'D':
                new_blank_index = (blank_row + 1) * 3 + blank_col
            elif move == 'L':
                new_blank_index = blank_row * 3 + (blank_col - 1)
            elif move == 'R':
                new_blank_index = blank_row * 3 + (blank_col + 1)

            # Swap the blank with the adjacent tile
            new_state[self.blank_index], new_state[new_blank_index] = new_state[new_blank_index], new_state[self.blank_index]
            next_states.append(Node(''.join(new_state), self))

        return next_states
from collections import deque

def bfs(start_state, goal_state):
    visited = set()
    queue = deque([Node(start_state)])

    while queue:
        current_node = queue.popleft()

        if current_node.state == goal_state:
            return current_node  # Goal found

        visited.add(current_node.state)

        for next_node in current_node.generate_next_states():
            if next_node.state not in visited:
                queue.append(next_node)

    return None  # No solution
def dfs(start_state, goal_state, visited=None):
    if visited is None:
        visited = set()

    current_node = Node(start_state)

    if current_node.state == goal_state:
        return current_node  # Goal found

    visited.add(current_node.state)

    for next_node in current_node.generate_next_states():
        if next_node.state not in visited:
            result = dfs(next_node.state, goal_state, visited)
            if result is not None:
                return result  # Goal found

    return None  # No solution
def iddfs(start_state, goal_state, max_depth):
    for depth in range(max_depth):
        visited = set()
        if dls(start_state, goal_state, depth, visited):
            return True
    return False

def dls(state, goal_state, depth, visited):
    if depth == 0 and state == goal_state:
        return True
    if depth > 0:
        visited.add(state)
        current_node = Node(state)
        for next_node in current_node.generate_next_states():
            if next_node.state not in visited:
                if dls(next_node.state, goal_state, depth - 1, visited):
                    return True
    return False
import heapq

def heuristic(state):
    goal_state = '123456780'
    h = sum(1 for i in range(9) if state[i] != goal_state[i] and state[i] != '0')
    return h

def a_star(start_state, goal_state):
    open_set = []
    heapq.heappush(open_set, (0, Node(start_state)))
    visited = set()

    while open_set:
        current_node = heapq.heappop(open_set)[1]

        if current_node.state == goal_state:
            return current_node  # Goal found

        visited.add(current_node.state)

        for next_node in current_node.generate_next_states():
            if next_node.state not in visited:
                next_node.g = current_node.g + 1
                next_node.h = heuristic(next_node.state)
                heapq.heappush(open_set, (next_node.g + next_node.h, next_node))

    return None  # No solution
def greedy_best_first(start_state, goal_state):
    open_set = []
    heapq.heappush(open_set, (heuristic(start_state), Node(start_state)))
    visited = set()

    while open_set:
        current_node = heapq.heappop(open_set)[1]

        if current_node.state == goal_state:
            return current_node  # Goal found

        visited.add(current_node.state)

        for next_node in current_node.generate_next_states():
            if next_node.state not in visited:
                heapq.heappush(open_set, (heuristic(next_node.state), next_node))

    return None  # No solution
start_state = '123456780'  # Initial state
goal_state = '123456780'   # Goal state

# Test BFS
bfs_result = bfs(start_state, goal_state)
print("BFS found solution:", bfs_result.state if bfs_result else "No solution")

# Test DFS
dfs_result = dfs(start_state, goal_state)
print("DFS found solution:", dfs_result.state if dfs_result else "No solution")

# Test IDDFS
iddfs_result = iddfs(start_state, goal_state, max_depth=20)
print("IDDFS found solution:", "Found" if iddfs_result else "No solution")

# Test A*
a_star_result = a_star(start_state, goal_state)
print("A* found solution:", a_star_result.state if a_star_result else "No solution")

# Test Greedy Best-First Search
greedy_result = greedy_best_first(start_state, goal_state)
print("Greedy Best-First found solution:", greedy_result.state if greedy_result else "No solution")

