[49. Group Anagrams](https://leetcode.com/problems/anagrams/)

Idea: to sort every element(string) in the given strs input. After this, anagrams will be the same string. Use a dict, the key is the sorted string, value is the original string. The result would be the values of the dict.

```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.setdefault(key, []) + [w]
        return d.values()
```

To Notice:

1. not about this problem but the different between `d.get()` and `d.setdetault`is tricky. See this [post](http://stackoverflow.com/questions/7423428/python-dict-get-vs-setdefault).

