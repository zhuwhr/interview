[508-most-frequent-subtree-sum](https://leetcode.com/problems/most-frequent-subtree-sum/#/description)

```python
思路清晰明了，出了个小bug，一遍过
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def cal_sum(node):
            if not node: return 0
            left = cal_sum(node.left)
            right = cal_sum(node.right)
            subtree_sum = left + right + node.val
            dic[subtree_sum] = dic.get(subtree_sum, 0) + 1
            return subtree_sum
        
        dic = {}
        result = []
        cal_sum(root)
        if dic:
            max_val = max(dic.values())
            for k, v in dic.items():
                if v == max_val:
                    result.append(k)
        return result
```

bug: 一开始没判断 dic 是否为空，当max()里面为空值的时候会报错。像root为空这种情况，要不以后就单独拉出来一行算了，省得再出这种意外的bug。