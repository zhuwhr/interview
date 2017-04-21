[104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

recursive:

`return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 if root else 0`

iterative:

用一个queue来做，放进去的是每个非空节点，推出来的时候，先记录一下每层的大小，然后一层一层地往外推，每推一层把长度加一。

```python
from collections import deque

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # iterative
        if not root: return 0
        q = deque()
        q.append(root)
        depth = 0
        
        while q:
            level_size = len(q)
            while level_size > 0:
                level_size -= 1
                node = q.pop()
                if node.left:
                    q.appendleft(node.left)
                if node.right:
                    q.appendleft(node.right)
            depth += 1  
        
        return depth
```

