class Solution:
	def maxProfit(self, prices):
		if len(prices)<=1:
			return 0
		b = []
		for x in range(len(prices)-1):
			b[x] = prices[x+1] - prices[x]
			
		start_p = 0
		end_p = len(b)-1
		# kick the useless ones out
		i = start_p
		while b[i] < 0:
			i += 1
		start_p = i
		i = end_p
		while b[i] < 0:
			i -= 1
		end_p = i
		
		middle_p = 0
		min_v = b[start_p]
		for x in range(start_p, end_p+1):
			if b[x] < min_v:
				min_v = b[x]
				middle_p = x
		
		# now, 2 parts: start_p to middle_p, middle_p+1 to end_p
		min_left = b[start_p]
		left_p = start_p
		for x in range(start_p, middle_p):
			if b[x] < min_left:
				min_left = b[x]
				left_p = x
		min_right = b[middle_p+1]
		right_p = end_p
		for x in range(middle_p+1,end_p+1):
			if b[x] < min_right:
				min_right = b[x]
				right_p = x
		profit_l = max(sum(b[start_p:left_p]), sum(b[start_p:middle_p]), sum(b[left_p+1,middle_p]))
		profit_2 = max(sum(b[middle_p+1:right_p]), sum(b[middle_p+1:end_p]),sum(b[right_p+1,end_p]))
		profit = profit_1 + profit_2
		return profit
		