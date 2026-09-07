class Solution:
    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(0, n-1, 1):
            for j in range(0, n-i-1, 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums
nums = [8,9,4,2,1]
s = Solution()
print(s.bubble_sort(nums))
        