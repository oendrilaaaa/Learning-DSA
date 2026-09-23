class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        st = 0
        end = len(nums)-1
        lb = end + 1
        while st <= end:
            mid = st +(end - st)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                st = mid + 1
            else:
                lb = mid
                end = mid- 1
        return lb
        
