class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count = {}
        for char in s:
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1
            
        for char in t:
            if char not in letter_count:
                return False
            letter_count[char] -= 1
            if letter_count[char] < 0:
                return False
            
        for val in letter_count.values():
            if val != 0:
                return False
        return True