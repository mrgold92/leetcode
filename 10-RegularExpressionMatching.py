"""
Given an input string s and patter p, implement regular expression matching with support for '.' and '*'. where:
'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:
Input: s = "aab", p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 2]
                    if self.matches(s, p, i, j - 1):
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    if self.matches(s, p, i, j):
                        dp[i][j] = dp[i - 1][j - 1]
        return dp[m][n]
    
    def matches(self, s, p, i, j):
        if i == 0:
            return False
        if p[j - 1] == ".":
            return True
        return s[i - 1] == p[j - 1]
        
if __name__ == "__main__":
    s = "aab"
    p = "c*a*b"
    print(Solution().isMatch(s, p))