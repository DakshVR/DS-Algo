class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        answer = size * [1]

        prefix = 1
        for i in range(size):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(size-1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer
