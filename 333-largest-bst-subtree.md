[333-largest-bst-subtree](https://leetcode.com/problems/largest-bst-subtree/#/description)

```python
'''
idea: 
1. min, max value allowed of current bst.
2. Calculate the current largest number of nodes, use '-inf' to represent the invalid. When adding, '-inf' will make all node in the subtree '-inf'
3. Calculate the max value of bst subtree. Again, invalid will be always -inf and will not be considered in max function.
DFS function returns: max(result), current node's largest # of nodes in bst, min/max of subtree

key point: use '-inf' to represent invalid bst
'''
def largestBSTSubtree(self, root):
    """
        :type root: TreeNode
        :rtype: int
    """
    def dfs(node):
        if not node:
            return 0, 0, float('inf'), float('-inf')
        N1, n1, min1, max1 = dfs(node.left)
        N2, n2, min2, max2 = dfs(node.right)
        n = n1 + n2 + 1 if max1 < node.val < min2 else float('-inf')
        return max(N1, N2, n), n, min(min1, node.val), max(max2, node.val)
    return dfs(root)[0]
```

