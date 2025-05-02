class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        size = len(nums)

        for i in range(size):
            if nums[i] > nums[(i+1) % size]:
                count += 1
                if count > 1:
                    return False
        
        return True