import sys


class Solution:
    def give_input(self, inp):
        self.piles = [
            list(map(int, line.split())) for line in inp.strip().split("\n")[1:]
        ]

    def solution(self):
        answer = []
        for pile in self.piles:
            if sum(pile) % 3 == 0 and 2 * min(pile) >= max(pile):
                answer.append("YES")
            else:
                answer.append("NO")
        return "\n".join(answer)


if __name__ == "__main__":
    data = sys.stdin.read().strip()
    obj = Solution()
    obj.give_input(data)
    print(obj.solution())


# Code for the platform
# t = input()
# data = ""
# data += t + "\n"

# for i in range(int(t)):
#     data += input() + "\n"

# obj = Solution()
# obj.give_input(data)
# print(obj.solution())
