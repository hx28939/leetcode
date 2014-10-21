class Solution:
	def maxProfit(self, prices):
		if len(prices)<=1:
			return 0
		lowest = prices[0]
		profit = 0
		
		for x in range(len(prices)-1):
			if prices[x]<= lowest:
				lowest = prices[x]
			elif prices[x+1] < prices[x]:
				profit += (price[x]-lowest)
				lowest = prices[x+1]
		
		if prices[len(prices)-1] > lowest:
			profit += (prices[len(prices)-1] - lowest)
			