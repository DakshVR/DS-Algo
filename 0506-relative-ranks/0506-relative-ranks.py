class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        size = len(score)
        result = [""] * size

        heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(heap)

        rank = 1
        while heap:
            _, i = heapq.heappop(heap)
            if rank == 1:
                result[i] = "Gold Medal"
            elif rank == 2:
                result[i] = "Silver Medal"
            elif rank == 3:
                result[i] = "Bronze Medal"
            else:
                result[i] = str(rank)
            rank += 1
        
        return result