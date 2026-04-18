class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dict = {}
        result = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                target = 0-(nums[i] + nums[j])
                if(target in dict.keys()):
                    dict[target].append({i, j})
                else:
                    dict[target] = [set([i, j])]
        for i in range(len(nums)):
            if(nums[i] in dict.keys()):
                candidates = dict[nums[i]]
                for val in candidates:
                    if(i not in val):
                        # print(list(val))
                        indices = list(val) + [i]
                        actuals = [nums[indices[x]] for x in range(0, 3)]
                        actuals.sort()
                        # print('----', inner, nums[inner[0]], nums[inner[1]], nums[inner[2]])
                        result.add(tuple([actuals[0], actuals[1], actuals[2]]))
        return [list(t) for t in result]