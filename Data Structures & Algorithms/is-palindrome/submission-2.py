class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                new_s += ch.lower()
        l = 0
        r = len(new_s) - 1
        while l < r:
            if new_s[l] == new_s[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
