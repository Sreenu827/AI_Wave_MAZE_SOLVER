class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        self.rows = len(maze)
        self.cols = len(maze[0])
        self.path = []

    def solve_maze(self, start, end):
        if self.dfs(start, end):
            return self.path
        else:
            return None

    def dfs(self, current, end):
        row, col = current
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.maze[row][col] == 1 or self.visited[row][col]:
            return False

        self.visited[row][col] = True
        self.path.append(current)

        if current == end:
            return True

        if self.dfs((row + 1, col), end) or self.dfs((row - 1, col), end) or self.dfs((row, col + 1), end) or self.dfs((row, col - 1), end):
            return True

        self.path.pop()
        return False


# Example usage:
maze = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0]
]

solver = MazeSolver(maze)
start = (0, 0)
end = (4, 4)
solution = solver.solve_maze(start, end)

if solution:
    print("Path found:", solution)
else:
    print("No path found")
