[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)

核心思想：

每新加一个字母，回文串的长度会增长1或者2。1的情况是 `aaaaaa + a` 2的情况是` abc + b` 。这个道理在所有回文串的题目中都非常有用。

知道了上面那个道理，题目就变得简单了。扫一遍字符串，用一个变量 `max` 记录当前回文串最大长度，每走到一个字母时，检查它之前 ` max or max + 1` 长度的子串是不是回文串。这里就是上面说的，是加1还是加2呢。如果是加1，那么该字符和它之前 `max` 个字符组成的子串也是回文串，此时把 `max ` 再加1，记录下新的最长回文串长度。如果是加2， 那么该字符和它之前的 `max + 1` 个字符组成的子串也是回文串，此时把 ` max ` 再加2，记录下新的最长回文串的长度。

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0: return 0
        max_len = 1
        start = 0
        
        for i in range(len(s)):
            # 这里的检查条件是确保index不向左出界（在一开始的时候）
            # 回文串长度加1的情况
            if i - max_len >= 0 and s[i - max_len : i + 1] == s[i - max_len : i + 1][::-1]:
                start = i - max_len
                max_len += 1
                continue # 为了跑得更快，要么加1，要么加2.加了1就不会加2了
            # 回文串长度加2的情况
            if i - max_len - 1 >= 0 and s[i - max_len - 1 : i + 1] == s[i - max_len - 1 : i + 1][::-1]:
                start = i - max_len - 1
                max_len += 2
                
        return s[start:start+max_len]   
```

时间复杂度是伪 O(n)，因为总共只是对着字符串扫了一遍，但是`[::1]` 这里对字符对象进行了一个复制，不是 `O(1)`

bug:

 ` start = i - max_len` & ` max_len += 1` 写反了。其实这里道理很显而易见，但是写的时候没多想就随意写了。今后还是应该想清楚，一步是一步的写，