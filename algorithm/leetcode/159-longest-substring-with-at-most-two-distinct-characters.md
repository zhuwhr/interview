[159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)

评论：

这个题也是快慢指针，快指针一直往前走，当碰到限制条件时（三个不同的字母了），把最小pos所放的那个元素删掉，慢指针在此基础上加一。这里和第三题找最长独立子字符串的变化是，dict里存的不再是 字符的数量， 而是字符的最高位置。

这样做方便了删除操作，如果还存字符数量的话，那么需要一个一个往前找着删，直到把某个字符删光为止。事实上我们想一下，当遇到限止条件时，我们删除的目标是删掉一个distinct的字符，以减少子字符串中distinct字符的数量。这个时候最好的办法就是找出那个位置最低的字符然后删掉它。

```python
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        # key: char, value: highest pos
        distinct = {}  
        max_len = 0
        slow = 0
        
        for fast in range(0, len(s)):
            if len(distinct) == 2 and s[fast] not in distinct:
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



一个错误的例子：

用set来做，快指针一直走一直加，当len(set) > 3的时候，开始从慢指针处往回删。这种做法是错误的，出个bug调了半天。因为从set里删掉一个元素后，set的size变小了一个，但实际上快慢指针之间还是可能有刚才被删过的元素。所以这个题用set是不对的，还是要用dict。鉴于dict比set范围更广，以后这种题全用dict得了。下午都栽在这个set上了！

