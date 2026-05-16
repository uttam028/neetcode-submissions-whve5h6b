class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = int(len(nums)/3)
        freq = {}
        for num in nums:
            if(num in freq):
                freq[num] += 1
            else:
                freq[num] = 1
        result = []
        for key, value in freq.items():
            if(value > threshold):
                result.append(key)
        return result