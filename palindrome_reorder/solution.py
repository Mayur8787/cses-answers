class Solution:
    def give_input(self, inp):
        self.string = inp.strip()

    def solution(self):
        letter_counts = [0] * 26
        for char in self.string:
            letter_counts[ord(char) - ord("A")] += 1
        odd = ""
        odd_count = 0
        first_half = ""
        for i in range(26):
            if letter_counts[i] % 2 != 0:
                odd = chr(i + ord("A"))
                odd_count += 1
                if odd_count > 1:
                    return "NO SOLUTION"
            else:
                first_half += (chr(ord("A") + i) * (letter_counts[i] // 2))
        if odd:
            return first_half + (odd * letter_counts[ord(odd) - ord("A")]) + first_half[::-1]
        return first_half + first_half[::-1]


if __name__ == "__main__":
    obj = Solution()
    obj.give_input(input())
    print(obj.solution())
