
class Solution:
    def give_input(self,inp):
        self.s = inp.strip()
        self.ref = set()

    def solution(self):
        def permute(s,left,right):
            if left == right:
                self.ref.add("".join(s))
            else:
                for i in range(left, right+1):
                    s[left], s[i] = s[i], s[left]
                    permute(s, left+1, right)
                    s[left], s[i] = s[i], s[left]
        permute(list(self.s),0,len(self.s)-1)
        answer = f"{len(self.ref)}\n" + "\n".join(sorted(self.ref))
        return answer


if __name__ == "__main__":
    obj = Solution()
    obj.give_input(input())
    print(obj.solution())
