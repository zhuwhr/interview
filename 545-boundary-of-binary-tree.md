[545-boundary-of-binary-tree](https://leetcode.com/problems/boundary-of-binary-tree/#/description)



```python
最直观的方式，自己写出来的AC，O(3n)，目前也没有看到更好的优化
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def findLeft(node):
            if not node: return
            if node.left:
                left.append(node.left.val)
                findLeft(node.left)
            elif node.right:
                left.append(node.right.val)
                findLeft(node.right)
        
        def findRight(node):
            if not node: return
            if node.right:
                right.append(node.right.val)
                findRight(node.right)
            elif node.left:
                right.append(node.left.val)
                findRight(node.left)
        
        def findLeaves(node):
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.left:
                findLeaves(node.left)
            if node.right:
                findLeaves(node.right)

        left = []
        right = []
        leaves = []
        
        if not root: return []
        if not root.left and not root.right:
            return [root.val]
        if root.left:
            left = [root.left.val]
            findLeft(root.left)
        if root.right:
            right = [root.right.val]
            findRight(root.right)
        findLeaves(root)
        if left:
            leaves.pop(0)
        if right:
            leaves.pop()
        return [root.val] + left + leaves + list(reversed(right))
        
```

