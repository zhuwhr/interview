[383-ransom-note](https://leetcode.com/problems/ransom-note/#/description)

非常直观的一道题。一开始我的想法是，把两个字符串里面的字符都存到一个map中，然后比较这个map里面的值的数字大小。后来看讨论受到启发，这个题只有26个小写字母，用一个list就来存频次就够了。

后面有简单的，用`all(), str.count()` 来解题的方法。

```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        frequency = [0] * 26
        for c in magazine:
            frequency[ord(c) - ord('a')] += 1
        
        for s in ransomNote:
            frequency[ord(s) - ord('a')] -= 1
            if frequency[ord(s) - ord('a')] < 0:
                return False
        
        return True
        
        '''
        all(), str.count()
        return all(ransomNote.count(c) <= magazine.count(c) for c in ransomNote)
        
        make it faster with a set
        return all(ransomNote.count(c)<=magazine.count(c) for c in set(ransomNote))
        '''
```

时间复杂度 O(n)  n is the larger number of size magazine and note.

Space O(26) a list