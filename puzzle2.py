# Write your code here :-)
class Node:
    def __init__(self, state, parent=None):
        self.state = state  # Current state of the puzzle
        self.parent = parent  # Reference to the parent node
        self.blank_index = state.index('0')  # Position of the blank tile
        self.g = 0  # Cost from the start node
        self.h = 0  # Heuristic cost

    def generate_next_states(self):
        next_states = []
        for move in self.get_possible_moves():
            new_state = list(self.state)  # Create a copy of the current state
            # Swap the blank with the adjacent tile
            new_state[self.blank_index], new_state[new_blank_index] = new_state[new_blank_index], new_state[self.blank_index]
            next_states.append(Node(''.join(new_state), self))  # Add new node to the list

        return next_states  # Return all possible states

# Example usage
start_state = '123456780'  # Example start state
goal_state = '123456780'   # Example goal state
a_star_result = a_star(start_state, goal_state, heuristic)
