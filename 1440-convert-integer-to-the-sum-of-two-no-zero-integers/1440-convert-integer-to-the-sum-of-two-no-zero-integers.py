class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def has_zero(x):
            return '0' in str(x)

        for i in range(1, n):
            if not has_zero(i) and not has_zero(n - i):
                return [i, n - i]