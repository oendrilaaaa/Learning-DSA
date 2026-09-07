#      *
#     ***
#    *****
#   *******
#  *********

class Solution:
    def pattern7(self, n):
        st_n = 1
        sp_n = n-1
        for i in range(0, n, 1):
            print(" "*sp_n,"*"*st_n)
            sp_n -= 1
            st_n += 2
            
            

p = Solution()
p.pattern7(5)