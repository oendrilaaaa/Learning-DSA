# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

class Solution:
    def pattern12(self, n):
        space_n = (2*n) 
        for i in range(0, n+1, 1):
            for j in range(1, i+1, 1):
                print(j, end="")
            print(space_n*" ",end="")
            for k in range(i, 0, -1):
                print(k, end="")
            print()
            space_n -= 2

p = Solution()
p.pattern12(5)