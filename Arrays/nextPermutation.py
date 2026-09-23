class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        idx = -1
        n = len(nums) - 1
        for i in range(n, 0, -1):
            if nums[i] > nums[i-1]:
                idx = i-1
                break
        if idx == -1:
            nums[:] = nums[::-1]
            return
        for i in range(n, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break
        nums[idx+1:] = nums[idx+1:][::-1]
        
        