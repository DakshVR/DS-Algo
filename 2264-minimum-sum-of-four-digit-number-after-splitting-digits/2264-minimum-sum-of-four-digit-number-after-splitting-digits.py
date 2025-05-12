class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted([int(d) for d in str(num)])
        num1 = digits[0] * 10 + digits[2]
        num2 = digits[1] * 10 + digits[3]
        return num1 + num2