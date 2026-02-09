class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
            
        n = len(nums)
        officer = 0
        cm = 1
        
        while cm < n:
            if nums[cm] == nums[cm - 1]:
                cm += 1
                continue
            else:
                officer += 1
                nums[officer] = nums[cm]
                cm += 1
                
        return officer + 1