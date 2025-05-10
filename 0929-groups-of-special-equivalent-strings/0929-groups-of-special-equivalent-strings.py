class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        groups = set()

        for word in words:
            even = [word[i] for i in range(0, len(word), 2)]
            odd = [word[i] for i in range(1, len(word), 2)]

            even.sort()
            odd.sort()

            sign = (tuple(even), tuple(odd))

            groups.add(sign)
        return len(groups)