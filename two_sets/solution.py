class Solution:

    def give_input(self, inp):
        self.n = int(inp)

    def solution(self):
        summ = (self.n * (self.n + 1)) // 2
        if summ % 2 != 0:
            return "NO"
        first = set()
        half = summ // 2
        number = self.n

        while half > 0:
            if half >= number:
                first.add(number)
                half -= number
            number -= 1
        second = set(i for i in range(1, self.n + 1) if i not in first)
        answer = (
            "YES\n"
            + str(len(first))
            + "\n"
            + " ".join(str(i) for i in first)
            + "\n"
            + str(len(second))
            + "\n"
            + " ".join(str(i) for i in second)
            + "\n"
        )
        return answer


if __name__ == "__main__":
    num = input()
    obj = Solution()
    obj.give_input(num)
    print(obj.solution())
