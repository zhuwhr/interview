[14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)

评论：

最直观的方法，把第一个字符串当prefix，然后一个一个往下找。如果没匹配，就把这个公共子串缩小，缩到匹配为止。

这里有一个小优化 `s.startswith(prefix, 0, len(prefix))` 加上`start` `end` 这两个参数后，搜索时只搜这么长。这个优化把速度提高了20ms，从30%提高到90%多

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: return ''
        
        prefix = strs[0]
        for s in strs:
            if s.startswith(prefix):
                continue
            else:
                while not s.startswith(prefix, 0, len(prefix)):
                    prefix = prefix[0:len(prefix)-1]
                    
        return prefix
```

时间复杂度 O(n + k)，n 是 strs 的长度， k是第一个字符串的长度，也是最大可能的长度。（其实这个题是不是可以先扫一遍，找出最短的那个字符，这样会不会快一点）最好情况下，一匹配到底，就相当于把列表过了一遍。最坏情况下，k 被一个个地减掉，总共用时 O(k) 的时间。

