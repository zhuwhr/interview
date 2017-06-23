[103. Binary Tree Zigzag Level Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)



```python
用一个boolean来控制正反
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        ans, level, zigzag = [], [root], True
        # while root and level to take the null root case
        while level:
            if zigzag:
                ans.append([node.val for node in level])
                zigzag = False
            else:
                ans.append(list(reversed([node.val for node in level])))
                zigzag = True
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return ans
```

## 