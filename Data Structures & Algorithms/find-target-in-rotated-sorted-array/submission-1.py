class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while(low<=high):
            mid = int((high+low)/2)
            trivial_left = nums[low] <=nums[mid]
            trivial_right = nums[mid]<=nums[high]
            if(target == nums[mid]):
                return mid
            
            if(nums[low]<= target < nums[mid]):
                high = mid-1
            elif(nums[high] >= target > nums[mid]):
                low = mid+1
            elif(trivial_left):
                low = mid+1
            else:
                high = mid-1
        return -1