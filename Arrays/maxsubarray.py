class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = 0
        max_sum = float("-inf")
        for i in range(0, len(nums), 1):
            curr_sum += nums[i]
            if curr_sum < nums[i]:
                curr_sum = nums[i]
            max_sum = max(max_sum, curr_sum)
        return max_sum