#brute force approach

# class Solution:
#     def searchRange(self, nums, target):
#         first_occ = -1
#         last_occ = -1
#         for i in range(0, len(nums), 1):
#             if nums[i] == target:
#                 first_occ = i
#                 break
#         for j in range(len(nums)-1, -1, -1):
#             if nums[j] == target:
#                 last_occ = j
#                 break
#         return [first_occ, last_occ]
# nums = [5, 7, 7, 8, 8, 10]
# s = Solution()
# print(s.searchRange(nums, 7))

class Solution:
    def searchRange(self, nums, target):
        first_occ = -1
        last_occ = -1
        st = 0
        end = len(nums) - 1
        while st <= end:
            if nums[mid] < target:
                st = mid + 1