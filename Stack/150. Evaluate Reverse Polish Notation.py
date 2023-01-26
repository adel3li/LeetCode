class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for o in tokens :
            if o == '+' :
                stack.append(stack.pop() + stack.pop())
            elif o == '-' :
                a, b = stack.pop(), stack.pop()
                stack.append(b - a) 
            elif o == '*' :
                stack.append(stack.pop() * stack.pop())
            elif o == '/' :
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else :
                stack.append(int(o))
        return stack[0]
            
#another solution

class Solution:
    def evalRPN(self, t: List[str]) -> int:
        a = ['+', '-', '*', '/']
        s = []
        for i in t:
            if i not in a:
                s.append(int(i))
            else:
                d, h = s.pop(), s.pop()
                if i == '+':
                    s.append(h + d)
                elif i == '-':
                    s.append(h - d)
                elif i == '*':
                    s.append(h * d)
                else:
                    s.append(int(h / d))
        return s[0]
