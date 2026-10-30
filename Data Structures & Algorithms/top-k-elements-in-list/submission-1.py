class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {num:0 for num in nums}
        res = []
        for num in nums:
            if(num in count):
                count[num] += 1
        
        for i in range(k):
            top = max(count, key = count.get)
            res.append(top)
            count.pop(top)
            

        return res
            

            



        
        
