class Solution:
    def maxProduct(self, nums):
        first = 0   # biggest number so far
        second = 0  # second biggest number so far
        
        for n in nums:
            if n > first:
                second = first
                first = n
            elif n > second:
                second = n
        
        return (first - 1) * (second - 1)
        