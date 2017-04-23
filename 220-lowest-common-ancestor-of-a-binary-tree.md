[220. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)



```python
找最低共同祖先
case1：直接隶属关系
	往下要的是：有没有？
    自己的处理是：看看自己是不是？
    往上报的是：有没有？哪个？
case2：非直接隶属关系
	往下要的是：有没有？
    自己的处理是：看看报上来的，左右都空就报空，左右仅一空就报非空，左右都不空就报自己
    往上报的是：有没有？哪个？
    
优化：
往下要的是：左右有没有出现p, q
自己的处理：
想一下上面那两种情况，首先自己如果是p, q之一，那么有两种情况，一种是自己下面还有另一个节点，这时候自己就是LCA，返回自己。另一种是自己下面没有节点了，但自己是其中之一，要向上级汇报自己找到了，还是要返回自己。于是我们知道，无论下面找没找到，只要自己就是p, q之一，那么一定是返回自己。另外，如果自己是空，应该返回空，也相当于返回自己。所以，如果自己是None, p, q中的任何一个，都应该返回自己。这里面也包含了上面那个case1
然后再处理从左右要上来的两个值：如果这两个值分别返上来两个要找的node，这时说明自己就是LCA，返回自己。如果这两个值有一个None，另一个是Node，这时的这个Node有可能是两种情况，一种是两个都找到之后返回的那个LCA被返回来了，另一种是只找到一个，然后返回来了。但无论这个Node是哪种情况，在这一层，都应该返回这个找上来的Node。

def lowestCommonAncestor(self, root, p, q):
    """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    if root in (None, p, q): return root
    left, right = (self.lowestCommonAncestor(child, p, q) for child in (root.left, root.right))

    return root if left and right else left or right

这里注意返回时python的一个小trick：root if left and right else left or right。这个else后面跟的应该是判断条件不满足的情况下返回的值。这个值可以用or来连接，返回其中为真的那个，如果都不为真，返回的是None

或者另外一个奇淫技巧：using that None is considered smaller than any node:
def lowestCommonAncestor(self, root, p, q):
    if root in (None, p, q): return root
    subs = [self.lowestCommonAncestor(kid, p, q)
            for kid in (root.left, root.right)]
    return root if all(subs) else max(subs)

迭代的做法：
利用一个祖先路径字典。首先用一个栈，把每层的节点往里压，直到找到p, q为止，压的过程中把它们的祖先都保存在地图路径中。当p,q都被找到后，意味着它们的所有祖先都被保存在这个字典中了。
然后用一个set，先把p 的祖先全都提取出来，然后从q的祖先链上一个一个的往上找，直到找到为止。
当找到root还是空的时候，返回空，没找到。
def lowestCommonAncestor(self, root, p, q):
    """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
    if not root: return root

    stack = [root]
    parent = {root: None}

    while p not in parent or q not in parent:
        node = stack.pop()
        if node.left:
            parent[node.left] = node
            stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

     ancestors = set()
     while p:
        ancestors.add(p)
        p = parent[p]
     while q not in ancestors:
        q = parent[q]

     return q
```

