[94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

```python
# recursion
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def DFS(node):
            if node:
                DFS(node.left)
                result.append(node.val)
                DFS(node.right)
        result = []
        DFS(root)
        return result

# iteration: 树的遍历一定要走到空，压stack的时候想清楚怎么处理空，当压进去的东西物理意义不一样的时候，要利用好cur指针    
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right
        return result
```
