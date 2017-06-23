[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

#### 

```python
用队列做BFS题，基本思路是用一个队列存每一层的节点，记录队列的长度做为每层的长度，处理时只做这一层的工作，打印结果并把子节点加到队列中。
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = deque()
        level = []
        result = []
        if not root: return result
        q.append(root)
        while q:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
            level = []
        
        return result
pythonic way:
不需要用队列进来进去，每层更新level就可以
用好list comprehension
用好 if 来处理空节点
def levelOrder(self, root):
    if not root:
        return []
    ans, level = [], [root]
    # while root and level to take the null root case
    while level:
        ans.append([node.val for node in level])
        temp = []
        for node in level:
            temp.extend([node.left, node.right])
        level = [leaf for leaf in temp if leaf]
    return ans
```

#### 