[38. Count and Say](https://leetcode.com/problems/count-and-say/)

What is [count and say](https://discuss.leetcode.com/topic/2264/examples-of-nth-sequence)?

这个题主要就是理解了count and say是干什么的，然后一步步的数下来就可以了。

第n个结果是数第 n - 1 个序列得到的，所以一共要数 n - 1 遍。每数一遍，都要更新一下result这个变量，result实际上存的是每数一遍过后的结果。要求 Nth，实际上result 存过了 1，2，3.。。 n - 1 步的结果。需要注意的就是，每遍数完后，要把最后一个字母也加上。

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = '1'
        for _ in range(n - 1):
            temp = []
            count = 1
            for i in range(1, len(result)):
                if result[i] == result[i-1]:
                    count += 1
                else:
                    temp.append(str(count))
                    temp.append(result[i-1])
                    count = 1
            # 这里就是注意把最后一个字母加上！
            temp.append(str(count))
            temp.append(result[-1])
            result = ''.join(temp)
        return result;
```

时间复杂度是O(n*串的长度)，空间复杂度是O(串的长度)