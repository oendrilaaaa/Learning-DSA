# 1
# 01
# 101
# 0101
# 10101

class Solution:
    def pattern11(self, n):
        for i in range(0, n+1 ,1):
            if i%2 == 0:
                for j in range(0, i, 1):
                    if j%2 != 0:
                        print("1", end="")
                    else:
                        print("0", end="")
                print()
            else:   
                for j in range(0, i, 1):
                    if j%2 != 0:
                        print("0", end="")
                    else:
                        print("1", end="")
                print()

p = Solution()
p.pattern11(5)