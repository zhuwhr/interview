[6. ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

what is zigzag [pattern](https://discuss.leetcode.com/topic/22925/if-you-are-confused-with-zigzag-pattern-come-and-see)

Idea: use a list of strings to hold each rows. Add chars to the list. If understanding the zigzag pattern, it is not hard to realize how to add chars to each row. The step should be either 1 or -1, this is to control the directions of moving.

```python
def convert(self, s, numRows):
    # corner case: 1 row or 1 column
    if numRows == 1 or numRows > len(s): return s
    
    L = [''] * numRows
    i, step = 0, 1
    for c in s:
        L[i] += c
        if i == 0 or i == numRows - 1:
            step = -step  # change direction
        i += step  # move towards direction
    return ''.join(L)
```



评论：

关键还是看能不能理解zigzag pattern，往下走和往上走的边界条件要清楚。当这个index到两头的时候，就该换方向了。