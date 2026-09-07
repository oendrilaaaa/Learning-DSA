#  *********
#   *******
#    *****
#     ***
#      *

class Solution:
    def pattern8(self, n):
        st_n = (2*n)-1
        sp_n = 0
        for i in range(0, n, 1):
            print(" "*sp_n, "*"*st_n)
            st_n -= 2
            sp_n += 1

p = Solution()
p.pattern8(5)