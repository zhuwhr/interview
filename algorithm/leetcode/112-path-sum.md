[112. Path Sum](https://leetcode.com/problems/path-sum/)

从根到叶，存不存在一个目标

```python
从根到叶，判断存在，不要路径，不用保存节点
判断存在：一层层往下减，到叶子节点再判断正误
def hasPathSum(self, root, sum):
    """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
    if not root: return False
    if not root.left and not root.right and root.val == sum:
        return True
    sum -= root.val
    return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum) 
```



#### 