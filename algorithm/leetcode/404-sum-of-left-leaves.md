[404-sum-of-left-leaves](https://leetcode.com/problems/sum-of-left-leaves/#/description)

标准的递归简单题，想清楚三个要素，一遍过。
关键点在于，递归时：既不需要左右孩子的值，也不需要返回值。需要的就是遍历，发现左叶子后计算就可以了。如果有左孩子，判断是不是叶子，是的话计算，不是的话继续往左走，最后统一返回往右走。

```python
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node):
            if not node: return;
            if node.left:
                if not node.left.left and not node.left.right:
                    left_leaves[0] += node.left.val
                else:
                    traverse(node.left)
            return traverse(node.right) 
        
        left_leaves = [0]
        traverse(root)
        return left_leaves[0]
```

