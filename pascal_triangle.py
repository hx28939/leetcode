def getRow(rowIndex):
        def cn(k,n):
            val = 1
            for i in range(k):
                val = val * (n-i)/(i+1)
            return val
        res = []
        for i in range(rowIndex+1):
            res.append(cn(i,rowIndex))
        return res