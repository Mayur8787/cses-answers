class Solution:

    def give_input(self, inp):
        self.n = int(inp)

    def solution(self):
        count = 0

        while self.n >= 5:
            self.n //= 5
            count += self.n

        return str(count)


if __name__ == "__main__":
    number = input()
    obj = Solution()
    obj.give_input(number)
    print(obj.solution())
