class Solution:
    def rotateArrayByOne(self, nums):
        n = len(nums)
        temp = nums[0]
        for i in range(1, n, 1):
            nums[i-1] = nums[i]
        nums[n-1] = temp
        return nums
nums = [1,2,3,4,5]
s = Solution()
print(s.rotateArrayByOne(nums))