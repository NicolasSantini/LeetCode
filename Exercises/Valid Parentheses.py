#time O(n) space O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        #creating two dict to understand if it's a opening ph or a closing one
        opening_p = {'(' : 1, '[' : 2, '{' : 3}
        closing_p = {')' : 1, ']' : 2, '}' : 3}
        #stack su cui aggiungere le parentesi in ordine tenendo conto della FIFO
        stack = []
        #iteration on every element of the list
        for c in s:
            if c in opening_p:
                stack.append(c)
            elif c in closing_p:
                if len(stack) != 0:
                    val = stack.pop()
                    if  opening_p[val] == closing_p[c]:
                        continue
                    else:
                        return False
                else:
                    return False

        return True if len(stack) == 0 else False



