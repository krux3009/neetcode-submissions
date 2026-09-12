class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checker = {}
        res = []
        for i in range(len(nums)):
            if nums[i] not in checker:
                checker[nums[i]] = [i]
            else:
                checker[nums[i]].append(i)
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in checker and checker[difference] != [i]:
                res = checker[nums[i]] + checker[difference]
                res = list(set(res))
                return res
            
        