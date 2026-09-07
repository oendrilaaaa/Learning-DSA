class Solution:
    def printNumbers(self, n):
        if n == 1:
            print(n)
        else:
            self.printNumbers(n-1)
            print(n)
            

s = Solution()
s.printNumbers(5)