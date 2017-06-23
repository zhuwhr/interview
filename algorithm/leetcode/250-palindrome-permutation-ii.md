[250. Palindrome Permutation II](https://leetcode.com/problems/palindrome-permutation-ii/)

Idea:

- Pre-process the string. Count appearance times of each char and get the element for half palindrome.
- Use elements to do normal string permutation and get the result. Add the single one to the middle if it exists.

注意：如果一个字符出现了奇数次，那么每一对要加到排列字符表中一次。比如 `aaa`, 那么a应该被加到排列字符表中一次，也应该被加到单独表中一次。

再就是字符串是不可变的，做排列的时候要注意。

```python
class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        permutation_elements = []
        single = []
        for c in s:
            dic[c] = dic.get(c,0) + 1
        for k, v in dic.items():
            if v % 2:
                while v > 1:
                    v -= 2
                    permutation_elements.append(k)
                single.append(k)
            else:
                while v > 0:
                    v -= 2
                    permutation_elements.append(k)
        if len(single) > 1:
            return []
        
        def dfs(string, index):
            if index == len(string):
                if single:
                    res.append(string + single[0] + ''.join(reversed(string)))
                else:
                    res.append(string + ''.join(reversed(string)))
                return
            prefix_set = set()
            for i in range(index, len(string)):
                if string[i] not in prefix_set:
                    prefix_set.add(string[i])
                    string = swap(string, index, i)
                    dfs(string, index+1)
                    string = swap(string, index, i)
        
        def swap(string, i, j):
            lst = list(string)
            lst[i], lst[j] = lst[j], lst[i]
            return ''.join(lst)
        
        res = []
        s = ''.join(permutation_elements)
        dfs(s, 0)
        return res
```

