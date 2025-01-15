class Solution:

    def give_input(self, inp):
        v1, v2 = inp.strip().split("\n")
        self.n = int(v1)
        self.numbers = list(map(int, v2.split()))

    def solution(self):
        return str(len(set(self.numbers)))


if __name__ == "__main__":
    n = input() + "\n"
    numbers = input()
    obj = Solution()
    obj.give_input(n + numbers)
    print(obj.solution())
