class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        stops = [0] * 1001  # max location is 1000

        for num_passengers, start, end in trips:
            stops[start] += num_passengers
            stops[end] -= num_passengers
        
        current_passengers = 0
        for passenger_change in stops:
            current_passengers += passenger_change
            if current_passengers > capacity:
                return False
        
        return True