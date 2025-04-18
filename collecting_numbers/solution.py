class Solution:

    def give_input(self, inp):
        v1, v2 = inp.strip().split("\n")
        self.n = int(v1)
        self.numbers = list(map(int, v2.split()))

    def solution(self):
        ref = set()

        for number in self.numbers:
            if number - 1 not in ref:
                ref.add(number)
            else:
                ref.remove(number - 1)
                ref.add(number)
        return str(len(ref))


if __name__ == "__main__":
    n = input() + "\n"
    numbers = input()
    obj = Solution()
    obj.give_input(n + numbers)
    print(obj.solution())
