[256. Integer to English Words](https://leetcode.com/problems/integer-to-english-words/)

这个题有提示，根据提示来非常直观，难点在于各种边角情况的处理。首先，拿到一个数，根据读音规则，应该把数切成每三位一段。想办法把每三位一段的数读出来，每段内部的读法是一样的。然后读出来后，要在后面加上这段数的“千位级别”。

这里借鉴评论区一种写的非常清晰易懂的方法。（刷题就应该学习这种思路，而不是各种炫技的简短写法，这些写法虽然很牛，但是在面试中不好交流，容易挂。）这个方法首先把需要定义的字典都放到 `__init__` 里去了，然后用巧妙的方法循环千位级的数组，一个一个的加到后面。在帮助函数中，很好地用递归思想处理好了空格的问题，同时也能用除法和取余数的操作来有效切割数字串。

```python
class Solution(object):
    def __init__(self):
        self.lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        self.tens = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        self.thousands = ["","Thousand","Million","Billion"]
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        rst = ""
        
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                rst = self.helper(num % 1000) + self.thousands[i] + " " + rst
            num /= 1000
        
        return rst.strip()
        
    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num/10] + " " + self.helper(num%10)
        else:
            return self.lessThan20[num/100] + " Hundred " + self.helper(num%100)
```

O(n), n is the digits of the num



bug：

最关键地是想好怎么处理空格的问题，想清楚哪里该有空格，哪里不该有，最后的结果要去掉两头的空格。