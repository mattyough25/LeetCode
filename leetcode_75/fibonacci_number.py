'''
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:

0 <= n <= 30
'''

class Solution:
    def fib(self, n: int) -> int:

        def calcNext(num):
            temp = num[:]
            num[0] = temp[1]
            num[1] = temp[0] + temp[1]

            return num

        if n == 0:
            return 0
        elif n == 1:
            return 1

        f = [0, 1]
        for i in range(n - 1):
            sum = calcNext(f)

        return sum[1]

# Test Cases
s = Solution()
n = 0
out = s.fib(n)
print(out)

s = Solution()
n = 1
out = s.fib(n)
print(out)

s = Solution()
n = 2
out = s.fib(n)
print(out)

s = Solution()
n = 3
out = s.fib(n)
print(out)

s = Solution()
n = 4
out = s.fib(n)
print(out)

s = Solution()
n = 5
out = s.fib(n)
print(out)