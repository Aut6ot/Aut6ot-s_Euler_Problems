# note: I tried my best to work through this problem, and when I felt totally lost, I used this resource:
# https://martin-ueding.de/posts/project-euler-solution-15-lattice-paths/

import math


def lattice_paths(grid_size):
    steps = 2 * grid_size
    solution = math.factorial(steps) / (math.factorial(grid_size) * math.factorial(steps - grid_size))
    print(int(solution))


lattice_paths(20)
