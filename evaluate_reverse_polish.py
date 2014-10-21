class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                if i == "+":
                    result = n1 + n2
                elif i == "-":
                    result = n2 - n1
                elif i == "*":
                    result = n2 * n1
                else:
                    result = int(n2 * 1.0 / n1)
                stack.append(result)
        
        return stack[0]

