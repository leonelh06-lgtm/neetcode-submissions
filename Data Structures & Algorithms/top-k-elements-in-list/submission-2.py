class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {val:0 for val in nums}
        res = []
        for val in nums:
            freq[val] += 1
        
        for i in range(k):
            top = max(freq, key = freq.get)
            res.append(top)
            freq.pop(top);
        return res


            

            



        
        
