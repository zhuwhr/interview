[434-number-of-segments-in-a-string](https://leetcode.com/problems/number-of-segments-in-a-string/#/description)



正常数的话，碰到一个空格，它前面那个字符又不是空格，这就得算一个。corner case："hello" 这种情况下，如果 i == 0，也可以算一个。

```python
def countSegments(self, s):
    """
    :type s: str
    :rtype: int
    """
    # return len(s.split())
    rst = 0
    for i in range(len(s)):
        if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
            rst += 1
    return rst
```