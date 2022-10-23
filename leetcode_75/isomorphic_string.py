'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_unique = list()
        t_unique = list()
        for i in range(len(s)):
            s_unique.append(s.index(s[i]))
            t_unique.append(t.index(t[i]))

        if s_unique == t_unique:
            return True
        else:
            return False

# Test Cases

s = Solution()
string = "egg"
t = "add"
out = s.isIsomorphic(string,t)
print(out)

s = Solution()
string = "foo"
t = "bar"
out = s.isIsomorphic(string,t)
print(out)

s = Solution()
string = "paper"
t = "title"
out = s.isIsomorphic(string,t)
print(out)

s = Solution()
string = "bbbaaaba"
t = "aaabbbba"
out = s.isIsomorphic(string,t)
print(out)
