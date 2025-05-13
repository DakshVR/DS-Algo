class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)
        total = sum(cardPoints[:k])
        max_sum = total
        for i in range(1, k+1):
            total = total - cardPoints[k-i] + cardPoints[-i]
            max_sum = max(max_sum, total)
        
        return max_sum