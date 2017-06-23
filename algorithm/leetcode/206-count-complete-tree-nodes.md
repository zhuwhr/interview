[206. Count Complete Tree Nodes](https://leetcode.com/problems/count-complete-tree-nodes/)

```python
这个题的难点在于最后一层不一定是满的
基本思路是把树的最左边的高度和最右边的高度算出来，如果相等说明是一棵完全树，返回 2^h - 1即可。如果不相等，说明在最底层的某个地方没有填满，这时可以递归往左右孩子走，直到发现不满的那一个为止

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getLeftHeight(node):
            depth = 0
            while node:
                node = node.left
                depth += 1
            return depth
        
        def getRightHeight(node):
            depth = 0
            while node:
                node = node.right
                depth += 1
            return depth
        
        left_height = getLeftHeight(root)
        right_height = getRightHeight(root)
        
        if left_height == right_height:
            return (1 << left_height) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1
```

