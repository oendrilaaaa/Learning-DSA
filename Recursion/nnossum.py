class Solution:
    def nNumbersSum(self, n):
        if n == 1:
            return n
        else:
            return n + self.nNumbersSum(n-1)

s = Solution()
print(s.nNumbersSum(5))
    