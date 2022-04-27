'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

- input: ["flower","flow","flight"]
- output: "fl"

Example 2:

- input: ["dog","racecar","car"]
- output: ""

Constrains:

- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lower-case English letters.
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
        return prefix


if __name__ == '__main__':
  sol = Solution()
  print(sol.longestCommonPrefix(["flower","flow","flight"]))
  print(sol.longestCommonPrefix(["dog","racecar","car"]))
  