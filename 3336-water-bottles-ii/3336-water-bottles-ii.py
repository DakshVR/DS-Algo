class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        # Start by drinking all initial bottles
        total_drunk_bottel = numBottles
        empty = numBottles
        full =0
        while empty >= numExchange:
            empty -= numExchange
            full += 1
            total_drunk_bottel += full
            empty += full
            full =0
            numExchange += 1
        return total_drunk_bottel