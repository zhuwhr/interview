[563-binary-tree-tilt](https://leetcode.com/problems/binary-tree-tilt/#/description)

```python
标准的递归简单题，想清楚三个要素，一遍过。
关键点是在节点中怎么处理，递归传的值是 sum ，在节点上要算的值是 tilt, 最后把tilt数组加起来
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def findSum(node):
            if not node: return 0
            left = findSum(node.left)
            right = findSum(node.right)
            tilt.append(abs(left - right))
            return left + right + node.val
        
        tilt = []
        findSum(root)
        return sum(tilt)
```

