class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = Counter(word)
        
        for char in list(freq.keys()):  # Use a copy of the keys to avoid RuntimeError
            freq[char] -= 1  # Simulate removing one occurrence

            if freq[char] == 0:
                del freq[char]

            values = list(freq.values())
            if len(set(values)) == 1:
                return True

            # Restore original state
            freq[char] = freq.get(char, 0) + 1

        return False