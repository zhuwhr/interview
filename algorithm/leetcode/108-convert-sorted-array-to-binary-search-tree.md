[108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)

```python
这个题浪费了挺多时间，卡在以下两点：
第一，不熟悉除法怎么进退，3/2 = 1，在corner case的处理上费了半天时间
第二，不熟悉list怎么取值，还想了半天怎么处理index out of bound
其实这个题很直观，确实是道easy题。这个思考过程很有收获。
还有一个问题就是，用slice取值时，是用了一个deep copy，浪费了很多空间，这道题这么做是可以的，但是construct bt from inorder and preorder这道题就不行了。
讨论里有讲这个问题，看到那题的时候再回来看这题
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None;
        idx = len(nums) / 2
        node = TreeNode(nums[idx])
        node.left = self.sortedArrayToBST(nums[0:idx]) #if len(nums) > 1 else None
        node.right = self.sortedArrayToBST(nums[idx+1:]) #if idx + 1 < len(nums) else None
        return node
```

