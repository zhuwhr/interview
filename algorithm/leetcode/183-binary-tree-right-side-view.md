[183. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

```python
这个题就是一个level order，把每个level最右边的加到view里去，注意加的是值不是节点。O(n) 时间复杂度
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        view = []
        if not root: return view
        level = [root]
        while level:
            view.append(level[-1].val)
            temp = []
            for node in level:
                if node.left: temp.append(node.left)
                if node.right: temp.append(node.right)
            level = temp
        return view
```

