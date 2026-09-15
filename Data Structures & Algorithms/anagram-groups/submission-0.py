class Solution:
    def groupAnagrams(self, strs):
        res = []
        hashmap = defaultdict(list) 
        for string in strs:
            count = [0] * 26
            for ch in string:
                count[ord(ch) - 97] += 1
            hashmap[tuple(count)].append(string)
        res = list(hashmap.values())


        return res

 






