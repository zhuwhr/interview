[60. Permutation Sequence](https://leetcode.com/problems/permutation-sequence/)

这道题的本质是一道数学题，对训练算法意义不大，可以跳过了。

最直观的办法，可以把所有的排列都打印出来，选第k个，但是这样是O(n!)的复杂度，显然不是这个题想要的。需要用数学的方法算出第k个在哪个排列中，直接去找这个排列就可以了。参考这个[post](https://discuss.leetcode.com/topic/19269/share-my-python-solution-with-detailed-explanation)

```python
import math
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation
```

