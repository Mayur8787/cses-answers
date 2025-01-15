class Solution:

    def give_input(self,inp):
        v1,v2 = inp.strip().split("\n")
        self.length = int(v1)
        self.numbers = list(map(int,v2.split()))
    
    def solution(self):
        moves = 0
        for i in range(1,len(self.numbers)):
            difference = self.numbers[i] - self.numbers[i-1]
            if difference < 0:
                moves += abs(difference)
                self.numbers[i] += abs(difference)
        return str(moves)


if __name__ == "__main__":
    length = input() + "\n"
    array = input()
    obj = Solution()
    obj.give_input(length+array)
    print(obj.solution())