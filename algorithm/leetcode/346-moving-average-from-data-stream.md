[346-moving-average-from-data-stream](https://leetcode.com/problems/moving-average-from-data-stream/#/description)

```python
# using maxlen property of deque collection
class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.queue = collections.deque(maxlen=size)
    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        queue = self.queue
        queue.append(val)
        return float(sum(queue))/len(queue)
```

