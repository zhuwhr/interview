[337-house-robber-iii](https://leetcode.com/problems/house-robber-iii/#/description)

```python
第一种解法：基本递归
	假设这个方程能算出当前节点的最大值，那么在子节点上同样可以用这个方程算出结果。那么假设我已知所有子，孙节点的值，就可以算这个节点的值了。计算时，要么是本身加所有孙节点(就是抢的情况)，要么是子节点(不抢的情况)，这两种情况取最大值返回就可以了。停止条件是本身为空，没得可抢，返回0.但这种直观的做法复杂度是指数级的，肯定会超时
class Solution(object):
    def rob(self, root):
        if not root: return 0
        val = 0
        if root.left:
            val += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            val += self.rob(root.right.left) + self.rob(root.right.right)
        return max(root.val + val, self.rob(root.left) + self.rob(root.right))
第二种解法：记忆化搜索(DP)
	自上而下，用一个字典把算过的结果存起来
class Solution(object):
    def rob(self, root):
        def helper(node, visited):
            if not node: return 0
            if node in visited: return visited[node]
            
            val = 0
            if node.left:
                val += helper(node.left.left, visited) + helper(node.left.right, visited)
            if node.right:
                val += helper(node.right.left, visited) + helper(node.right.right, visited)
            
            val = max(val + node.val, helper(node.left, visited) + helper(node.right, visited))
            visited[node] = val
            return val
        
        return helper(root, {})
第三种方法：两种情况都记法
	想一下什么情况导致了重复计算？第一种解法里说到的两种情况，这个节点被或者不被抢时，是不是把另一种扔掉了？如果把它记在结果里，这样向下要值的时候，就不用重复递归了，这样每一个节点就是O(1)的操作，整个就是n的复杂度了
class Solution(object):
    def rob(self, root):
        def helper(node):
            # res[0] node is not robbed, res[1] node is robbed
            res = [0, 0]
            if not node: return res
            
            left = helper(node.left)
            right = helper(node.right)
            
            res[0] = max(left[0], left[1]) + max(right[0], right[1])
            res[1] = node.val + left[0] + right[0]
            
            return res
        
        res = helper(root)
        return max(res[0], res[1]) 
```

