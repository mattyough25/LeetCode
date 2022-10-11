'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        noteLength = len(ransomNote)
        for iLet in range(noteLength):
            if ransomNote[iLet] in magazine:
                count1 = ransomNote.count(ransomNote[iLet])
                count2 = magazine.count(ransomNote[iLet])
                if count1 > count2:
                    return False
            else: 
                return False
        
        return True

# Test Cases
s1 = Solution()
ransomNote1 = "a"
magazine1 = "b"
out1 = s1.canConstruct(ransomNote1, magazine1)
print(out1)

s2 = Solution()
ransomNote2 = "aa"
magazine2 = "ab"
out2 = s2.canConstruct(ransomNote2, magazine2)
print(out2)

s3 = Solution()
ransomNote3 = "aa"
magazine3 = "aab"
out3 = s3.canConstruct(ransomNote3, magazine3)
print(out3)

s4 = Solution()
ransomNote4 = "chejaccdae"
magazine4 = "geceeibccchjejhdd"
out4 = s4.canConstruct(ransomNote4, magazine4)
print(out4)

