[450-delete-node-in-bst](https://leetcode.com/problems/delete-node-in-a-bst/#/description)

```python
'''
idea:
1、find this node, straight forward
2、do something on this node: there are 4 conditions:
   	no l and r child
	l child only
    r child only
    both l and r child
First three is straitforward. If the node has both l and r child, we need to find the min val of it's right sub tree, and substitude the node's val with this min val, and delete the min node recursively.

key point:
1. When calling recursive function, be sure to catch the return value and point root's children to the value
2. Delete the min node recursively.

Analysis:
Time: O(log n) because we only perform constant operation in each tree level
'''
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            root.val = self.findMin(root.right)
            root.right = self.deleteNode(root.right, root.val)
        return root
    
    def findMin(self, root):
        if not root: return None
        while root.left:
            root = root.left
        return root.val
```

