import sys

class Solution:
    def give_input(self,inp):
        inp = inp.strip().split("\n")
        self.n, self.q = map(int, inp[0].split())
        self.numbers = list(map(int, inp[1].split()))
        self.queries = [tuple(map(int, i.split())) for i in inp[2:]]

    def solution(self):
        prefix_sum = [0] * (self.n + 1)
        for i in range(1, self.n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + self.numbers[i - 1]

        results = []
        for l, r in self.queries:
            total = prefix_sum[r] - prefix_sum[l - 1]
            results.append(str(total))

        return "\n".join(results)

if __name__ == "__main__":
    obj = Solution()
    obj.give_input(sys.stdin.read())
    print(obj.solution())
