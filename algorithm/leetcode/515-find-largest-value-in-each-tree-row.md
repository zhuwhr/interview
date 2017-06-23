[515-find-largest-value-in-each-tree-row](https://leetcode.com/problems/find-largest-value-in-each-tree-row/#/description)

```python
level order变种，一遍过
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        level = [root]
        if not root: return result
        while level:
            largest = float('-inf')
            temp = []
            for node in level:
                largest = max(largest, node.val)
                temp += node.left, node.right
            result.append(largest)
            level = [leaf for leaf in temp if leaf]
        
        return result
```



```python
神解法，level order弱爆了。。。
这种做法适用于不需要记录节点的，光遍历就可以了。如果不需要记住order的结果，用一个stack就可以遍历了
BFS right-to-left:
    只返回最后一个节点(最左侧的)。妙用filter(None, iterable)，妙用python中循环结束后 循环变量还在的特性
def findLeftMostNode(root):
    q = [root]
    for node in q:
        q += filter(None, (node.right, node.left))
    return node.val
```

