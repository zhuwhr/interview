[98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

```python
用一个帮助函数，传参数的时候挂一个最大最小值传下去，判断条件是>=max or <= min，就返回错误
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def validation(node, min, max):
            if not node: return True
            if node.val <= min or node.val >= max:
                return False
            return validation(node.left, min, node.val) and validation(node.right, node.val, max)
        
        return validation(root, float('-inf'), float('inf'))
```

