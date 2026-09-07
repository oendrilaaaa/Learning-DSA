# class Solution:
#     def secondLargestElement(self, nums):
#         nums.sort()
#         for i in range(0, len(nums)-2, 1):
#             if nums[1] == nums[-1]:
#                 return -1
#             j = i+1
#             if nums[i] == nums[j]:
#                 del nums[j]
#         return nums[-2]
# nums = [10, 19, 3, 5, 8, 1, 19, 10, 15]
# s = Solution()
# print(s.secondLargestElement(nums))

class Solution:
    def secondLargestElement(self, nums):
        max_el = float('-inf')
        sec_max_el = float('-inf')
        
        for i in range(0, len(nums), 1):
            if nums[1] == nums[-1]:
                return -1
            if nums[i] > max_el:
                max_el = nums[i]
            
        for i in range(0, len(nums), 1):
            if nums[i] > sec_max_el and nums[i] < max_el:
                sec_max_el = nums[i]

        return sec_max_el

nums = [10, 19, 3, 5, 8, 1, 19, 10, 15]
s = Solution()
print(s.secondLargestElement(nums))
    
