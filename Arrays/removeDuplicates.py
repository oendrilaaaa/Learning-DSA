class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        j = i+1
        if len(nums) == 1:
            return 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1

        return i+1
nums = [0, 1, 3, 3, 3, 4, 4, 4, 5, 5]
s = Solution()
print(s.removeDuplicates(nums))