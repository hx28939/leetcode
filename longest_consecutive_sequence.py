class Solution:
	def longestConsecutive(self, num):
		dict = {x:False for x in num}
		longest = -1
		for i in dict:
			if dict[i] == False:
				current = i + 1
				len1 = 0
				while current in dict and dict[current] == False:
					
					dict[current] = True
					current += 1
					len1 += 1
				
				current = i-1
				len2 = 0
				while current in dict and dict[current] == False:
					
					dict[current] = True
					current -= 1
					len2 += 1
				
				longest = max(longest, len1+len2+1)
		
		return longest
		