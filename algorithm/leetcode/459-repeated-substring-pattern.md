[459-repeated-substring-pattern](https://leetcode.com/problems/repeated-substring-pattern/#/description)

从前往后扫输入的字符串，如果找到哪一个字符和首字符相等，说明这有可能是重复子串的开始。想要返回真还有两个条件，输入字符串的长度能被子串整除，the number of substring in the stirng should equal to the length of string divided by the length of substring:



```python
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        
        for i in range(1, len(s)):
            if s[i] == s[0] and len(s) % i == 0 and s.count(s[:i]) == len(s) / i:
                return True
```

神解法看[这里](https://discuss.leetcode.com/topic/68206/easy-python-solution-with-explaination)，不理解怎么证明的，但看起来很厉害

`return s in (s + s)[1:-1]`

