class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) <= 1 : 
            return len(nums)
        if len(nums) == 2 : 
            if nums[1] != nums[0] :
                return 2
            else :
                return 1
        
        i = 1
        count = 1
        while i < len(nums) - 1 :    
            prevdiff = nums[i] - nums[i - 1]
            currdiff = nums[i + 1] - nums[i]
            if currdiff * prevdiff >= 0 :
                del(nums[i])
            else :
                prevdiff = currdiff
                i += 1
                count += 1
                
        if (nums[len(nums)-1] - nums[len(nums)-2]) * (nums[len(nums)-2] - nums[len(nums)-3]) < 0 :
            return count + 1
        else:
            return count
