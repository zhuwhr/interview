[216. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

```python
# key point: when adding a new element, add all other element one by one in reverse order
class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        # O(n), when adding a new element, add all other element one by one in reverse order
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.pop(0))
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q.pop(0)
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.q[0]
    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.q) == 0
```

