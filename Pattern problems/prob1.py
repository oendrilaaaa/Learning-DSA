# 1
# 12
# 123
# 1234
# 12345

class Solution:
    def pattern3(self, n):
        for i in range(1, n, 1):
            for j in range(1, i+1, 1):
                print(j, end="")
            print()
            

p = Solution()
p.pattern3(4)