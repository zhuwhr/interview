[501-find-a-mode-in-BST](https://leetcode.com/problems/find-mode-in-binary-search-tree/#/description)

```python
'''
idea: # easy to do with extra space, hard to do within O(1), here is easy one. But it does not use anything specialty in BST.
'''
def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        count = {}       
        def traverse(node):
            if node:
                count[node.val] = count.get(node.val, 0) + 1
                traverse(node.left)
                traverse(node.right)
        if not root: return []
        traverse(root)
        mode = max(count.values())
        return [k for k,v in count.items() if v == mode]
```

