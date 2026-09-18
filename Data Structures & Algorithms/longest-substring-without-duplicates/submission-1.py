class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checker = {}
        l = 0
        r = 0
        res = 0
        while r <= len(s) - 1:
            if s[r] not in checker:
                checker[s[r]] = 1
                res = max(res, r - l + 1)
                r += 1
            else:
                if s[l] in checker:
                    del checker[s[l]]
                    l += 1
        return res
