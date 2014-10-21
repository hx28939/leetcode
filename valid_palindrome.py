class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) == 0:
            return True
        else:
        	news = ''
        	for i in s:
        		if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z' or i >= '0' and i <= '9':
        			news += i
        	if len(news)<=1:
        		return True
        	else:
        		middle_p = int((len(news) -1)/2)
        		news.lower()
        		ss = True
        		for j in range(0,middle_p):
        			if news[j] != news[-j-1]:
        				ss = False
        		return ss