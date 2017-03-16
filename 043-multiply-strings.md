[43. Multiply Strings](https://leetcode.com/problems/multiply-strings/)

idea is from [here](https://discuss.leetcode.com/topic/30508/easiest-java-solution-with-graph-explanation)

It is slightly different than the normal production we process. Here we do not use count, just use the index in the result.

` num1[i] * num2[j]` will be place at the index of result at `[i + j, i+j+1]`

在实际实现中，由于python的语言特质，我们可以反着循环这两个输入的数组，同样的结果也是反着出现的

```python
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # 可以不用处理这个case，后面单独处理
        # if num1 == '0' or num2 == '0': return '0'
        res = [0] * (len(num1) + len(num2))
        
        for i, c1 in enumerate(reversed(num1)):
            for j, c2 in enumerate(reversed(num2)):
                res[i+j] += int(c1) * int(c2)
                res[i+j+1] += res[i+j]/10
                res[i+j] %= 10
        
        # 处理开头的0
        while len(res) > 1 and res[-1] == 0: res.pop()
                
        return ''.join(map(str, res[::-1]))
                                            
```

Time: O(mn)

Space O(m + n)



收获：

1. 找syntax error往前找
2. 学会怎么反着循环
3. 熟用map方程