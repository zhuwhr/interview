[58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/)



naive solution:

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        l = s.split()
        return len(l[-1]) if l else 0
```

Notice the use of `split()`

`'1,2,3,'.split(',') -> ['1', '2', '3', '']`
**注意后面还有一个空字符**



```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        rst = 0
        for c in s:
            if c != ' ':
                rst += 1
            else:
                rst = 0
        
        return rst
```

