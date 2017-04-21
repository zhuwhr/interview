[234. Count Univalue Subtrees](https://leetcode.com/problems/count-univalue-subtrees/)

```python
思路写出来了，题意理解错了。我理解成“数 其某个子树节点值与根的傎一样的 树的个数”，实际上是 "数 所有子节点值都一样 的 树的个数"
例如：根节点 5 不能算 uni value subtree，因为它的子节点中有和它值不一样的。首先所有的叶子节点肯定都算一个 uni value subtree，然后第二层右边的 5-5 也算一棵，但 5-5-5就不算。
		5
      /   \
     1     5
   /  \     \
  5    5     5
理解了题意之后，很快写出标准的递归思路，多么简洁明了的方法啊，这也是自己之前已经掌握了的。所以做题前一定要自己先跑几个test case确保理解清楚了题意，然后就是规矩地写递归，不要哼哧哼哧写迭代好吗
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def check(node):
            if not node: return True
            left = check(node.left)
            right = check(node.right)
            if left and right and (not node.left or node.left.val == node.val) and (not node.right or node.right.val == node.val):
                count[0] += 1
                return True
            return False
        
        count = [0]
        check(root)
        return count[0]
    
    理解错题意的丑代码：
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        uni = [root]
        sub = []
        count = 0
        while uni:
            node = uni.pop()
            if node:
                count += 1
                if node.left:
                    if node.left.val == node.val:
                        sub.append(node.left)
                    else:
                        uni.append(node.left)
                if node.right:
                    if node.right.val == node.val:
                        sub.append(node.right)
                    else:
                        uni.append(node.right)
            while sub:
                node_sub = sub.pop()
                if node_sub:
                    if node_sub.left:
                        if node_sub.left.val == node.val:
                            sub.append(node_sub.left)
                        else:
                            uni.append(node_sub.left)
                    if node_sub.right:
                        if node_sub.right.val == node.val:
                            sub.append(node_sub.right)
                        else:
                            uni.append(node_sub.right)
        return count
```

