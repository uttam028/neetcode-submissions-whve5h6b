class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # missing = -1
        expected_sum = int((len(nums) * (len(nums) + 1))/2)
        actual_sum = 0
        for num in nums:
            actual_sum += num
        
        return expected_sum - actual_sum