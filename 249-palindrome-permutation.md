[249. Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/)

Count the number of chars in the string. If it can form a palindrome, it should have at most 1 odd chars.

```python
class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {}
        count_odd = 0
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        for v in dic.values():
            if v % 2:
                count_odd += 1
        return count_odd < 2
```

