import sys


class Solution:
    def give_input(self, inp):
        data = inp.split()
        self.n = int(data[0])
        self.numbers = map(int, data[1:])

    def solution(self):
        return str(len(set(self.numbers)))


if __name__ == "__main__":
    case = sys.stdin.read().strip()
    obj = Solution()
    obj.give_input(case)
    print(obj.solution())


# Code for the platform
"""sys.stdin.readline()

numbers = set()

for number in sys.stdin.read().split():
    numbers.add(number)

print(len(numbers))"""
