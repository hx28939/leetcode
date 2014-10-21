class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if len(A) == 1:
            return A[0]
        maxP = 1
        minP = 1
        result = A[0]
        
        for i in A:
            tmp = maxP
            maxP = max(max(maxP * i, i), minP * i)
            minP = min(min(minP * i, i), tmp * i)
            result = max(maxP, result)
        
        return result