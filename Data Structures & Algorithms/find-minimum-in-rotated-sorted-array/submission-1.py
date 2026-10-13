class Solution:
    def findMin(self, nums: List[int]) -> int:
        for k in range(1,len(nums)):
            if nums[k-1]>nums[k]:
                return nums[k]
        return nums[0]