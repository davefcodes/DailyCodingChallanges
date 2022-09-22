class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        closedToOpen = {')':'(', '}':'{',']':'['}
        
        for p in s:
            if p in closedToOpen:
                if stack and stack[-1] == closedToOpen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False
                