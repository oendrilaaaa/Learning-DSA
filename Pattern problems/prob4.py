#      *
#     ***
#    *****
#   *******
#  *********
#  *********
#   *******
#    *****
#     ***
#      *

class Solution:
    def pattern9(self, n):
        u_st_n = 1
        u_sp_n = n-1
        for i in range(0, n, 1):
            print(" "*u_sp_n,"*"*u_st_n)
            u_st_n += 2
            u_sp_n -= 1
        l_st_n = (2*n) - 1
        l_sp_n = 0
        for i in range(0, n, 1):
            print(" "*l_sp_n,"*"*l_st_n)
            l_st_n -= 2
            l_sp_n += 1

p = Solution()
p.pattern9(5)