class Solution:
    def getFloorAndCeil(self, nums, x):
       floor = -1
       ceil = -1
       #floor
       st = 0
       end = len(nums)-1
       while st <= end:
           mid = st + (end-st)//2
           if nums[mid] == x:
               floor = nums[mid]
           if nums[mid] < x:
               floor = nums[mid]
               st = mid + 1
           else:
                end = mid - 1
        
       #ceil
       st = 0
       end = len(nums) - 1
       while st <= end:
           mid = st + (end - st)//2
           if nums[mid] == x:
               ceil = nums[mid]
           if nums[mid] < x:
               st = mid +1
           else:
               ceil = nums[mid]
               end = mid - 1
       return floor, ceil

nums = [1,4,5,7,9,10]
s = Solution()
print(s.getFloorAndCeil(nums, 8))

