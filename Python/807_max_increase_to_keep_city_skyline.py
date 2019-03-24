"""
Decompose:
1. Determine the skyline from all 4 directions
2. Determine max height for each cell as a function of skylines

Data:
1. grid

Pattern:
1. given the grid and direction, return skyline
2. given a cell and skylines, return max value for the cell
"""
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        grid_len = len(grid)
        left_or_right = [max(grid[i]) for i in range(0, grid_len)]
        top_or_bottom = [max(list(zip(*grid))[i]) for i in range(0, grid_len)]
                
        counter = 0
        for i in range(0, grid_len):
            for j in range(0, grid_len):
                if grid[i][j] in (left_or_right[i], top_or_bottom[j]):
                    pass
                else:
                    counter += min(left_or_right[i], top_or_bottom[j]) - grid[i][j]
        return counter