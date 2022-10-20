'''
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        if len(s) == 0:
            return 0
        for iStr in range(len(s)):
            if iStr == 0:
                temp = list(s[iStr])
            else:
                temp.append(s[iStr])
            for iTemp in range(len(temp)):
                try:
                    if s[iStr+1] in temp:
                        if len(temp) >= count:
                            count = len(temp)
                            temp.clear()
                except:
                    if s[iStr] in temp:
                        if len(temp) >= count:
                            count = len(temp)
                            temp.clear()
                    return count
'''
class Solution():
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Base condition
        if s == "":
            return 0
        # Starting index of window
        start = 0
        # Ending index of window
        end = 0
        # Maximum length of substring without repeating characters
        maxLength = 0
        # Set to store unique characters
        unique_characters = set()
        # Loop for each character in the string
        while end < len(s):
            if s[end] not in unique_characters:
                unique_characters.add(s[end])
                end += 1
                maxLength = max(maxLength, len(unique_characters))
            else:
                unique_characters.remove(s[start])
                start += 1
        return maxLength

# Test Cases
s = Solution()
str = "abcabcbb"
out = s.lengthOfLongestSubstring(str)
print(out)

s = Solution()
str = "bbbbb"
out = s.lengthOfLongestSubstring(str)
print(out)

s = Solution()
str = "pwwkew"
out = s.lengthOfLongestSubstring(str)
print(out)

s = Solution()
str = ""
out = s.lengthOfLongestSubstring(str)
print(out)

s = Solution()
str = " "
out = s.lengthOfLongestSubstring(str)
print(out)

s = Solution()
str = "au"
out = s.lengthOfLongestSubstring(str)
print(out)

s = Solution()
str = "aab"
out = s.lengthOfLongestSubstring(str)
print(out)