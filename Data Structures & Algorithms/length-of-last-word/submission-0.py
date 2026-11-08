class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 1. Split the string into a list of words by whitespace
        words = s.split()
        
        # 2. Return the length of the last item in that list
        return len(words[-1])
