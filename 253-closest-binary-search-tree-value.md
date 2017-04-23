[253. Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value/)

```python
'''
idea: the result is either root's value or the cloest value in the correct subtree (recursive)

analysis:
Time: O(log n) we perform only constant operation in each tree level
Space: O(1) if iterative, O(log n) if recursive.
'''

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest = root.val
        while root:
            closest = root.val if abs(root.val - target) < abs(closest - target) else closest
            root = root.left if root.val > target else root.right
        return closest
        
        '''recursive
        # the result is either root's value or the cloest value in the correct subtree (recursive)
        a = root.val
        child = root.left if a > target else root.right
        if not child: return a
        b = self.closestValue(child, target)
        return a if abs(a - target) < abs(b - target) else b
        '''
```

