[145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

```python
# recursion
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def DFS(node):
            if node:
                DFS(node.left)
                DFS(node.right)
                result.append(node.val)
        result = []
        DFS(root)
        return result
# reverse way of doing pre-order, but add right (instead of left node) to the top of the stack, and return reverse order result.
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack += node.left, node.right
        return list(reversed(result))
```

### 