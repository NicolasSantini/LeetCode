from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        curr = 0
        operators = ['+', '-', '*', '/']
        first = True
        for t in tokens:
            if t in operators:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                match t:
                    case '+':
                        curr = num1 + num2
                    case '-':
                        curr = num1 - num2
                    case '*':
                        curr = num1 * num2
                    case '/':
                        curr = round(num1 / num2,1)
                stack.append(int(curr))
            else:
                stack.append(t)

        return int(stack.pop()) if stack else 0


sol = Solution()
#tokens = ["4","-2","/","2","-3","-","-"]
#tokens = ["2","1","+","3","*"]
#tokens = ["4","13","5","/","+"]
#tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
tokens = ["-78","-33","196","+","-19","-","115","+","-","-99","/","-18","8","*","-86","-","-","16","/","26","-14","-","-","47","-","101","-","163","*","143","-","0","-","171","+","120","*","-60","+","156","/","173","/","-24","11","+","21","/","*","44","*","180","70","-40","-","*","86","132","-84","+","*","-","38","/","/","21","28","/","+","83","/","-31","156","-","+","28","/","95","-","120","+","8","*","90","-","-94","*","-73","/","-62","/","93","*","196","-","-59","+","187","-","143","/","-79","-89","+","-"]
print(sol.evalRPN(tokens))
