[165. Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/)



首先把两个输入的版本号以 '.' 分开，这时的输入变成了两个 list of strings，每个string代表一个版本数。（注意 int (str))  然后开始循环两个列表，应该以两边最大值为界，如果index比长度长了，就返回0。这样比较的话，在每一层里都会判断一次两个数的差值，发现不同就立即返回了。遇到一些特例时，如 `1.1.0.0.0  vs 1.1` 这种的，会把0都比较完，最后再返回相等。

```python
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        l1 = version1.split('.')
        l2 = version2.split('.')
        
        for i in range(max(len(l1), len(l2))):
            diff = (int(l1[i]) if i < len(l1) else 0) - (int(l2[i]) if i < len(l2) else 0)
            if diff != 0:
                return 1 if diff > 0 else -1
                
        return 0
```

