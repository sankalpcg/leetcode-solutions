class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nSet = set()
        for i in nums:
            if i in nSet:
                return True
            else:
                nSet.add(i)
        return False