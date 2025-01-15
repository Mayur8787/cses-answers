class Solution:

    def give_input(self, inp):
        self.n = int(inp)

    def solution(self):
        return str((int(self.n * "1", 2) + 1) % (10**9 + 7))


if __name__ == "__main__":
    number = input()
    obj = Solution()
    obj.give_input(number)
    print(obj.solution())
