# 1
# 22
# 333
# 4444
# 55555

class Solution:
    def pattern4(self, n):
        for i in range(1, n+1, 1):
            for j in range(1, i+1, 1):
                print(i, end="")
            print()
            

p = Solution()
p.pattern4(4)