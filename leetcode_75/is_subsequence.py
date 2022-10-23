'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?
'''
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        ix = 0
        length = len(t_list)
        while length > len(s_list):
            try:
                if t_list[ix] not in s_list:
                    t_list.remove(t_list[ix])
                    length = len(t_list)
                    ix -= 1
                ix += 1
            except:
                break

        if s_list == t_list:
            return True
        else:
            return False
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(s == t):
            return True
        else:
            temp=''
            cou=0
            for i in range(len(t)):
                if(cou < len(s)):
                    if(s != "" and s[cou] == t[i]):
                        temp+=t[i]
                        cou+=1
            if(temp == s):
                return True
            else:
                return False

# Test Cases

s = Solution()
string = "abc"
t = "ahbgdc"
out = s.isSubsequence(string,t)
print(out)

# Test Cases
s = Solution()
string = "axc"
t = "ahbgdc"
out = s.isSubsequence(string,t)
print(out)

# Test Cases
s = Solution()
string = "aec"
t = "abcde"
out = s.isSubsequence(string,t)
print(out)

# Test Cases
s = Solution()
string = "rjufvjafbxnbgriwgokdgqdqewn"
t = "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq"
out = s.isSubsequence(string,t)
print(out)

s = Solution()
string = "ab"
t = "baab"
out = s.isSubsequence(string,t)
print(out)

