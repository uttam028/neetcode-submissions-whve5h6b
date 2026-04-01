class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in list.keys():
                index = list[num]
                return [index, i]
            else:
                list[target-num] = i
