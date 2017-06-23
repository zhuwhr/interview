[17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

普通迭代思路：

很直观地来做，每一步把新增的字母一个一个的加进来，再把这一步的结果当成最后的结果，不断地更新。这个思路很直观，但是超时了，目前也没有想到什么改进的方法。

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return ''
        
        digit_map = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = ['']
        
        for d in digits:
            number = ord(d) - ord('0')
            letters = digit_map[number]
            temp = result
            for s in result:
                for l in letters:
                    temp.append(s.join(l))
            result = temp

        return result
```

Time: O(k ^ n), where n is the length of digits and each digit can represent k chars. Same space.

递归的思路：

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []
        
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
        if len(digits) == 1:
            return list(mapping[digits[0]])

        # recurse for the last step, with one letter off from right
        prev_rst = self.letterCombinations(digits[:-1])
        last_digit_letter = mapping[digits[-1]]
        
        # straight forward
        '''
        result = []
        print(prev_rst)
        for s in prev_rst:
            for c in last_digit_letter:
                result.append(s + c)

        return result
        '''
        # list comprehensions
        return [s+c for s in prev_rst for c in last_digit_letter]
```









这里还有个非常好的思路，来自高票答案：

用queue来实现。最核心的思想是“有多少个数字，结果中每个字符串就应该有多少个字母”。把所有的结果push进去，看队列的头一个的长度是不是等于输入的数字串里的位置 - 1，比如说我们已经处理到第三位数字了，那么结果队列中还有待处理的字符串长度就应该是2，因为前面已经处理过两位数字了。

但是leetcode python不允许 import deque，导致用 list 来当 queue 超时，非常遗憾。

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_map = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        result = ['']
        
        for i in range(0, len(digits)):
            number = ord(digits[i]) - ord('0')
            while(len(result[0]) == i):
                temp = result.pop()
                for ch in digit_map[number]:
                    result.insert(0, temp.join(ch))
        
        return result
```





这道题的小技巧：

不必要非得用dict，有时用个List就足够来找了，当index是连续数字的时候应该考虑用list。

bug:

python调递归时，不需要加self，只是在定义函数的时候加这个参数。self的概念需要再好好熟悉熟悉。

```python
def func(self, param):
    # do something
    func(param)
    # wrong: func(self, param)
```

