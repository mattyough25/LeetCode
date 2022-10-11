'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

class Solution:
    def longestCommonPrefix(self, strs: str) -> str:
        min_word = min(strs, key=len)
        min_len = len(min(strs, key=len))
        
        for iList in range(len(strs)):
            for iPre in range(min_len):
                if min_word != strs[iList][0:len(min_word)]:
                    min_word = min_word[:-1]
                    continue
                if min_word not in strs[iList]:
                    min_word = min_word[:-1]

        return min_word

# Test Cases

s1 = Solution()
strs1 = ["flower","flow","flight"]
out1 = s1.longestCommonPrefix(strs1)
print(out1)

s2 = Solution()
strs2 = ["dog","racecar","car"]
out2 = s2.longestCommonPrefix(strs2)
print(out2)

s3 = Solution()
strs3 = ["reflower","flow","flight"]
out3 = s3.longestCommonPrefix(strs3)
print(out3)

s4 = Solution()
strs4 = ["aa","ab"]
out4 = s4.longestCommonPrefix(strs4)
print(out4)

