[28. Implement strStr()](https://leetcode.com/problems/implement-strstr/)

life is short, use python

```python
# return haystack.find(needle)
```



in general:

相当于用一个长度为needle的窗口在haystack里面滑，时间复杂度其实是 O(mn), m, n are length of haystack and needle

这里python怎么实现的两个字符串的比较就不知道了，正常来说要扫一遍一个一个字符去比较的。

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
            return i
        return -1
        
        # return haystack.find(needle)
```



KMP, Robin Carp算法都可以优化。