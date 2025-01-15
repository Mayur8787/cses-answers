class Solution:

    def give_input(self,inp):
        self.inp = inp.strip()

    def solution(self):
        max_score = 0
        curr_score = 1
        curr_char = self.inp[0]

        for i in range(1,len(self.inp)):
            if curr_char != self.inp[i]:
                max_score = max(max_score,curr_score)
                curr_score = 0
                curr_char = self.inp[i]
            curr_score += 1
        
        max_score = max(max_score,curr_score)
        
        return str(max_score)


if __name__ == "__main__":
    inp = input()
    obj = Solution()
    obj.give_input(inp)
    print(obj.solution())