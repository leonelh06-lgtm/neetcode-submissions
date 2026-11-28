class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            counter = tuple(sorted(Counter(word).items()))
            res[counter].append(word)  
        return list(res.values())

            