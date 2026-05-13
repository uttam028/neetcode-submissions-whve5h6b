class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if(len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return 0 if nums[0] == val else 1

        left = 0
        right = len(nums)-1
        swaped = False
        while(left < right):
            if(nums[left] != val):
                left+=1
                continue
            while(nums[right] == val and left<right):
                right -= 1
            swaped = True
            temp = nums[right]
            nums[right] = nums[left]
            nums[left] = temp
        return left if swaped else right+1

            
