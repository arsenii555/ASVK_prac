from collections import deque


class Maze:
    def __init__(self, N):
        self.N = N
        self.grid = [['█' for _ in range(N * 2 + 1)] for _ in range(N * 2 + 1)]
        self.graph = {}
        self.rooms = set()
        for i in range(N):
            for j in range(N):
                self.grid[2 * i + 1][2 * j + 1] = '·'
                self.rooms.add((2 * i + 1, 2 * j + 1))
                self.graph[(2 * i + 1, 2 * j + 1)] = set()

    def __str__(self):
        return '\n'.join([''.join(row) for row in self.grid])

    def __getitem__(self, key):
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]
        x0, y0 = 2 * x0 + 1, 2 * y0 + 1
        x1, y1 = 2 * x1 + 1, 2 * y1 + 1
        return self.bfs_path_exists((x0, y0), (x1, y1))

    def __setitem__(self, key, value):
        if value not in ['·', '█']:
            return
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]
        x0, y0 = 2 * x0 + 1, 2 * y0 + 1
        x1, y1 = 2 * x1 + 1, 2 * y1 + 1
        if x0 == x1:
            for y in range(min(y0, y1), max(y0, y1) + 1):
                if (x0, y) not in self.rooms:
                    self.grid[y][x0] = value
                    if value == '·':
                        if (x0, y) not in self.graph:
                            self.graph[(x0, y)] = set()
                        for neighbor in [(x0 - 1, y), (x0 + 1, y), (x0, y + 1), (x0, y - 1)]:
                            if neighbor in self.graph:
                                self.graph[(x0, y)].add(neighbor)
                                self.graph[neighbor].add((x0, y))
                    else:
                        if (x0, y) in self.graph:
                            del self.graph[(x0, y)]
                        for neighbor in [(x0 - 1, y), (x0 + 1, y), (x0, y + 1), (x0, y - 1)]:
                            if neighbor in self.graph:
                                self.graph[neighbor].discard((x0, y))
        elif y0 == y1:
            for x in range(min(x0, x1), max(x0, x1) + 1):
                if (x, y0) not in self.rooms:
                    self.grid[y0][x] = value
                    if value == '·':
                        if (x, y0) not in self.graph:
                            self.graph[(x, y0)] = set()
                        for neighbor in [(x - 1, y0), (x + 1, y0), (x, y0 + 1), (x, y0 - 1)]:
                            if neighbor in self.graph:
                                self.graph[(x, y0)].add(neighbor)
                                self.graph[neighbor].add((x, y0))
                    else:
                        if (x, y0) in self.graph:
                            del self.graph[(x, y0)]
                        for neighbor in [(x - 1, y0), (x + 1, y0), (x, y0 + 1), (x, y0 - 1)]:
                            if neighbor in self.graph:
                                self.graph[neighbor].discard((x, y0))

    def bfs_path_exists(self, start, goal):
        graph = self.graph
        if start == goal:
            return True
        visited = set()
        queue = deque([start])
        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                if vertex == goal:
                    return True
                queue.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
        return False


import sys

exec(sys.stdin.read())
