class Solution:
    def pattern7(self, n):
        k = n - 1
        for i in range(n):
            st_n = (2 * i) + 1
            space = "_" * k
            k -= 1
            star = "*"*st_n
            print(space + star)
            
            

p = Solution()
p.pattern7(5)