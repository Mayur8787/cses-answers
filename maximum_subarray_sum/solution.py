from math import inf


class Solution:

    def give_input(self, inp):
        v1, v2 = inp.strip().split("\n")
        self.arr = list(map(int, v2.split()))

    def solution(self):
        curr, maxx = 0, -inf

        for i in self.arr:
            curr = max(i, curr + i)
            maxx = max(maxx, curr)
        return str(maxx)


if __name__ == "__main__":
    length = input() + "\n"
    numbers = input()
    obj = Solution()
    obj.give_input(length+numbers)
    print(obj.solution())
