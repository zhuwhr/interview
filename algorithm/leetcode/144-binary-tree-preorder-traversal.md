[144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)

```python
# recursion
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def DFS(node):
            if node:
                result.append(node.val)
                DFS(node.left)
                DFS(node.right)
        result = []
        DFS(root)
        return result
# iteration
class Solution(object):
    def preorderTraversal(self, root):
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
                stack += node.right, node.left
        return result
# iteration with stack only stores right node
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # iteration with stack only store right node
        right_nodes = []
        result = []
        while root:
            result.append(root.val)
            if root.right:
                right_nodes.append(root.right)
            root = root.left
            if not root and right_nodes:
                root = right_nodes.pop()
        
        return result
```