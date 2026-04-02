class Solution:
    @staticmethod
    def sort(a:str) -> str:
        return "".join(sorted(a))

    # @staticmethod
    # def isAnagram(a: str, b:str) -> bool:
    #     return sort(a) == sort(b)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        list = {}
        for item in strs:
            if self.sort(item) in list.keys():
                inner_list = list[self.sort(item)]
                inner_list.append(item)
            else:
                list[self.sort(item)] = [item]
        return [v for k, v in list.items()]