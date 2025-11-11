import sys

class Solution:
    def __init__(self):
        self.n = None
        self.grid = None
        self.MOD = 10**9 + 7

    def give_input(self, inp: str):
        inp = inp.strip().split()
        self.n, self.grid = int(inp[0]), inp[1:]


    def solution(self):
        if self.grid[0][0] == '*' or self.grid[self.n-1][self.n-1] == '*':
            return str(0)
        grid = [[0]* self.n for _ in range(self.n)]

        for i in range(self.n):
            for j in range(self.n):
                if i == 0 and j == 0:
                    grid[i][j] = 1
                else:
                    top = grid[i-1][j] if i > 0 and self.grid[i-1][j] != '*' else 0
                    left = grid[i][j-1] if j > 0 and self.grid[i][j-1] != '*' else 0
                    grid[i][j] = (top + left) % self.MOD
        return str(grid[self.n-1][self.n-1])


if __name__ == "__main__":
    obj = Solution()
    data = sys.stdin.read().strip()
    obj.give_input(data)
    print(obj.solution())
