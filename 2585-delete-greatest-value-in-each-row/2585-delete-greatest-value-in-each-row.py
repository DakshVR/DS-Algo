class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        for row in grid:
            row.sort()
        
        ans = 0
        # Repeat for the number of columns
        for col in range(len(grid[0])):
            max_deleted = 0
            for row in grid:
                max_deleted = max(max_deleted, row.pop())  # Delete max from row
            ans += max_deleted
        
        return ans
