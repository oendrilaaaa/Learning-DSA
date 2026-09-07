class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        count = 0
        for i in range(0, len(nums), 1):
            if nums[i] == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count
nums =  [0, 0, 0, 0, 0, 0, 0]
s = Solution()
print(s.findMaxConsecutiveOnes(nums))