[8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)

idea: there are following cases to handle:

1. empty
2. redundant spaces
3. sign
4. invalid input, non-digit chars
5. out of bound



```python
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        # handle empty input
        if len(str) == 0: return 0;
        
        # leading and trailing spaces
        l = list(str.strip()) 
        
        # handle sign
        sign = -1 if l[0] == '-' else 1
        if l[0] in ['-','+']: del l[0]
        
        
        rst, i = 0, 0
        # invaild input: isdigit()
        # out of bound: max, min
        while i < len(l) and l[i].isdigit():
            rst = rst*10 + ord(l[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * rst, 2**31-1))
```

To Notice:

1. May also use RegEX to handle invalid input like this `str = re.findall('(^[\+\-0]*\d+)\D*', str)`
   Need to review RegEX

评论：

这个题挺无聊的，即使算是基本功，也真的挺无聊的