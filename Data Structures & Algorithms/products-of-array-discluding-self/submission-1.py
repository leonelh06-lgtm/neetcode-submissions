class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prefix = [0] * n
        suff = [0] * n

        for i in range(n):
            if(i == 0):
                prefix[i] = 1
                continue
            prefix[i] = prefix[i-1] * nums[i-1]

        suff[n-1] = 1

        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]

        # Multiply prefix and suffix
        for i in range(n):
            res[i] = prefix[i] * suff[i]

        return res
