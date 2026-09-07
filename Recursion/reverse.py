class Solution:
    def reverse(self, arr: list, n: int) -> None:
        if n <= 1:
            return n
        else:
            temp = arr[1]
            arr[1] = arr[-1]
            arr[-1] = temp
            return self.reverse(arr[1:-1], n-2)

s = Solution()
print(s.reverse([1, 2, 3, 4, 5], 5))