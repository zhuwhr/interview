[22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

[code ganker](http://blog.csdn.net/linhuanmars/article/details/19873463)

这道题其实是关于卡特兰数的，如果只是要输出结果有多少组，那么直接用卡特兰数的公式就可以。关于卡特兰数，请参见[卡特兰数-维基百科](http://zh.wikipedia.org/wiki/%E5%8D%A1%E5%A1%94%E5%85%B0%E6%95%B0)，里面有些常见的例子，这个概念还是比较重要的，因为很多问题的原型其实都是卡特兰数，大家可以看看。特别是其中

![img](http://img.blog.csdn.net/20140225022814250)

这个递推式的定义，很多这类问题都可以归结成这个表达式。这个题对于C的定义就是第一对括号中包含有几组括号。因为第一组括号中包含的括号对数量都不同，所以不会重复，接下来就是一个递归定义，里面又可以继续用更小的C去求组合可能性。

说完卡特兰数的内容，我们来看看这个具体问题怎么解决。一般来说是用递归的方法，因为可以归结为子问题去操作。在每次递归函数中记录左括号和右括号的剩余数量，然后有两种选择，一个是放一个左括号，另一种是放一个右括号。当然有一些否定条件，比如剩余的右括号不能比左括号少，或者左括号右括号数量都要大于0。正常结束条件是左右括号数量都为0。算法的复杂度是O(结果的数量)，因为卡特兰数并不是一个多项式量级的数字，所以算法也不是多项式复杂度的。



stepan神解法：

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right, parenthesis=[]):
            if left: 
                generate(p + '(', left-1, right)
            if right > left:
                generate(p + ')', left, right-1)
            if not right:
                parenthesis += p,
            return parenthesis
        
        return generate('', n, n)
```



