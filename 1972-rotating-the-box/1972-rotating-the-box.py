class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])

        # shift stones ('#') to the rightmost position
        for row in boxGrid:
            write = n - 1 # rightmost position to drop a stone
            for col in range(n-1, -1, -1):
                if row[col] == '*':
                    write = col -1 # obstacle
                elif row[col] == '#':
                    if col != write:
                        row[write], row[col] = row[col], '.'
                    write -= 1
        rotated = [[''] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m-1-i] = boxGrid[i][j]
        
        return rotated