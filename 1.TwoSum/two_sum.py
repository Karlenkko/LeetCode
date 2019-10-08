class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i, n in enumerate(nums):
            if target - n in mydict:
                return [mydict[target - n], i]
            mydict[n] = i
