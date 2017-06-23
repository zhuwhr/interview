[340-longest-substring-with-as-most-k-distinct-characters](https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/#/description)



```python
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        distinct = {}  # char: pos
        max_len = 0
        slow = 0
        
        for fast in range(0, len(s)):
            if len(distinct) == k and s[fast] not in distinct:
                slow = min(distinct.values()) + 1
                self.remove_lowest_element(distinct)
            distinct[s[fast]] = fast
            max_len = max(max_len, fast - slow + 1)
        return max_len
    
    def remove_lowest_element(self, distinct):
        lowest_pos = min(distinct.values())
        for k, pos in distinct.items():
            if pos == lowest_pos:
                char = k
        distinct.pop(char)
```

