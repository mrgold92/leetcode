'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backwards as forwards.

For example:
  - 121 is a palindrome while 123 is not.

Example 1:
  Input: x = 121
  Output: true
  Explanation: From left to right, it reads 121. From right to left, it becomes 121.

Example 2:
  Input: x = -121
  Output: false
  Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''

class Solution(object):
  def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0:
      return False
    else:
      x = str(x)
      if x == x[::-1]:
        return True
      else:
        return False


if __name__ == '__main__':
  sol = Solution()
  print(sol.isPalindrome(121))
  print(sol.isPalindrome(-121))
  print(sol.isPalindrome(10))
  print(sol.isPalindrome(989))