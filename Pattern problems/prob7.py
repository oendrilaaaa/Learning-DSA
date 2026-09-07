# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


class Solution:
    def pattern10(self, n):
        st_n = 1
        for i in range(0, n-1, 1):
            print("*"*st_n)
            st_n += 1
        l_st_n = n
        for i in range(0, n, 1):
            print("*"*l_st_n)
            l_st_n -= 1

p = Solution()
p.pattern10(5)