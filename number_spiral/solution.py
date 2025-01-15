class Solution:
    def give_input(self, inp):
        inputs = inp.strip().split("\n")
        self.total_cases = int(inputs[0])
        self.testcases = [list(map(int, case.split())) for case in inputs[1:]]

    def solution(self):
        results = []
        for y, x in self.testcases:
            n = max(x, y)
            if n % 2 == 0:
                if y == n:
                    results.append((n * n) - (x - 1))
                else:
                    results.append((n * n) - (n - 1) - (n - y))
            else:
                if x == n:
                    results.append((n * n) - (y - 1))
                else:
                    results.append((n * n) - (n - 1) - (n - x))
        return "\n".join(map(str, results))

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    t = input()
    obj = Solution()
    obj.give_input(t)
    print(obj.solution())
