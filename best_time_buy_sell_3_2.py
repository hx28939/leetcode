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
		for i in range(len(prices)-1, -1, -1):
			highest = max(highest, prices[i])
			count_2 = max(count_2, highest - prices[i])
			profit_2.insert(0,count_2)
		
		maxprofit = 0
		for i in range(len(prices)):
			maxprofit = max(maxprofit, profit[i]+profit_2[len(prices)-1-i])
			
			
		return maxprofit
			