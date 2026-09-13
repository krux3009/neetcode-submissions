class Solution:
    def isAnagram(self, s, t):
        d1 = {}
        d2 = {}
        for char in s:
            if char in d1:
                d1[char] += 1
            else:
                d1[char] = 1

        for char in t:
            if char in d2:
                d2[char] += 1
            else:
                d2[char] = 1

        if d1.items() == d2.items():
            return True
        else:
            return False       

