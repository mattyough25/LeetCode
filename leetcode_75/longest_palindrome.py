'''
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = dict()
        for i in range(len(s)):
            try:
                d[s[i]] = d[s[i]] + 1
            except:
                d.update({s[i]: 1})
        if len(d.keys()) == 1:
            return len(s)
        else:
            num_1 = list(d.values()).count(1)
            length = len(s) - (num_1 - 1)
        return length
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        dic ={}
        res = 0
        odd = False
        
        for i in s:
            dic.update({i:s.count(i)})
        
        for key,value in dic.items():
            if value%2==0:
                res += value
            else:
                res += value - 1
                odd = True
                
        if odd:
            return res+1
        else:
            return res

# Test Cases

s = Solution()
str = "abccccdd"
out = s.longestPalindrome(str)
print(out)

s = Solution()
str = "a"
out = s.longestPalindrome(str)
print(out)

s = Solution()
str = "abcdef"
out = s.longestPalindrome(str)
print(out)

s = Solution()
str = "bb"
out = s.longestPalindrome(str)
print(out)

s = Solution()
str = "bananas"
out = s.longestPalindrome(str)
print(out)
