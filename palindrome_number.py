'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
'''
import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_string = str(x)
        if x_string[0] == "-":
            return False
        for iString in range(math.floor(len(x_string)/2)):
            if x_string[iString] != x_string[-(iString+1)]:
                return False

        return True
# Test Cases

s1 = Solution()
x1 = 121
print(s1.isPalindrome(x1))

s2 = Solution()
x2 = -121
print(s2.isPalindrome(x2))

s3 = Solution()
x3 = 10
print(s3.isPalindrome(x3))
