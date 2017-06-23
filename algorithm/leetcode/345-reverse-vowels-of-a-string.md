[345-reverse-vowels-of-a-string](https://leetcode.com/problems/reverse-vowels-of-a-string/#/description)



两个指针从前往后走，当共同碰到元音时，交换。如果没有共同碰到，哪个没碰到就动哪个，碰到的不动。这里注意是大小写都要放到元音集合里。

```python
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) == 0: return s;
        
        l = list(s)
        left, right = 0, len(l) - 1
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        while (left < right):
            if l[left] in vowels and l[right] in vowels:
                # 大小写也不换的情况： if l[left].lower() != l[right].lower():
                l[left], l[right] = l[right], l[left]
                left += 1
                right -= 1
            if l[left] not in vowels: left += 1
            if l[right] not in vowels: right -= 1
            
        return ''.join(l)
```

时间复杂度 O(n)



大神：

```python
def reverseVowels(self, s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
```

