[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

非常直观，用stack

```python
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0: return True
        stack = []
        dict = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if len(stack) == 0 or dict.get(char, '') != stack[-1]:
                stack.append(char)
            else:
                stack.pop()
                
        return len(stack) == 0
```



bug:

用dict[]一定要注意查列表里有没有关键字。python里没有的话就 KeyError了，不像JS里返回一个 undifined。这里用`dict.get(char, default)` 来避免这个错误。