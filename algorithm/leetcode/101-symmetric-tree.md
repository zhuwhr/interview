[101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

iterative:

level order traversal, use a queue to enqueue and dequeue nodes, in each level, use the size to control a level, and use a list to store the node's val, then decide if it is symmetric. 

```python
        if not root: return True
        q = deque()
        q.append(root)
        level = []
        
        while q:
            level_size = len(q)
            while level_size > 0:
                node = q.popleft()
                if node.left: 
                    level.append(node.left.val)
                    q.append(node.left)
                else:
                    level.append(None)
                if node.right:
                    level.append(node.right.val)
                    q.append(node.right)
                else:
                    level.append(None)
                level_size -= 1
            if level != level[::-1]: return False
            level = []
        
        return True
```



recursive:

This is different from deciding if two trees are identical. Here we have only one tree, so we need the helper function since we have to see if left subtree and right subtree are identical.

```python
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # recursive
        return not root or self.helper(root.left, root.right)
    
    def helper(self, n1, n2):
        if not n1 and not n2: return True
        if not n1 or not n2: return False
        #trick: if not n1 or not n2: return n1 == n2
        if n1.val != n2.val: return False
        return self.helper(n1.left, n2.right) and self.helper(n1.right, n2.left)
```

