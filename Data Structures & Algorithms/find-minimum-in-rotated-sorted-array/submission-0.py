class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = int((low+high)/2)
            trivial_left = nums[low] <= nums[mid]
            trivial_right = nums[high] >= nums[mid]
            if(trivial_left and trivial_right):
                return nums[low]
            elif(trivial_left and trivial_right is False):
                low = mid+1
            elif(trivial_left is False and trivial_right):
                high = mid
            