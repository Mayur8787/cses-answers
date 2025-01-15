class Solution:

    def give_input(self, inp):
        v1, v2 = inp.strip().split("\n")
        self.n, self.k = map(int, v1.split())
        self.primes = sorted(map(int, v2.split()))

    def solution(self):
        multiples = set()
        for prime in self.primes:
            multiples.update(range(prime, self.n + 1, prime))
        return str(len(multiples))


if __name__ == "__main__":
    first = input() + "\n"
    second = input()
    obj = Solution()
    obj.give_input(first + second)
    print(obj.solution())
