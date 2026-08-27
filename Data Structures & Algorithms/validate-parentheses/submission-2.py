class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        matching = { 
            
            ")" : "(", 
            "}" : "{", 
            "]" : "["
                
         }
        
        for c in s:
            if c in ["(", "{", "["]:
                stack.append(c)
            
            elif not stack:
                return False
                
            elif stack[-1] != matching[c]:
                return False

            else:
                stack.pop()

            
        return not stack
