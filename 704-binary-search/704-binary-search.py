class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lower_bound = 0
        upper_bound = len(nums) -1
        mid_point = 0
        
        while lower_bound <= upper_bound:
            mid_point = (upper_bound + lower_bound) // 2
            
            if nums[mid_point] < target:
               lower_bound = mid_point + 1
            elif nums[mid_point] > target:
                upper_bound = mid_point - 1
            else:
                return mid_point
        return -1