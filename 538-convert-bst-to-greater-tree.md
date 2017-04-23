[538-convert-bst-to-greater-tree](https://leetcode.com/problems/convert-bst-to-greater-tree/#/description)

```python
'''
idea: 
1. traverse the BST to get the sum of all nodes
2. inorder traverse the BST to add the sum to each node

key point:
Inorder traversal of a BST is an increasing sorted array
For each node, we need to add the sum of all values that is larger, meaning the sum of all elements in the elements behind itself in the sorted array. Use a global sum to keep track the sum value.

'''
def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        sum = [0]
        
        def traverse(node):
            if node:
                sum[0] += node.val
                traverse(node.left)
                traverse(node.right)
        
        def convert(node):
            if node:
                convert(node.left)
                sum[0] -= node.val
                node.val += sum[0]
                convert(node.right)
        
        traverse(root)
        convert(root)
        return root
```

