from typing import List

class Solution:
    def minNumberOfHours(
        self, initialEnergy: int, initialExperience: int,
        energy: List[int], experience: List[int]
    ) -> int:
        total_hours = 0
        
        # Check total energy requirement
        required_energy = sum(energy) + 1
        if initialEnergy < required_energy:
            total_hours += required_energy - initialEnergy

        # Check experience requirement for each opponent
        current_experience = initialExperience
        for exp in experience:
            if current_experience <= exp:
                hours_needed = exp - current_experience + 1
                total_hours += hours_needed
                current_experience += hours_needed
            current_experience += exp

        return total_hours
