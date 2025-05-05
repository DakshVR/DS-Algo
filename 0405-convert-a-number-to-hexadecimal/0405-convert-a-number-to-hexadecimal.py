class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        result = []

        # Use 32-bit unsigned representation
        num &= 0xFFFFFFFF

        while num:
            result.append(hex_chars[num & 0xF])
            num >>= 4

        return ''.join(reversed(result))