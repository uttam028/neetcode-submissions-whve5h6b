class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        bucket = {}
        for i in range(len(nums)):
            if(nums[i] not in bucket):
                bucket[nums[i]] = i
            else:
                if(i-bucket[nums[i]] <= k):
                    return True
                bucket[nums[i]] = i
    
        
        return False