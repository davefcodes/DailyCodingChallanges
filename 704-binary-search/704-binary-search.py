class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lower_bound = 0
        upper_bound = len(nums) - 1
        
        while lower_bound <= upper_bound:
            midpoint = (lower_bound + upper_bound) // 2
        
            
            if nums[midpoint] == target: 
                return midpoint
            elif nums[midpoint] > target:
                upper_bound = midpoint - 1
            elif nums[midpoint] < target:
                lower_bound = midpoint + 1
            else:
                return midpoint
        return -1