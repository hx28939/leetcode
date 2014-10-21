class Solution:
	
	def plusOne(self, digits):
		w = (len(digits) - 1)
		ss = 0
		
		while (ss == 0):
			if (digits[w] == 9):
				digits[w] = 0
				w -= 1
			else:
				ss = 1
		
		if (w == -1):
			newb = [0]*(len(digits) + 1)
			newb[0] = 1
			return newb
		else:
			digits[w] += 1
			return digits
			