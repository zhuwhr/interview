[151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)



See how powerful python is!

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])
```



