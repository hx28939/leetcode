class Solution:

	def maxProfit(self, prices):
		if len(prices)<=1:
			return 0
		lowest = prices[0]
		profit = 0
		for x in range(len(prices)):
			lowest = min(lowest, prices[x])
			profit = max(profit, prices[x] - lowest)
		return profit