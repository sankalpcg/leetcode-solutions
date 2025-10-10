class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start<=end:
            mid = int(floor((start+end)/2))
            if target == nums[mid]:
                return mid
            elif target>nums[mid]:
                start = mid+1
            elif target<nums[mid]:
                end = mid-1
        else:
            return -1