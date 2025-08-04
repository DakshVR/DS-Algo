class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        water = capacity

        for i in range(len(plants)):
            if water >= plants[i]:
                water -= plants[i]
                steps += 1
            else:
                steps += 2 * i
                water = capacity - plants[i]
                steps += 1
        
        return steps