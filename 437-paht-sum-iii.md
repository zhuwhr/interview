437. [path sum iii](https://leetcode.com/problems/path-sum-iii/#/description)

任意节点，存不存在一个目标，返回满足条件的路径数目

```python
def pathSum(self, root, sum):
    """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
    path = []
    count = [0]
    def countPathSum(node, sum, path):
        if not node: return;
        path.append(node.val)
        findTarget(sum, path)
        countPathSum(node.left, sum, path)
        countPathSum(node.right, sum, path)
        path.pop()

    def findTarget(target, path):
        cur = 0
        for value in reversed(path):
            cur += value
            if cur == target: count[0] += 1

    countPathSum(root, sum, path)
    return count[0]
```

bug：有值为零的结点，可能会带来多条路径。因此这个题让我数数，不像判断有没有的，看准了就可以返回了。这个题要在判断的函数里不断地数，防止有0出现的情况发生。

```python
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        path = []
        count = [0]
        def countPathSum(node, sum, path):
            if not node: return;
            path.append(node.val)
            if findTarget(sum, path):
                count[0] += 1
            countPathSum(node.left, sum, path)
            countPathSum(node.right, sum, path)
            path.pop()
        
        def findTarget(target, path):
            cur = 0
            for value in reversed(path):
                cur += value
                if cur == target: return True
            return False
            
        countPathSum(root, sum, path)
        return count[0]
```

找直上直下path题目的复杂度，从根到叶一般是O(n)，因为基本思路就是每个节点都处理一遍。任意节点一般都是O(n logn)，因为每碰到一个节点都要回看一下，这一看就是O(log n) 因为最坏要看整个树高，一共有n个点，所以复杂度是O(n logn)