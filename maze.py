# Write your code here :-)
def bfs_maze(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    queue = deque([start])  # Initialize queue with the start position
    visited = set([start])  # Mark the start position as visited

    while queue:  # While there are positions to process
        x, y = queue.popleft()  # Dequeue the next position

        if (x, y) == goal:
            return True  # Goal found

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  # Explore neighbors (right, down, left, up)
            nx, ny = x + dx, y + dy  # Calculate new position
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))  # Mark as visited
                queue.append((nx, ny))  # Enqueue the new position

    return False  # No path found
