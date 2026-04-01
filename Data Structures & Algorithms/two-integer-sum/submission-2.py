class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = {}
        for i in range(len(nums)):
            # num = nums[i]
            if nums[i] in list.keys():
                index = list[nums[i]]
                return [index, i]
            else:
                list[target-nums[i]] = i
