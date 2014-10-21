class Solution:
	def maxProfit(self, prices):
		if len(prices)<=1:
			return 0
		lowest = prices[0]
		count = 0
		profit = []
		
		for i in range(len(prices)):
			lowest = min(lowest, prices[i])
			count = max(count, prices[i] - lowest)
			profit.append(count)
			
		highest = prices[len(prices)-1]
		count_2 = 0
		profit_2 = []
		for curprice in reversed(prices):
			highest = max(highest, curprice)
			count_2 = max(count_2, highest - curprice)
			profit_2.insert(0, count_2)
			
		maxprofit = profit[-1]
		for i in xrange(len(prices) -1):
			maxprofit = max(maxprofit, profit[i] + profit_2[i+1])	
	
		return maxprofit
			