[110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/)

旧解法 getHeight() 调用了很多次，子节点被重复计算了。这里做的改进是，不像之前一样，每一次递归都算一遍子树的高度了。用这类题的三步曲，往左右各要一个高度，这个高度是左右子树的最大高度。要上来后判断一下这两个高度相差是不是大于1，如果大于1就返上去一个-1，意思是高度差大于1了，应该返回false了。如果不大于1，返上去两个的最大值再加1。如果传上来的数就是-1，说明这个树已经不平衡了，返回上去一个-1就可以。

```python
def isBalancedTree(root):
    # input TreeNode, output: boolean
    def helper(root):
        # input TreeNode, output: int
        if not root: return 0
        left, right = (helper(child) for child in (root.left, root.right))
        if left == -1 or right == -1 or abs(left - right) > 1: return -1
        return max(left, right) + 1
    
    return helper(root) != -1
    
```



旧解法：

O(nlogn)

```java
public boolean isBalanced(TreeNode root) {
  if (root == null) return true;
  int diff = getHeight(root.left) - getHeight(root.right);
  if (Math.abs(diff) > 1) return false
  return isBalanced(root.left) && isBalanced(root.right);
}
```

