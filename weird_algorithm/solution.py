class Solution:

    def give_input(self, inp):
        self.inp = int(inp.strip())

    def solution(self) -> str:
        def helper(n):
            if n == 1:
                return ""
            if n % 2 == 0:
                return f"{n//2} " + helper(n // 2)
            else:
                return f"{(n*3)+1} " + helper((n * 3) + 1)

        return str(self.inp) + " " + helper(self.inp)


if __name__ == "__main__":
    n = input()
    obj = Solution()
    obj.give_input(n)
    print(obj.solution())
