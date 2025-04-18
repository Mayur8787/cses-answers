class Solution:

    def give_input(self, input):
        v1, v2 = input.strip().split("\n")
        self.number = int(v1)
        self.lis = list(map(int, v2.split()))

    def solution(self):
        answer = (self.number * (self.number + 1)) // 2

        for num in self.lis:
            answer -= num

        return str(answer)


if __name__ == "__main__":
    number = input() + "\n"
    numbers = input()
    obj = Solution()
    obj.give_input(number + numbers)
    print(obj.solution())
