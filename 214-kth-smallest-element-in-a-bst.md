[214. Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/)

```python
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        #use an array to store elements, O(n) space but O(1) lookup
        def inorder(node):
            if not node: return
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        nodes = []
        inorder(root)
        return nodes[k - 1]
        '''O(1) space, but is not good for frequent insert and delete
        count = [0]
        result = [0]
        def inorder(node):
            if not node: return;
            inorder(node.left)
            count[0] += 1
            print(count[0])
            if count[0] == k:
                result[0] = node.val
                return;
            inorder(node.right)
        
        inorder(root)
        return result[0]
        '''
```

