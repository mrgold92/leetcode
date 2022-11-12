"""
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:
Input: s = "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        max_len = 1
        res = s[0]
        for i in range(len(s)):
            odd = self.center_spread(s, i, i)
            even = self.center_spread(s, i, i+1)
            max_len = max(max_len, odd, even)
            if max_len > len(res):
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
                res = s[start:end+1]
        return res

    def center_spread(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1
    
if __name__ == "__main__":
    s = "babad"
    print(Solution().longestPalindrome(s))