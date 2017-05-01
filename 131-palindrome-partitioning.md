[131. Palindrome Partitioning](https://leetcode.com/problems/palindrome-partitioning/)

思路：循环从`start` 开始，从前往后找，当发现回文串时，递归下一层。

终止条件是`start` 正好落在回文串结束后的下一个位置，这时说明正好剩下的也是一个回文串。

```python
def partition(self, s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    def backtrack(temp, start):
        if start == len(s):
            res.append(list(temp))
            return
        for i in range(start, len(s)):
            if s[start:i+1] == s[start:i+1][::-1]:
                temp.append(s[start:i+1])
                backtrack(temp, i+1)
                temp.pop()
    res = []
    backtrack([], 0)
    return res
```
Analysis: 

Worst Case Exponential