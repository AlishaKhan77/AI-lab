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

