class Solution:
    def pattern14(self, n):
        char = 'A'
        for i in range(0, n, 1):
            for j in range(0, i, 1):
                print(char, end="")
            char = chr(ord(char) + 1)
            print()

p = Solution()
p.pattern14(5)