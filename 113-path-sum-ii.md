[113. Path Sum II](https://leetcode.com/problems/path-sum-ii/)

从根到叶，存不存在一个目标，并打印路径（需要保存节点了）



```python
def pathSum(self, root, sum):
    """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
    path = []
    result = []
    def helper(node, sum, path, result):
        if not node: return;
        path.append(node.val)
        if not node.left and not node.right and node.val == sum:
            result.append(list(path))
            path.pop()
            return
        else:
            helper(node.left, sum - node.val, path, result)
            helper(node.right, sum - node.val, path, result)
        path.pop()

    helper(root, sum, path, result)
    return result
```

这个题，因为第13行没加list，使得result里面的path跟着边了，最后返回空，搞了一下午这个bug。

还犯了一个错误，没想好在哪里加叶子节点，应该先加再判断啊：

```python
def pathSum(root, sum):
    path = []
    result = []
    def helper(node, sum, path, result):
        if not node: return;
        if not node.left and not node.right and node.val == sum:
            result.append(path)
            return;
        sum -= node.val
        path.append(node.val)
        print(path, sum)
        helper(node.left, sum, path, result)
        helper(node.right, sum, path, result)
        path.pop()
        sum += node.val
        print(path, sum)
        return;

    helper(root, sum, path, result)
    return result
```

