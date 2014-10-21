class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        aa = {}
        for i in range(len(A)):
            if A[i] in aa and aa[A[i]] == 1:
                aa[A[i]] = 2
            elif A[i] in aa and aa[A[i]] == 2:
            	del aa[A[i]]
            else:
                aa[A[i]] = 1
        c = aa.items()
        return(c[0][0])
        