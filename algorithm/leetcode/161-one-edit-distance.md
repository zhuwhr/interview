[161. One Edit Distance](https://leetcode.com/problems/one-edit-distance/)

首先，要弄明白，一步编辑的意思是，增，删，改。其次，增和删实质上是同一种操作，一定是增短的那个或者删长的那个。

这里有个小技巧，就是人为规定一下两个传进来的字符串哪个更长，如果不对，再重新调一遍这个函数，把参数对调一下就可以了。

现在我们假设 s 不长于 t，长度可以相等，或者更短。那么如果长度差距大于1了，肯定是不对的。另外一个情况就是两个字符串完全相等，也是不满足条件的。

现在开始判断两个字符串，循环的长度是可能更短的那个，也就是s。循环的过程就是要找两个字符串中不同的那个字符。当碰到不同的字符时，有两种情况：要么是替换一下，要么是可能更短的那个s，增加一个。如果是替换，就说明在这个不同字符之后的字符，两个串应该相等。如果是增加，就说明短串从这个字符开始，长串从这个字符的下一个开始，两个串相等。直接返回两个表达式就可以了

最后，如果一直都没找到不相等的，而前提条件是这两个字符串本身不相等，长度又差在1以内，说明一定是长串比短串长了1，满足条件，返回真。

```python
class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        if s == t or len(t) - len(s) > 1:
            return False
        for i in range(len(s)):
            if s[i] != t[i]:
                # replace or insertion
                return s[i+1:] == t[i+1:] or s[i:] == t[i+1:]
        return True
```



Time O(n) n is the length of s, Sapce O(1)

注意：

- 写的时候 return 写成这样的： `return s[i+1: len(s)] ==` 脑子抽了，其实完全没有必要写后面的index （len(s)）。还是对字符串的操作不够熟悉
- 如果写成上面那种样子，就要先判断 replace，再判断 insertion的情况，因为如果判断insertion，t会长出1来，如果写了结尾index，而事实上两个一样长，就会出IndexError: index out of range。这一点写的时候注意到了，说明慢慢地敏感了，不错