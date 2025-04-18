class Solution:

    def give_input(self, inp):
        self.n = int(inp.strip())

    def solution(self):
        if 1 < self.n < 4:
            return "NO SOLUTION"
        if self.n == 4:
            return "2 4 1 3"
        array = [0] * self.n
        odd_index = 0
        even_index = self.n // 2 if self.n % 2 == 0 else self.n // 2 + 1

        for number in range(1, self.n + 1, 2):
            array[odd_index] = str(number)
            if even_index < self.n:
                array[even_index] = str(number + 1)
            odd_index += 1
            even_index += 1
        return " ".join(array)


if __name__ == "__main__":
    n = input()
    obj = Solution()
    obj.give_input(n)
    print(obj.solution())
