class Solution:
    def selection_sort(self, nums):
        for i in range(0, len(nums), 1):
            min_idx = i
            for j in range(i+1, len(nums), 1):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[min_idx], nums[i] = nums[i], nums[min_idx]

        return nums
nums = [8,6,7,5,3,4,1,2]
s = Solution()
print(s.selection_sort(nums))

