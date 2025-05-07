class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()

        for word in words2:
            word_count = Counter(word)
            for char in word_count:
                max_freq[char] = max(max_freq[char], word_count[char])
        
        result = []
        for word in words1:
            word_count = Counter(word)
            if all(word_count[c] >= max_freq[c] for c in max_freq):
                result.append(word)
        
        return result