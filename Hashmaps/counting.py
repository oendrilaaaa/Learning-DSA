nums =[1,1,2,2,2,2,3,4,4]
class Solution:
    def countFrequencies(self, nums):
        hashmap ={}
        for i in range(0, len(nums), 1):
            hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1

        return hashmap
s = Solution()
print(s.countFrequencies(nums))
