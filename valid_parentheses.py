'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
''' My Solution
class Solution:
    def isValid(self, s: str) -> bool:
        bValid = False

        par_open = [i for i in range(len(s)) if s.startswith('(', i)]
        par_close = [i for i in range(len(s)) if s.startswith(')', i)]
        if len(par_open) != len(par_close):
            return False
        elif len(par_open) == 1:
            if par_open[0] > par_close[0]:
                return False
            else:
                bValid = True
        else:
            for iPar in range(len(par_open)):
                try:
                    if par_open[iPar + 1] < par_close[iPar]:
                        return False
                    else:
                        bValid = True
                except:
                    break

        brack_open = [i for i in range(len(s)) if s.startswith('[', i)]
        brack_close = [i for i in range(len(s)) if s.startswith(']', i)]
        if len(brack_open) != len(brack_close):
            return False
        elif len(brack_open) == 1:
            if brack_open[0] > brack_close[0]:
                return False
            else:
                bValid = True
        else:
            for iBrack in range(len(brack_open)):
                try:
                    if par_open[iBrack + 1] < par_close[iBrack]:
                        return False
                    else:
                        bValid = True
                except:
                    break
        
        cur_open = [i for i in range(len(s)) if s.startswith('{', i)]
        cur_close = [i for i in range(len(s)) if s.startswith('}', i)]
        if len(cur_open) != len(cur_close):
            return False
        elif len(cur_open) == 1:
            if cur_open[0] > cur_close[0]:
                return False
            else:
                bValid = True
        else:
            for iCur in range(len(cur_open)):
                try:
                    if cur_open[iCur + 1] < cur_close[iCur]:
                        return False
                    else:
                        bValid = True
                except:
                    break
        
        return bValid
'''
class Solution:
    def isValid(self, s: str) -> bool:
        # Stack for left symbols
        leftSymbols = []
        # Loop for each character of the string
        for c in s:
            # If left symbol is encountered
            if c in ['(', '{', '[']:
                leftSymbols.append(c)
            # If right symbol is encountered
            elif c == ')' and len(leftSymbols) != 0 and leftSymbols[-1] == '(':
                leftSymbols.pop()
            elif c == '}' and len(leftSymbols) != 0 and leftSymbols[-1] == '{':
                leftSymbols.pop()
            elif c == ']' and len(leftSymbols) != 0 and leftSymbols[-1] == '[':
                leftSymbols.pop()
            # If none of the valid symbols is encountered
            else:
                return False
        return leftSymbols == []

# Test Cases

s1 = Solution()
par1 = "()"
out1 = s1.isValid(par1)
print(out1)
'''
s2 = Solution()
par2 = "()[]{}"
out2 = s2.isValid(par2)
print(out2)

s3 = Solution()
par3 = "(]"
out3 = s3.isValid(par3)
print(out3)

s4 = Solution()
par4 = "({})()"
out4 = s4.isValid(par4)
print(out4)
'''