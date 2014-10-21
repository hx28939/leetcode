class Solution:
	def twoSum(self, num, target):
	    
	    tmp_num = {}
	    for i in range(len(num)):
	    	if target - num[i] in tmp_num:
	    		return (tmp_num[target-num[i]]+1, i+1)
	    	else:
	    		tmp_num[num[i]] = i
	    		
	    return (-1, -1)